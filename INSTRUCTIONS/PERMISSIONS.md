# AI Permissions
Last reviewed: 2026-10-02

## What AI Agents May Do
- May read anything inside the AI-HUB folder.
- May create or edit files only inside AI-HUB, and specifically only in the project or folder named in the current task.

## What AI Agents Must Ask Before Doing
- Deleting or moving files.
- Editing more than 5 files at once.
- Installing any software.
- Running any terminal command that changes the system state.

## What AI Agents Must NEVER Do
- Run `git push` or force-push.
- Touch, read, or modify files outside the AI-HUB directory.
- Read or write secrets, passwords, or tokens.
- Send content marked LOCAL-ONLY to any online service.

## Logging
- Must log meaningful changes and milestones in the relevant project's `CURRENT_STATE.md`.
