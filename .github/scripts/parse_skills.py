import sys, re
text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", sys.stdin.read()))
m = re.search(r"([\d.,]+\s*[KkMm]?)\s*total installs", text)
print(m.group(1).strip() if m else "")
