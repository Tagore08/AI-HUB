#!/usr/bin/env python3
"""
build_instructions.py
Generates platform instruction files from INSTRUCTIONS/CANONICAL.md.
Uses only the Python standard library.
"""

import sys
import os
import difflib
from pathlib import Path

HEADER = "<!-- AUTO-GENERATED from INSTRUCTIONS/CANONICAL.md: DO NOT EDIT -->\n\n"

TARGETS = [
    Path("CLAUDE.md"),
    Path("GEMINI.md"),
    Path(".github/copilot-instructions.md"),
]

def main():
    repo_root = Path(__file__).resolve().parent.parent.parent
    canonical_file = repo_root / "INSTRUCTIONS" / "CANONICAL.md"

    if not canonical_file.exists():
        print(f"ERROR: Canonical rules file not found: {canonical_file}", file=sys.stderr)
        sys.exit(1)

    canonical_content = canonical_file.read_text(encoding="utf-8")
    generated_content = HEADER + canonical_content

    force = "--force" in sys.argv or "-f" in sys.argv
    has_conflicts = False

    for rel_path in TARGETS:
        target_path = repo_root / rel_path

        if target_path.exists():
            existing_content = target_path.read_text(encoding="utf-8")
            if existing_content == generated_content:
                print(f"[OK] {rel_path} is already up to date.")
                continue

            diff = list(difflib.unified_diff(
                existing_content.splitlines(keepends=True),
                generated_content.splitlines(keepends=True),
                fromfile=f"a/{rel_path}",
                tofile=f"b/{rel_path}",
            ))

            print(f"\n[DIFF] Detected differences for {rel_path}:")
            sys.stdout.writelines(diff)

            if not force:
                print(f"[BLOCKED] Refusing to overwrite {rel_path} without --force.\n")
                has_conflicts = True
                continue

        # Target directory creation
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(generated_content, encoding="utf-8")
        print(f"[WRITE] Generated {rel_path}")

    if has_conflicts:
        print("\nSome files had differences and were not updated. Re-run with --force to overwrite.", file=sys.stderr)
        sys.exit(2)

    print("\nPlatform instructions successfully synchronized.")

if __name__ == "__main__":
    main()
