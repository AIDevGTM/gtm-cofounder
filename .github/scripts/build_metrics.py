#!/usr/bin/env python3
"""Regenerate METRICS.md: one place for skills.sh installs, GitHub clones/views, and website visits."""
import csv, json, os, datetime

def read_csv(p):
    if not os.path.exists(p): return []
    with open(p) as f: return list(csv.DictReader(f))

def num(x):
    try: return int(float(x))
    except Exception: return 0

traffic = read_csv("traffic/traffic-daily.csv")
clones_total = sum(num(r.get("clones")) for r in traffic)
views_total  = sum(num(r.get("views"))  for r in traffic)
recent = traffic[-14:]
clones_recent = sum(num(r.get("clones")) for r in recent)
clones_recent_u = sum(num(r.get("clones_unique")) for r in recent)
views_recent  = sum(num(r.get("views")) for r in recent)
first_date = traffic[0]["date"] if traffic else "n/a"
last_date  = traffic[-1]["date"] if traffic else "n/a"

sk = read_csv("metrics/skills-installs.csv")
sk_installs = sk[-1]["installs_display"] if sk else "n/a"
sk_date     = sk[-1]["date"] if sk else "n/a"

manual = json.load(open("metrics/manual.json")) if os.path.exists("metrics/manual.json") else {}
web = manual.get("website", {})

today = datetime.date.today().isoformat()

md = f"""# gtm-cofounder · metrics

_Auto-generated weekly by `.github/workflows/traffic-snapshot.yml`. Last updated: {today}._

The three signals in one place. **Report skills.sh installs as the headline install number** (it is all-time and CLI-specific).

![Daily clones](metrics/clones-trend.svg)

| Metric | Value | Source | Notes |
|---|---|---|---|
| **skills.sh installs (all-time)** | **{sk_installs}** | skills.sh CLI | scraped {sk_date}; the cleanest install number |
| **GitHub clones (cumulative, tracked)** | **{clones_total:,}** | GitHub traffic | since {first_date}; CLI + plugin + manual clone |
| GitHub clones (last 14 days) | {clones_recent:,} ({clones_recent_u:,} unique) | GitHub traffic | rolling |
| GitHub views (cumulative, tracked) | {views_total:,} | GitHub traffic | since {first_date} |
| Website visitors | {web.get('visitors','n/a')} | {web.get('source','Lovable')} | {web.get('period','')}, as of {web.get('as_of','')} (manual) |

## What each number is
- **skills.sh installs**: every `npx skills add` install, all-time. Public at <https://skills.sh/aidevgtm/gtm-cofounder> (no login). Coarse to ~0.1K.
- **GitHub clones**: installs via the Claude Code plugin and manual `git clone` that skills.sh doesn't see. Cumulative here only since tracking began ({first_date}), because GitHub's API only keeps 14 days.
- **Website visitors**: top of funnel. Mostly not your ICP (heavy mobile/India on the last read), so treat installs, not visits, as the result.

## How this updates
- GitHub clones/views: automatic weekly (needs the `TRAFFIC_TOKEN` secret).
- skills.sh installs: automatic weekly scrape of the pack page.
- Website visitors: manual — Lovable has no public API. Edit `metrics/manual.json` when you check the dashboard.
"""
with open("METRICS.md","w") as f: f.write(md)
print(f"wrote METRICS.md (skills={sk_installs}, clones_total={clones_total}, views_total={views_total})")
