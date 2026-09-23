"""Batch-export MoTeC i2 style section statistics from .ld telemetry files.

Each .ld file needs its .ldx file next to it (the lap marks come from there).

Usage:
    python extract.py SECTIONS_CSV OUTPUT_CSV LD_FILE_OR_DIR [...]

SECTIONS_CSV has columns `name,x,y`: each section starts where the car passes
the track point (x, y) (Car Coord X/Y, metres) and ends where the next one
starts; the last one runs to the end of the lap. The first section always
starts at the lap line, so its point is ignored. Points are used instead of
Lap Distance because Lap Distance jumps when the car spins or leaves the track.

Output: one row per file x lap x section, with `<channel> [<unit>] <stat>`
columns for Min, Max, Range, Avg, Start, End, Std Dev. Laps are numbered from
1 = the first complete lap, as in i2. Partial laps (the out lap and the last
lap of a file) are skipped, and so are laps that miss a section point.
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
    ys = np.concatenate(([np.interp(t0, t, y)], y[inside], [np.interp(t1, t, y)]))
    return [ys.min(), ys.max(), ys.max() - ys.min(), ys.mean(), ys[0], ys[-1], ys[:-1].std(ddof=1)]


def pass_time(t, pos, p, i0, radius=25.0):
    d = np.hypot(*(pos[i0:] - p).T)
    near = np.flatnonzero(d < radius)
    if not near.size:
        return None, None
    run = np.split(near, np.flatnonzero(np.diff(near) > 1) + 1)[0]
    j = min(max(i0 + run[np.argmin(d[run])], 1), len(t) - 2)
    f = (pos[j - 1:j + 2] - p) @ (pos[j + 1] - pos[j - 1])
    return np.interp(0, f, t[j - 1:j + 2]), j


def extract(ld_path, sections):
    head, ch = read_ld(ld_path)
    ch["Abs Lateral G"] = (ch["CG Accel Lateral"][0], "G", np.abs(ch["CG Accel Lateral"][2]))

    freq = ch["Car Coord X"][0]
    pos = np.column_stack([ch["Car Coord X"][2], ch["Car Coord Y"][2]])
    t = np.arange(len(pos)) / freq
    ldx = ET.parse(Path(ld_path).with_suffix(".ldx"))
    beacons = [float(m.get("Time")) / 1e6 for m in ldx.iter("Marker") if m.get("ClassName") == "BCN"]

    for lap, (t0, t1) in enumerate(zip(beacons[:-1], beacons[1:]), 1):
        starts, i = [t0], np.searchsorted(t, t0)
        for p in list(sections.values())[1:]:
            tp, i = pass_time(t, pos, np.array(p), i)
            if tp is None or tp >= t1:
                print(f"skipped: {Path(ld_path).name} lap {lap} (missed a section point)")
                break
            starts.append(tp)
        else:
            starts.append(t1)
            for k, name in enumerate(sections):
                row = {"file": Path(ld_path).name, "driver": head["driver"], "car": head["vehicle"],
                       "track": head["venue"], "lap": lap, "lap_time_s": round(t1 - t0, 3),
                       "section": name, "section_time_s": round(starts[k + 1] - starts[k], 3)}
                for cname, unit in CHANNELS:
                    cf, _, y = ch[cname]
                    vals = section_stats(np.arange(len(y)) / cf, y, starts[k], starts[k + 1])
                    row.update({f"{cname} [{unit}] {s}": round(v, 4) for s, v in zip(STATS, vals)})
                yield row


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    with open(sys.argv[1], newline="") as f:
        sections = {r["name"]: (float(r["x"]), float(r["y"])) for r in csv.DictReader(f)}
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
