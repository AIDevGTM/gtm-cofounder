#!/usr/bin/env python3
"""Validate gtm-cofounder's shipped content on every push and pull request.

Enforces the contract CONTRIBUTING.md documents:
- every skills/NN-<name>/SKILL.md opens with a YAML frontmatter block whose
  name matches the directory name and whose description is present,
- skill numeric prefixes are unique,
- the plugin and metrics JSON manifests parse,
- every workflow YAML parses.

Exit 0 when the repo is valid, 1 with a report otherwise.
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = re.compile(r"^(\d{2})-[a-z0-9-]+$")
problems = []


def fail(msg):
    problems.append(msg)


def main():
    # JSON manifests parsed by the plugin / marketplace and the metrics job.
    for rel in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json", "metrics/manual.json"):
        p = ROOT / rel
        try:
            json.loads(p.read_text())
        except Exception as e:
            fail(f"{rel}: invalid JSON: {e}")

    # Workflow YAML, so a malformed workflow cannot silently ship.
    for wf in sorted((ROOT / ".github/workflows").glob("*.yml")):
        try:
            yaml.safe_load(wf.read_text())
        except Exception as e:
            fail(f"{wf.relative_to(ROOT)}: invalid YAML: {e}")

    # Skills: NN-<kebab> directory with a SKILL.md frontmatter contract.
    skills = sorted(d for d in (ROOT / "skills").iterdir() if d.is_dir())
    prefixes = {}
    for d in skills:
        m = SKILL_DIR.match(d.name)
        if not m:
            fail(f"skills/{d.name}: directory must be NN-<kebab-name>")
            continue
        prefix, kebab = m.group(1), d.name[3:]
        if prefix in prefixes:
            fail(f"skills/{d.name}: duplicate numeric prefix {prefix} (already used by skills/{prefixes[prefix]})")
        else:
            prefixes[prefix] = d.name

        skill_file = d / "SKILL.md"
        if not skill_file.is_file():
            fail(f"skills/{d.name}: missing SKILL.md")
            continue
        lines = skill_file.read_text().splitlines()
        if not lines or lines[0].strip() != "---":
            fail(f"skills/{d.name}/SKILL.md: frontmatter must start with a '---' fence")
            continue
        end = None
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                end = i
                break
        if end is None:
            fail(f"skills/{d.name}/SKILL.md: frontmatter has no closing '---' fence")
            continue
        try:
            meta = yaml.safe_load("\n".join(lines[1:end]))
        except Exception as e:
            fail(f"skills/{d.name}/SKILL.md: frontmatter is not valid YAML: {e}")
            continue
        if not isinstance(meta, dict):
            fail(f"skills/{d.name}/SKILL.md: frontmatter must be a YAML mapping")
            continue
        if meta.get("name") != kebab:
            fail(f"skills/{d.name}/SKILL.md: frontmatter name is {meta.get('name')!r}, expected {kebab!r}")
        if not meta.get("description"):
            fail(f"skills/{d.name}/SKILL.md: frontmatter description is missing or empty")

    if problems:
        print("gtm-cofounder content validation failed:")
        for p in problems:
            print(f"- {p}")
        sys.exit(1)
    print(f"ok: {len(skills)} skills, manifests and workflows valid")


if __name__ == "__main__":
    main()
