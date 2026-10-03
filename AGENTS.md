# AI-HUB Agents Guide

**Last reviewed**: 2026-10-03  
**Authority**: `INSTRUCTIONS/CANONICAL.md` is the single source of truth.

Welcome to AI-HUB. This map guides AI agents to the correct context.

---

## Directory Map

- **`INSTRUCTIONS/`**: Core behavior rules.
  - `CANONICAL.md`: Master rules and context priorities.
  - `PERMISSIONS.md`: Allowed vs. forbidden actions.
  - `CODING_RULES.md`, `RESEARCH_RULES.md`, `WRITING_RULES.md`, `ANALYSIS_RULES.md`, `AGENT_RULES.md`: Domain-specific standards.
  - `PORTABLE_PREAMBLE.md`: Session bootstrap for chat apps.
- **`PROJECTS/`**: Isolated project workspaces.
  - `TEMPLATES/PROJECT_TEMPLATE/`: Starter scaffolding.
  - `ACTIVE/`: Currently active projects.
  - `ARCHIVED/`: Completed or deprecated projects.
- **`PROMPTS/`**: Reusable task and role templates (`STANDARD_TASK_CONTEXT.md`, `ROLES.md`).
- **`KNOWLEDGE/`**: Reusable reference material and cross-project documentation.
- **`INDEX/`**: Catalogs and keyword lookup maps.
- **`SCRIPTS/`**: Deterministic helper utilities (standard library only).
- **`OUTPUTS/`**: Final deliverables and generated reports.

---

## Agent Navigation Order

1. Read `INSTRUCTIONS/CANONICAL.md` for foundational rules.
2. Read the active project folder named in the user request (e.g., `PROJECTS/ACTIVE/<project>/AGENTS.md`).
3. If no project is named, read only the specific files directly cited by the user.
4. Mark unverified claims as `UNKNOWN`. Never invent paths or facts.
5. Log progress in the project's `CURRENT_STATE.md` and session actions in `SETUP_LOG.md`.
