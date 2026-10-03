# START HERE

**Last reviewed**: 2026-10-03  
**Context**: AI-HUB Personal Context Framework

---

## 📱 Quick Navigation

- **Rules**: `INSTRUCTIONS/CANONICAL.md`
- **Agent Map**: `AGENTS.md`
- **Agent Operations**: `AGENT_OPERATIONS.md`
- **Task Template**: `PROMPTS/STANDARD_TASK_CONTEXT.md`
- **Projects**: `PROJECTS/ACTIVE/`
- **Templates**: `PROJECTS/TEMPLATES/PROJECT_TEMPLATE/`
- **Index**: `INDEX/`
- **Knowledge**: `KNOWLEDGE/`
- **Outputs**: `OUTPUTS/`
- **Boundaries**: `PUBLIC_PRIVATE_BOUNDARY.md`

---

## 🚀 Starting a Project

1. Copy `PROJECTS/TEMPLATES/PROJECT_TEMPLATE/` into `PROJECTS/ACTIVE/<project-name>`.
2. For tiny projects, fill in only:
   - `README.md`
   - `GOALS.md`
   - `CURRENT_STATE.md`
   - `TODO.md`
3. Expand to `ARCHITECTURE.md`, `PLAN.md`, and `REQUIREMENTS.md` only as complexity increases.

---

## 💬 Using with Any Chat App

1. Copy `INSTRUCTIONS/PORTABLE_PREAMBLE.md` into your custom instructions or prompt start.
2. For each new task, fill out `PROMPTS/STANDARD_TASK_CONTEXT.md` and paste it into chat.
3. When hitting usage limits, fill in the **Handoff Section** (`DONE SO FAR`, `NEXT STEP`, `HANDOFF NOTES`) and paste into a new chat session.

---

## 🤖 Using with Coding Agents

1. Point your coding agent to this directory as its root workspace.
2. Coding agents must obey `INSTRUCTIONS/CANONICAL.md`, `INSTRUCTIONS/PERMISSIONS.md`, and `INSTRUCTIONS/CODING_RULES.md`.
3. Consult `AGENT_OPERATIONS.md` for explicit permissions regarding read-only vs. modifying actions.

---

## 🔒 Pre-Commit Leak Check

Before making any public commit, run the leak scanner:
```bash
python3 SCRIPTS/maintenance/check_public_leaks.py
```
This scans all tracked and prospective files for secret patterns and any sensitive keywords listed in your local, gitignored `PRIVATE_TERMS.txt`.

---

## ☁️ Google Drive & Cloud Sync

> **Important Drive Rule**:  
> Google Drive holds **ONLY**:
> - `INSTRUCTIONS/`
> - `KNOWLEDGE/`
> - `PROJECTS/`
> - `PROMPTS/`
> - `OUTPUTS/`
> - `INDEX/`
>
> **NEVER** sync:
> - Git repositories (`.git/`)
> - `node_modules/`
> - Build or binary output folders (`target/`, `dist/`, `build/`, `__pycache__/`)

---

## 🛠️ Maintenance

Refer to `MAINTENANCE.md` for event-driven triggers (`ON ADD`, `ON UPDATE`, `ON REMOVE`), monthly reviews, and quarterly architecture consolidation.
