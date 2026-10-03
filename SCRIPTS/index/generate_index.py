#!/usr/bin/env python3
"""
generate_index.py
Scans the AI-HUB repository and generates structured indexes in INDEX/.
Uses only the Python standard library.
"""

import os
import re
import sys
from pathlib import Path

HEADER = "<!-- AUTO-GENERATED: DO NOT EDIT -->\n\n"

IGNORED_DIRS = {".git", "__pycache__", ".pytest_cache", ".ruff_cache"}
IGNORED_FILES = {".DS_Store", "Thumbs.db", "desktop.ini"}

def get_rel_link(target: Path, from_dir: Path) -> str:
    """Computes a relative markdown link path from from_dir to target."""
    try:
        rel = os.path.relpath(target, from_dir)
        return str(Path(rel).as_posix())
    except ValueError:
        return str(target.as_posix())

def scan_files(root: Path):
    """Scans all non-ignored, existing files in root."""
    found = []
    for path in sorted(root.rglob("*")):
        if path.is_dir():
            continue
        # Skip if any parent is in IGNORED_DIRS
        parts = path.relative_to(root).parts
        if any(p in IGNORED_DIRS for p in parts):
            continue
        if path.name in IGNORED_FILES or path.name.endswith((".tmp", ".bak", ".swp", ".swo")):
            continue
        found.append(path)
    return found

def generate_sub_index(title: str, folder_name: str, repo_root: Path, index_dir: Path, output_filename: str):
    """Generates a dedicated sub-index (e.g. KNOWLEDGE.md, PROJECTS.md, PROMPTS.md)."""
    target_dir = repo_root / folder_name
    if not target_dir.exists():
        return False

    files = [f for f in scan_files(target_dir)]
    if not files:
        return False

    lines = [
        HEADER,
        f"# {title} Index\n\n",
        f"**Directory**: `{folder_name}/`  \n\n",
        "---\n\n",
    ]

    current_subdir = None
    for f in sorted(files, key=lambda p: str(p.relative_to(target_dir))):
        rel_to_target = f.relative_to(target_dir)
        parent_dir = rel_to_target.parent.as_posix()

        if parent_dir != "." and parent_dir != current_subdir:
            current_subdir = parent_dir
            lines.append(f"\n### {current_subdir}/\n\n")
        elif parent_dir == "." and current_subdir is not None:
            current_subdir = None

        link = get_rel_link(f, index_dir)
        lines.append(f"- [{rel_to_target.as_posix()}]({link})\n")

    out_file = index_dir / output_filename
    out_file.write_text("".join(lines), encoding="utf-8")
    print(f"[OK] Generated {out_file.name}")
    return True

def generate_topics(repo_root: Path, index_dir: Path):
    """Generates TOPICS.md from topics-map.yaml or topics-map.md, resolving and verifying links."""
    map_file = None
    for candidate in ["topics-map.md", "topics-map.yaml"]:
        p = index_dir / candidate
        if p.exists():
            map_file = p
            break

    if not map_file:
        return []

    content = map_file.read_text(encoding="utf-8")
    broken_links = []

    # Regex to find markdown links: [text](path)
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def check_link(match):
        label = match.group(1)
        rel_target = match.group(2)
        if rel_target.startswith(("http://", "https://", "#")):
            return match.group(0)

        # Target relative to index_dir
        resolved = (index_dir / rel_target).resolve()
        if not resolved.exists():
            broken_links.append((rel_target, f"Topic map link broken: {rel_target}"))
            return f"[{label}]({rel_target}) *(MISSING)*"
        return match.group(0)

    processed_content = link_pattern.sub(check_link, content)

    lines = [
        HEADER,
        "# Topic Map\n\n",
        "Curated index mapped by task domain and workflow.\n\n",
        "---\n\n",
        processed_content,
    ]

    out_file = index_dir / "TOPICS.md"
    out_file.write_text("".join(lines), encoding="utf-8")
    print(f"[OK] Generated TOPICS.md (source: {map_file.name})")
    return broken_links

def generate_main_index(repo_root: Path, index_dir: Path):
    """Generates main INDEX/INDEX.md organized by topic."""
    all_files = scan_files(repo_root)

    # Classify files into defined topic buckets
    topics = {
        "Start Here & Overview": [],
        "Instructions & Rules": [],
        "Prompts & Roles": [],
        "Project Templates & Projects": [],
        "Knowledge Base": [],
        "Platform & Tool Integrations": [],
        "Automation Scripts": [],
        "Index & Catalogs": [],
        "Other Files": [],
    }

    for f in all_files:
        rel = f.relative_to(repo_root).as_posix()

        if rel in ["START_HERE.md", "README.md", "PUBLIC_PRIVATE_BOUNDARY.md", "SECRETS_POLICY.md", "MAINTENANCE.md", "AUDIT_REPORT.md"]:
            topics["Start Here & Overview"].append(f)
        elif rel.startswith("INSTRUCTIONS/"):
            topics["Instructions & Rules"].append(f)
        elif rel.startswith("PROMPTS/"):
            topics["Prompts & Roles"].append(f)
        elif rel.startswith("PROJECTS/"):
            topics["Project Templates & Projects"].append(f)
        elif rel.startswith("KNOWLEDGE/"):
            topics["Knowledge Base"].append(f)
        elif rel.startswith("PLATFORM_INSTRUCTIONS/") or rel in ["CLAUDE.md", "GEMINI.md", ".github/copilot-instructions.md"]:
            topics["Platform & Tool Integrations"].append(f)
        elif rel.startswith("SCRIPTS/"):
            topics["Automation Scripts"].append(f)
        elif rel.startswith("INDEX/"):
            # Exclude INDEX.md itself from its listing to avoid circular clutter
            if rel != "INDEX/INDEX.md":
                topics["Index & Catalogs"].append(f)
        else:
            topics["Other Files"].append(f)

    lines = [
        HEADER,
        "# AI-HUB Master Index\n\n",
        "High-level index organized by topic. Optimized for mobile and desktop.\n\n",
        "---\n\n",
    ]

    for topic_name, files in topics.items():
        if not files:
            continue
        lines.append(f"## {topic_name}\n\n")
        for f in sorted(files, key=lambda p: p.relative_to(repo_root).as_posix()):
            rel_display = f.relative_to(repo_root).as_posix()
            link = get_rel_link(f, index_dir)
            lines.append(f"- [{rel_display}]({link})\n")
        lines.append("\n")

    out_file = index_dir / "INDEX.md"
    out_file.write_text("".join(lines), encoding="utf-8")
    print(f"[OK] Generated INDEX.md")

def check_all_links_in_index(index_dir: Path):
    """Verifies that all relative markdown links inside generated index files exist."""
    broken = []
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    for md_file in sorted(index_dir.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        for match in link_pattern.finditer(content):
            target = match.group(2)
            if target.startswith(("http://", "https://", "#")):
                continue
            resolved = (index_dir / target).resolve()
            if not resolved.exists():
                broken.append((md_file.name, target))
    return broken

def main():
    repo_root = Path(__file__).resolve().parent.parent.parent
    index_dir = repo_root / "INDEX"
    index_dir.mkdir(parents=True, exist_ok=True)

    print("Scanning repository and generating indexes...")

    # 1. Main topic-based index
    generate_main_index(repo_root, index_dir)

    # 2. Section sub-indexes
    generate_sub_index("Knowledge", "KNOWLEDGE", repo_root, index_dir, "KNOWLEDGE.md")
    generate_sub_index("Projects", "PROJECTS", repo_root, index_dir, "PROJECTS.md")
    generate_sub_index("Prompts", "PROMPTS", repo_root, index_dir, "PROMPTS.md")

    # Conditional sub-indexes
    generate_sub_index("Repositories", "REPOS", repo_root, index_dir, "REPOSITORIES.md")
    generate_sub_index("Skills", "SKILLS", repo_root, index_dir, "SKILLS.md")

    # 3. Topic map
    topic_broken = generate_topics(repo_root, index_dir)

    # 4. Check all generated links
    all_broken = check_all_links_in_index(index_dir)

    if all_broken:
        print("\n[WARNING] Broken links detected in index files:")
        for source_file, broken_link in all_broken:
            print(f"  - In {source_file}: {broken_link}")
    else:
        print("\n[VERIFIED] All generated index links resolve successfully to real files.")

if __name__ == "__main__":
    main()
