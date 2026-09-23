"""Minimal reader for MoTeC .ld telemetry files (as written by Telemetrick / ACC)."""
import struct

import numpy as np

HEAD = struct.Struct("<I4xII20xI24xHHHI8sHHI4x16s16x16s16x64s64s64x64s64x1024xI66x64s126x")
CHAN = struct.Struct("<IIIIHHHHhhhh32s8s12s40x")
DTYPES = {(0x07, 2): "<f2", (0x07, 4): "<f4", (0x00, 2): "<i2", (0x03, 2): "<i2",
          (0x05, 2): "<i2", (0x00, 4): "<i4", (0x03, 4): "<i4", (0x05, 4): "<i4", (0x08, 8): "<f8"}


def _str(b):
    return b.decode("latin-1").rstrip("\0").strip()


def read_ld(path):
    """Return (header dict, {channel name: (freq Hz, unit, np.ndarray)})."""
    with open(path, "rb") as f:
        buf = f.read()
    h = HEAD.unpack_from(buf, 0)
    head = {"driver": _str(h[14]), "vehicle": _str(h[15]), "venue": _str(h[16]),
            "date": _str(h[12]), "time": _str(h[13])}
    channels = {}
    ptr = h[1]
    while ptr:
        (_, nxt, data_ptr, n, _, dtype_a, size, freq, shift, mul, scale, dec,
         name, _, unit) = CHAN.unpack_from(buf, ptr)
        dtype = DTYPES.get((dtype_a, size))
        if dtype:
            raw = np.frombuffer(buf, dtype=dtype, count=n, offset=data_ptr).astype(float)
            channels[_str(name)] = (freq, _str(unit), (raw / scale * 10.0 ** -dec + shift) * mul)
        ptr = nxt
    return head, channels
