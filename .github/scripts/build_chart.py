#!/usr/bin/env python3
"""Render metrics/clones-trend.svg from traffic/traffic-daily.csv (no dependencies)."""
import csv, os, math

def num(x):
    try: return int(float(x))
    except Exception: return 0

rows = []
if os.path.exists("traffic/traffic-daily.csv"):
    with open("traffic/traffic-daily.csv") as f:
        rows = list(csv.DictReader(f))
rows.sort(key=lambda r: r["date"])
if not rows:
    rows = [{"date": "n/a", "clones": "0", "clones_unique": "0"}]

dates  = [r["date"] for r in rows]
clones = [num(r.get("clones")) for r in rows]
uniq   = [num(r.get("clones_unique")) for r in rows]

W, H = 820, 280
ML, MR, MT, MB = 48, 20, 40, 44
pw, ph = W - ML - MR, H - MT - MB
n = len(rows)

def nice(v):
    if v <= 0: return 1
    mag = 10 ** int(math.log10(v))
    for m in (1, 2, 2.5, 5, 10):
        if m * mag >= v: return int(m * mag)
    return int(10 * mag)
ymax = nice(max(max(clones + uniq), 1))

def X(i): return ML + (pw * (i / (n - 1)) if n > 1 else pw / 2)
def Y(v): return MT + ph * (1 - v / ymax)
def line(vals): return " ".join(("M" if i == 0 else "L") + f"{X(i):.1f} {Y(v):.1f}" for i, v in enumerate(vals))
area = line(clones) + f" L{X(n-1):.1f} {MT+ph:.1f} L{X(0):.1f} {MT+ph:.1f} Z"

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="ui-monospace,Menlo,monospace">']
s.append(f'<rect width="{W}" height="{H}" rx="12" fill="#0e1118"/>')
s.append(f'<text x="{ML}" y="24" fill="#eef1f6" font-size="14" font-weight="700">Daily clones (installs proxy)</text>')
for yv in (0, ymax // 2, ymax):
    yy = Y(yv)
    s.append(f'<line x1="{ML}" y1="{yy:.1f}" x2="{W-MR}" y2="{yy:.1f}" stroke="#ffffff" stroke-opacity="0.08"/>')
    s.append(f'<text x="{ML-8}" y="{yy+4:.1f}" fill="#7f8797" font-size="10" text-anchor="end">{yv}</text>')
s.append(f'<path d="{area}" fill="#2fe6a8" fill-opacity="0.12"/>')
s.append(f'<path d="{line(clones)}" fill="none" stroke="#2fe6a8" stroke-width="2"/>')
s.append(f'<path d="{line(uniq)}" fill="none" stroke="#2fe6a8" stroke-opacity="0.5" stroke-width="1.5" stroke-dasharray="4 4"/>')
for i in sorted(set([0, n // 2, n - 1])):
    s.append(f'<text x="{X(i):.1f}" y="{H-16}" fill="#7f8797" font-size="10" text-anchor="middle">{dates[i][5:]}</text>')
lx = W - MR - 150
s.append(f'<line x1="{lx}" y1="20" x2="{lx+18}" y2="20" stroke="#2fe6a8" stroke-width="2"/>')
s.append(f'<text x="{lx+24}" y="24" fill="#7f8797" font-size="10">total</text>')
s.append(f'<line x1="{lx+70}" y1="20" x2="{lx+88}" y2="20" stroke="#2fe6a8" stroke-opacity="0.5" stroke-width="1.5" stroke-dasharray="4 4"/>')
s.append(f'<text x="{lx+94}" y="24" fill="#7f8797" font-size="10">unique</text>')
s.append('</svg>')
os.makedirs("metrics", exist_ok=True)
open("metrics/clones-trend.svg", "w").write("\n".join(s))
print(f"wrote metrics/clones-trend.svg ({n} points, ymax={ymax})")
