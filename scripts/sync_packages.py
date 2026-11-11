#!/usr/bin/env python3
"""Rewrite the package table in profile/README.md from the organization's repos.

Any public repo in the org carrying the `miyu-package` topic shows up here.
Run by .github/workflows/sync-readme.yml, or by hand:

    GITHUB_TOKEN=... python scripts/sync_packages.py
"""
import json
import os
import re
import urllib.request
from pathlib import Path

ORG = os.environ.get("ORG", "Mymiyu-tool")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
README = Path("profile/README.md")
START, END = "<!-- packages:start -->", "<!-- packages:end -->"


def api(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    repos, page = [], 1
    while True:
        chunk = api(f"https://api.github.com/orgs/{ORG}/repos?per_page=100&type=public&page={page}")
        if not chunk:
            break
        repos.extend(chunk)
        if len(chunk) < 100:
            break
        page += 1

    pkgs = [
        r for r in repos
        if "miyu-package" in (r.get("topics") or [])
        and not r.get("archived")
        and not r["name"].startswith(".")
        and r["name"] != "packages"
    ]
    pkgs.sort(key=lambda r: r["name"])

    rows = ["| 包 | 说明 | 仓库 |", "|---|---|---|"]
    for r in pkgs:
        desc = (r.get("description") or "").replace("|", "\\|").strip() or "—"
        rows.append(f"| **{r['name']}** | {desc} | [{r['full_name']}]({r['html_url']}) |")
    if not pkgs:
        rows.append("| — | 还没有带 `miyu-package` topic 的仓库 | — |")

    text = README.read_text(encoding="utf-8")
    block = "\n".join(rows)
    new, n = re.subn(
        f"{re.escape(START)}.*?{re.escape(END)}",
        f"{START}\n{block}\n{END}",
        text,
        flags=re.S,
    )
    if n == 0:
        raise SystemExit(f"markers {START} / {END} not found in {README}")

    if new == text:
        print("no change")
        return
    README.write_text(new, encoding="utf-8")
    print(f"updated with {len(pkgs)} packages")


if __name__ == "__main__":
    main()
