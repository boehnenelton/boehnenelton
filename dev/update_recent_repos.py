#!/data/data/com.termux/files/usr/bin/env python3
"""
Name:          update_recent_repos.py
Description:   Update the Recently Updated Repositories section at the top of README.md
Version:       10000
Date Created:  2026-11-12
Author Credit: Elton Boehnen · boehnenelton2024@gmail.com · boehnenelton2024.pages.dev · github.com/boehnenelton
License:       PolyForm Noncommercial License 1.0.0 (PolyForm-Noncommercial-1.0.0)
RELATIONAL_ID: GUID_PLACEHOLDER
"""

import argparse
import json
import logging
import re
import subprocess
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("update_recent_repos")

REPO_ROOT = Path(__file__).resolve().parent.parent
README_PATH = REPO_ROOT / "README.md"

CURATED_DESCRIPTIONS = {
    "Android_Compiler": "Automated Android Gradle build system, APK compilation engine, target selector, and Flask management web service.",
    "NewAgent": "Autonomous AI coding assistant, task graph orchestrator, and execution platform for local developer environments.",
    "backup-tool-agy": "Universal config-driven 10-slot snapshot system, disc changer, and Flask web lifecycle manager.",
}

SECTION_HEADER = "## Recently Updated Repositories\n\n"
MARKER_START = "<!-- RECENT_REPOS_START -->\n"
MARKER_END = "<!-- RECENT_REPOS_END -->\n"


def fetch_repositories(limit: int = 50) -> list[dict]:
    cmd = [
        "gh",
        "repo",
        "list",
        "boehnenelton",
        "--limit",
        str(limit),
        "--json",
        "name,description,updatedAt,isPrivate,url",
    ]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        repos = json.loads(proc.stdout)
    except Exception as exc:
        logger.error(f"Failed to fetch repositories via gh CLI: {exc}")
        sys.exit(1)

    public_repos = [r for r in repos if not r.get("isPrivate") and r.get("name") != "boehnenelton"]
    public_repos.sort(key=lambda x: x.get("updatedAt", ""), reverse=True)
    return public_repos


def generate_markdown(repos: list[dict]) -> str:
    lines = [
        MARKER_START,
        "A clean, direct directory of recently updated open-source repositories across the Boehnen software ecosystem:\n\n",
    ]
    for r in repos:
        name = r["name"]
        url = r["url"]
        desc = (r.get("description") or "").strip()
        if not desc and name in CURATED_DESCRIPTIONS:
            desc = CURATED_DESCRIPTIONS[name]
        elif not desc:
            desc = "Open-source ecosystem component and developer utility."

        if not desc.endswith("."):
            desc += "."

        raw_date = r.get("updatedAt", "")
        date_str = raw_date[:10] if len(raw_date) >= 10 else ""
        date_tag = f" *(Updated {date_str})*" if date_str else ""

        lines.append(f"- [`{name}`]({url}) — {desc}{date_tag}\n")

    lines.append("\n" + MARKER_END)
    return "".join(lines)


def update_readme(dry_run: bool = False) -> None:
    if not README_PATH.is_file():
        logger.error(f"README not found at {README_PATH}")
        sys.exit(1)

    content = README_PATH.read_text(encoding="utf-8")
    repos = fetch_repositories()
    recent_block = generate_markdown(repos)

    if MARKER_START in content and MARKER_END in content:
        pattern = re.compile(
            re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
            re.DOTALL,
        )
        new_content = pattern.sub(recent_block.strip() + "\n", content)
    else:
        # Insert at the top right above ## Table of Contents
        target = "## Table of Contents"
        if target in content:
            replacement = f"{SECTION_HEADER}{recent_block}\n---\n\n{target}"
            new_content = content.replace(target, replacement, 1)

            # Also update Table of Contents to include the new section
            toc_marker = "## Table of Contents\n\n"
            if toc_marker in new_content:
                toc_entry = "- [Recently Updated Repositories](#recently-updated-repositories)\n"
                if toc_entry not in new_content:
                    new_content = new_content.replace(toc_marker, f"{toc_marker}{toc_entry}", 1)
        else:
            logger.error(f"Anchor '{target}' not found in README.md")
            sys.exit(1)

    if dry_run:
        logger.info("[Dry Run] Generated recently updated repositories block:\n" + recent_block)
        return

    README_PATH.write_text(new_content, encoding="utf-8")
    logger.info(f"Successfully updated {README_PATH} with {len(repos)} repositories.")


def main():
    parser = argparse.ArgumentParser(description="Update recently updated repos list in profile README.")
    parser.add_argument("--dry-run", action="store_true", help="Print output without writing to file.")
    args = parser.parse_args()
    update_readme(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
