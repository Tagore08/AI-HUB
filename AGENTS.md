# AI-HUB Agents Guide
Last reviewed: 2026-10-02

**AI-HUB** is a structured environment designed to provide AI agents with consistent rules, context, and project history to produce reliable work.

## Directory Map
- **INSTRUCTIONS/**: Core rules (`MASTER_RULES.md`) and boundaries (`PERMISSIONS.md`).
- **KNOWLEDGE/**: Reusable facts, tutorials, and general information.
- **PROJECTS/**: Isolated workspaces for distinct goals.
- **PROMPTS/**: Standardized formats for tasks and roles.

## How to Pick Relevant Context
Read only what you need. Start with the user's prompt, review `MASTER_RULES.md`, then consult the specific project folder named in the prompt. Ignore unrelated projects or deep knowledge files unless explicitly requested.

## Context Hierarchy
Source files outrank summaries. If a summary contradicts the actual code or data, trust the source file.

## Recording Decisions
Always record important choices, architectures, or pivots in the project's `DECISIONS.md` file.

## Handling Uncertainty
If information is missing, ambiguous, or unverifiable, mark it clearly as **UNKNOWN**. Do not invent facts or guess user intent without asking for clarification first.
