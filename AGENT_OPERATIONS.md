# Agent Operational Procedures & Permissions

**Last reviewed**: 2026-10-03  
**Scope**: Classification of permitted, gated, and strictly forbidden actions for AI agents in AI-HUB.

---

## 1. Safe Read-Only Operations (No Confirmation Needed)

Agents may execute the following read-only inspection tasks autonomously without prior approval:
- **Auditing**: Inspect directory structures, file existence, and permissions.
- **Listing & Searching**: Run file listings (`find`, `ls`), pattern grep searches (`grep`, `rg`), and text view operations.
- **Index Generation**: Run `SCRIPTS/index/generate_index.py` to inspect or test link integrity.
- **Change Detection**: Run `git status`, `git diff`, and `git log` to inspect working state and commit history.
- **Stale Asset Checks**: Scan file modification times and detect unreferenced or obsolete files.

---

## 2. Modifying Operations (Explicit Confirmation Required)

Agents must show a detailed plan first and receive explicit user approval (e.g., `"approved"`) before executing any of the following:
- **Repository Operations**: Adding, updating, or removing repository records or remotes.
- **Context Refresh**: Modifying, regenerating, or updating project context files (`CURRENT_STATE.md`, `GOALS.md`, `TODO.md`).
- **Skill Management**: Adding, scanning, registering, or altering agent skills and tools.
- **Instruction Updates**: Modifying `INSTRUCTIONS/CANONICAL.md`, domain rules, preambles, or platform instruction files.
- **Project Lifecycle**: Creating new project workspaces, moving projects between `ACTIVE/` and `ARCHIVED/`, or creating new scaffolding.
- **Local Git Commits**: Creating local commits (requires explicit approval of changes and commit message).

---

## 3. Strictly Forbidden Operations (Agents Must NEVER Do)

Under no circumstances may an agent perform the following actions:
1. **Never Delete Repositories**: Deleting local or remote repository roots or git directories is prohibited.
2. **Never Overwrite Uncommitted Work**: Silently overwriting unstaged or uncommitted modifications without displaying a diff and receiving explicit permission is forbidden.
3. **Never Install Unverified Skills or Dependencies**: Never run unvetted install scripts, third-party package managers (`pip install`, `npm install`), or download unverified executables.
4. **Never Expose or Commit Secrets**: Never read, generate, output, or commit API keys, tokens, passwords, private keys, or credentials.
5. **Never Alter Public/Private Boundaries**: Never move files across the boundary defined in `PUBLIC_PRIVATE_BOUNDARY.md` or introduce private paths into public files.
6. **Never Replace Source Code with Summaries**: Primary code and source files must never be replaced by descriptive summaries or high-level outlines.
7. **Never Run `git push` or Destructive Git Operations**: Agents must never run `git push`, `git reset --hard`, or any command with force flags (`-f`, `--force`).
