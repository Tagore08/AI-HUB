# Platform Instruction Files Guide

**Last reviewed**: 2026-10-03  
**Scope**: Instruction file locations and discovery behaviors across AI coding assistants and CLI tools.

---

## Tool Compatibility Matrix

### 1. Antigravity
- **Primary Instruction Files**: `GEMINI.md`, `AGENTS.md`, or `.agents/rules/*.md`.
- **Read Location**: Scans from the current working directory upwards to the repository root.
- **Global Location**: `~/.gemini/config/`
- **Behavior**: Contextual and hierarchical rules discovery. Progressive disclosure for skills and conditional rules.

### 2. Claude Code
- **Primary Instruction File**: `CLAUDE.md`
- **Read Location**: Repository root (`./CLAUDE.md`) or `.claude/CLAUDE.md`.
- **Local (Private) Location**: `./CLAUDE.local.md` (project-specific, untracked).
- **User-Level Location**: `~/.claude/CLAUDE.md`
- **Behavior**: Concatenates instructions from all matching `CLAUDE.md` files at session start.

### 3. Gemini CLI
- **Primary Instruction File**: `GEMINI.md`
- **Read Location**: Scans from current working directory upward to the repository root (first directory with `.git`).
- **Global Location**: `~/.gemini/GEMINI.md`
- **Behavior**: Hierarchical loading; supports `@file.md` modular imports.

### 4. GitHub Copilot
- **Primary Instruction File**: `copilot-instructions.md`
- **Read Location**: `.github/copilot-instructions.md` at repository root.
- **Path-Specific Location**: `.github/instructions/*.instructions.md` using `applyTo` frontmatter.
- **User-Level Location**: `%USERPROFILE%/copilot-instructions.md` (Windows) or `~/.config/github-copilot/copilot-instructions.md` (Linux/macOS: UNKNOWN if non-standard).
- **Behavior**: Injected into Copilot Chat prompts repository-wide.

### 5. OpenAI Codex CLI
- **Primary Instruction File**: `AGENTS.md`
- **Read Location**: Repository root (`./AGENTS.md`) and subdirectories (nested `AGENTS.md` files override higher-level guidance).
- **Global Location**: `~/.codex/AGENTS.md` (or `AGENTS.override.md`).
- **Configurable Fallbacks**: Can specify alternative filenames in `.codex/config.toml` via `project_doc_fallback_filenames` or `model_instructions_file`.
- **AI-HUB Strategy**: Root `AGENTS.md` remains hand-written and concise for Codex and human overview, while generated files (`CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`) synchronize directly from `INSTRUCTIONS/CANONICAL.md`.

---

## Generation & Synchronization

Run `python3 SCRIPTS/context/build_instructions.py` from repository root to synchronize platform files directly from `INSTRUCTIONS/CANONICAL.md`.
