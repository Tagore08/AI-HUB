# Agent Rules

**Last reviewed**: 2026-10-03  
**Scope**: Autonomous agent behaviors, multi-agent coordination, subagents, and automated workflows.

---

## 1. Boundary & Permission Enforcement

- **Strict Path Confinement**: Agents must remain strictly within the root working directory defined for the active session. Attempting to access, traverse (`../`), or read files outside the designated workspace is strictly prohibited.
- **Safety Checks**: Destructive operations (file deletions, mass overwrites, git resets, terminal state changes) require explicit confirmation before execution.
- **Secrets Protection**: Agents must never read, write, parse, echo, or store passwords, API keys, private tokens, or SSH keys.

---

## 2. Multi-Agent & Subagent Coordination

- **Focused Delegations**: When delegating work to subagents, assign clear, tightly scoped tasks with well-defined inputs and expected outputs. Avoid broad or ambiguous mandates.
- **Context Economy**: Pass only the necessary files and directives to subagents. Do not flood subagents with entire repository transcripts or unrelated files.
- **State Synchronization**: All findings, code modifications, and architectural decisions made by subagents must be reviewed, synthesized, and recorded back into the main session logs.

---

## 3. Session Persistence & Handoffs

- **Record as You Go**: Log state milestones in `CURRENT_STATE.md` and operational events in `SETUP_LOG.md`. Do not defer logging until the end of a long task.
- **Clean Handoff Formatting**: When preparing a session handoff, summarize:
  1. What was completed (`DONE SO FAR`)
  2. The immediate next action required (`NEXT STEP`)
  3. Critical context and blockers (`HANDOFF NOTES`)
