"""Batch-export MoTeC i2 style section statistics from .ld telemetry files.

Each .ld file needs its .ldx file next to it (the lap marks come from there).

Usage:
    python extract.py SECTIONS_CSV OUTPUT_CSV LD_FILE_OR_DIR [...]

SECTIONS_CSV has columns `name,start_m`: each section runs from its start_m
(Lap Distance, metres from the start/finish line) to the next start_m; the
last one runs to the end of the lap. The first section always starts at the
lap line, so its start_m is ignored.

Output: one row per file x lap x section, with `<channel> [<unit>] <stat>`
columns for Min, Max, Range, Avg, Start, End, Std Dev.
Partial laps (the out lap and the last lap of a file) are skipped.
"""
import csv
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

from ldfile import read_ld

CHANNELS = [
    ("Steering Angle", "°"),
    ("Ground Speed", "km/h"),
    ("Brake Pos", "%"),
    ("Abs Lateral G", "G"),
    ("CG Accel Lateral", "G"),
    ("CG Accel Longitudinal", "G"),
    ("CG Accel Vertical", "G"),
]
STATS = ["Min", "Max", "Range", "Avg", "Start", "End", "Std Dev"]


def section_stats(t, y, t0, t1):
    inside = (t > t0) & (t < t1)
    ts = np.concatenate(([t0], t[inside], [t1]))
    ys = np.concatenate(([np.interp(t0, t, y)], y[inside], [np.interp(t1, t, y)]))
    avg = np.trapezoid(ys, ts) / (t1 - t0)
    std = np.sqrt(np.trapezoid((ys - avg) ** 2, ts) / (t1 - t0))
    return [ys.min(), ys.max(), ys.max() - ys.min(), avg, ys[0], ys[-1], std]


def extract(ld_path, sections):
    head, ch = read_ld(ld_path)
    ch["Abs Lateral G"] = (ch["CG Accel Lateral"][0], "G", np.abs(ch["CG Accel Lateral"][2]))

    freq, _, dist = ch["Lap Distance"]
    lap_no = ch["Lap Number"][2]
    t = np.arange(len(dist)) / freq
    jumps = np.diff(dist, prepend=dist[0])
    offset = np.cumsum(np.where(jumps < -1000, -jumps, 0))
    ldx = ET.parse(Path(ld_path).with_suffix(".ldx"))
    beacons = [float(m.get("Time")) / 1e6 for m in ldx.iter("Marker") if m.get("ClassName") == "BCN"]

    for t0, t1 in zip(beacons[:-1], beacons[1:]):
        a, b = np.searchsorted(t, [t0, t1])
        lap_d = np.maximum.accumulate(dist[a:b] + offset[a:b] - offset[(a + b) // 2])
        starts = [t0] + [np.interp(s, lap_d, t[a:b]) for s in list(sections.values())[1:]] + [t1]
        for i, name in enumerate(sections):
            row = {"file": Path(ld_path).name, "driver": head["driver"], "car": head["vehicle"],
                   "track": head["venue"], "lap": int(lap_no[(a + b) // 2]),
                   "lap_time_s": round(t1 - t0, 3), "section": name,
                   "section_time_s": round(starts[i + 1] - starts[i], 3)}
            for cname, unit in CHANNELS:
                cf, _, y = ch[cname]
                vals = section_stats(np.arange(len(y)) / cf, y, starts[i], starts[i + 1])
                row.update({f"{cname} [{unit}] {s}": round(v, 4) for s, v in zip(STATS, vals)})
            yield row


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    with open(sys.argv[1], newline="") as f:
        sections = {r["name"]: float(r["start_m"]) for r in csv.DictReader(f)}
    files = []
    for arg in sys.argv[3:]:
        p = Path(arg)
        files += sorted(p.glob("*.ld")) if p.is_dir() else [p]

    writer = None
    with open(sys.argv[2], "w", newline="") as out:
        for ld in files:
            for row in extract(ld, sections):
                if writer is None:
                    writer = csv.DictWriter(out, fieldnames=list(row))
                    writer.writeheader()
                writer.writerow(row)
            print(f"done: {ld.name}")


if __name__ == "__main__":
    main()
