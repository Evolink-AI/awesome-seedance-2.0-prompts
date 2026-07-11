#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from http.client import IncompleteRead
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "Evolink-AI/awesome-seedance-2.0-prompts"
STAR_RE = re.compile(r"star-history\.com|Star History", re.I)


def stars() -> tuple[int, str]:
    url = f"https://api.github.com/repos/{REPOSITORY}"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "seedance-prompt-star-gate"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    last_error: Exception | None = None
    for _ in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=20) as response:
                return int(json.load(response)["stargazers_count"]), url
        except (IncompleteRead, OSError, ValueError, KeyError) as exc:
            last_error = exc
    gh = subprocess.run(["gh", "api", f"repos/{REPOSITORY}", "--jq", ".stargazers_count"], capture_output=True, text=True)
    if gh.returncode == 0 and gh.stdout.strip().isdigit():
        return int(gh.stdout.strip()), f"gh api repos/{REPOSITORY}"
    raise RuntimeError(f"live star read failed: {last_error}; {gh.stderr.strip()}")


def main() -> int:
    try:
        count, source = stars()
    except Exception as exc:
        print(f"Star History verification: BLOCKED\n- {exc}")
        return 1
    errors: list[str] = []
    for path in sorted(ROOT.glob("README*.md")):
        text = path.read_text(encoding="utf-8").rstrip()
        present = bool(STAR_RE.search(text))
        if count < 10 and present:
            errors.append(f"{path.name}: Star History must be hidden at {count} stars")
        if count >= 10 and (not present or not text.endswith("&Date)")):
            errors.append(f"{path.name}: Star History must be the final element at {count} stars")
    if errors:
        print("Star History verification: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    expected = "hidden" if count < 10 else "visible-at-end"
    print("Star History verification: PASS")
    print(f"- Repository: {REPOSITORY}")
    print(f"- Live stars: {count}")
    print(f"- Expected: {expected}")
    print(f"- Checked at: {datetime.now(timezone.utc).isoformat()}")
    print(f"- Source: {source}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
