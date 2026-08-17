#!/usr/bin/env python3
"""Regenerate METRICS.md: skills.sh installs (the headline) and website visits (manual). No auth needed."""
import csv, json, os, datetime

def read_csv(p):
    if not os.path.exists(p): return []
    with open(p) as f: return list(csv.DictReader(f))

sk = read_csv("metrics/skills-installs.csv")
sk_installs = sk[-1]["installs_display"] if sk else "n/a"
sk_date     = sk[-1]["date"] if sk else "n/a"

manual = json.load(open("metrics/manual.json")) if os.path.exists("metrics/manual.json") else {}
web = manual.get("website", {})

today = datetime.date.today().isoformat()

md = f"""# gtm-cofounder · metrics

_Auto-generated weekly by `.github/workflows/traffic-snapshot.yml`. Last updated: {today}._

**Report skills.sh installs as the headline install number** (it is all-time and CLI-specific).

| Metric | Value | Source | Notes |
|---|---|---|---|
| **skills.sh installs (all-time)** | **{sk_installs}** | skills.sh CLI | scraped {sk_date}; the cleanest install number |
| Website visitors | {web.get('visitors','n/a')} | {web.get('source','Lovable')} | {web.get('period','')}, as of {web.get('as_of','')} (manual) |

## What each number is
- **skills.sh installs**: every `npx skills add` install, all-time. Public at <https://skills.sh/aidevgtm/gtm-cofounder> (no login). Coarse to ~0.1K. This is the headline install number.
- **Website visitors**: top of funnel. Mostly not your ICP (heavy mobile on the last read), so treat installs, not visits, as the result.

## How this updates
- skills.sh installs: automatic weekly scrape of the pack page, no auth needed.
- Website visitors: manual, Lovable has no public API. Edit `metrics/manual.json` when you check the dashboard.
"""
with open("METRICS.md", "w") as f:
    f.write(md)
print(f"wrote METRICS.md (skills={sk_installs})")
