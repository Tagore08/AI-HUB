#!/usr/bin/env python3
"""
check_public_leaks.py
Scans repository files for secret patterns and private terms listed in PRIVATE_TERMS.txt.
Uses only the Python standard library.
Fails loudly (exit code 1) if any forbidden term or credential pattern is detected.
"""

import os
import re
import sys
from pathlib import Path

# Directories and files ignored during leak scanning
IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache"}
IGNORED_FILES = {
    "PRIVATE_TERMS.txt",  # Contains the term definitions themselves
    ".DS_Store",
    "Thumbs.db",
    "desktop.ini",
}

# Regex patterns matching high-entropy credentials and common secret structures
SECRET_PATTERNS = [
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "Cryptographic Private Key Header"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key ID"),
    (r"gh[pousr]_[A-Za-z0-9_]{36,}", "GitHub Personal Access Token"),
    (r"sk-[A-Za-z0-9_-]{20,}", "OpenAI / Cloud Secret Key"),
    (r"xox[baprs]-[0-9A-Za-z-]{10,}", "Slack Token"),
    (r"(?:api[_-]?key|password|secret|bearer)\s*[:=]\s*['\"][A-Za-z0-9_/-]{16,}['\"]", "Hardcoded Secret / Password Assignment"),
]

def load_private_terms(repo_root: Path):
    """Loads private terms from gitignored PRIVATE_TERMS.txt if it exists."""
    terms_file = repo_root / "PRIVATE_TERMS.txt"
    if not terms_file.exists():
        return []

    terms = []
    for line in terms_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            terms.append(line)
    return terms

def scan_file(file_path: Path, repo_root: Path, private_terms):
    """Scans a single file for secret patterns and private terms."""
    rel_path = file_path.relative_to(repo_root).as_posix()
    violations = []

    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        return [(rel_path, 0, f"Could not read file: {e}")]

    lines = content.splitlines()

    # 1. Check for secret patterns
    for pattern_str, label in SECRET_PATTERNS:
        regex = re.compile(pattern_str, re.IGNORECASE)
        for idx, line in enumerate(lines, start=1):
            if regex.search(line):
                violations.append((rel_path, idx, f"Secret Pattern Detected: {label}"))

    # 2. Check for private terms
    for term in private_terms:
        # Match as whole word or phrase, case-insensitive
        term_regex = re.compile(r"\b" + re.escape(term) + r"\b", re.IGNORECASE)
        for idx, line in enumerate(lines, start=1):
            if term_regex.search(line):
                violations.append((rel_path, idx, f"Private Term Detected: '{term}'"))

    return violations

def main():
    repo_root = Path(__file__).resolve().parent.parent.parent
    private_terms = load_private_terms(repo_root)

    print(f"Running Public Repository Leak Check in: {repo_root}")
    if private_terms:
        print(f"Loaded {len(private_terms)} private term(s) from PRIVATE_TERMS.txt")
    else:
        print("Note: PRIVATE_TERMS.txt not found or empty. Checking standard secret patterns.")

    all_violations = []

    for path in sorted(repo_root.rglob("*")):
        if path.is_dir():
            continue
        # Skip ignored directories
        parts = path.relative_to(repo_root).parts
        if any(p in IGNORED_DIRS for p in parts):
            continue
        # Skip ignored files
        if path.name in IGNORED_FILES or path.name.endswith((".tmp", ".bak", ".swp", ".swo")):
            continue

        violations = scan_file(path, repo_root, private_terms)
        all_violations.extend(violations)

    if all_violations:
        print("\n" + "=" * 60)
        print("!!! CRITICAL: LEAK DETECTED IN PUBLIC REPOSITORY !!!")
        print("=" * 60)
        for rel_path, lineno, reason in all_violations:
            print(f"  [FAIL] {rel_path}:{lineno} -> {reason}")
        print("\nAborting: Clean up detected items before staging or committing.")
        sys.exit(1)

    print("\n[PASS] No secret patterns or private terms detected.")
    print("Repository is clean for public commit.")
    sys.exit(0)

if __name__ == "__main__":
    main()
