import json, csv, os
CSV = "traffic/traffic-daily.csv"
FIELDS = ["date", "clones", "clones_unique", "views", "views_unique"]
rows = {}
if os.path.exists(CSV):
    with open(CSV) as f:
        for r in csv.DictReader(f):
            rows[r["date"]] = r
def merge(path, json_key, count_field, uniq_field):
    if not os.path.exists(path):
        return
    with open(path) as f:
        data = json.load(f)
    for d in data.get(json_key, []):
        date = d["timestamp"][:10]
        row = rows.get(date, {k: "" for k in FIELDS})
        row["date"] = date
        row[count_field] = d.get("count", "")
        row[uniq_field] = d.get("uniques", "")
        rows[date] = row
merge("clones.json", "clones", "clones", "clones_unique")
merge("views.json", "views", "views", "views_unique")
os.makedirs("traffic", exist_ok=True)
with open(CSV, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for date in sorted(rows):
        r = rows[date]
        w.writerow({k: r.get(k, "") for k in FIELDS})
print(f"wrote {len(rows)} days to {CSV}")
