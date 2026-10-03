# Coding Rules

**Last reviewed**: 2026-10-03  
**Scope**: Code generation, refactoring, and scripting in AI-HUB.

---

## 1. Dependency & Runtime Constraints

- **Standard Library First**: For scripts and utilities, use exclusively the Python standard library (`sys`, `os`, `pathlib`, `json`, `argparse`, `subprocess`, `hashlib`) or standard shell (`bash` / POSIX `sh`).
- **No Unsolicited Dependencies**: Never introduce external packages (`pip install`, `npm install`, etc.) unless the user explicitly mandates them in the project requirements.
- **Python Versioning**: Write clean, modern, backward-compatible Python (compatible with Python 3.10+). Avoid deprecated syntax and experimental language features.
- **Shell Scripts**: Ensure all bash scripts include `set -euo pipefail`. Use quoting around variables (`"$VAR"`) to handle whitespace safely. Avoid destructive commands without explicit error checking.

---

## 2. Code Quality & Modularity

- **Preserve Existing Patterns**: Adopt the existing code formatting, naming conventions, and file layout of the target project. Do not reformat unrelated files.
- **Deterministic Logic**: Favor pure functions and deterministic algorithms. Avoid hidden state, uncontrolled side effects, and non-deterministic sorting or file traversal.
- **Fail Fast & Explicit Errors**: Validate preconditions early. Raise meaningful exceptions or informative stderr messages rather than returning silent nulls or empty fallback data.
- **Defensive Resource Management**: Always use context managers (`with open(...) as f:`) when handling file handles, sockets, or subprocess streams.

---

## 3. Modification & Refactoring Discipline

- **Single Purpose Edits**: Keep modifications focused on the immediate task. Do not mix stylistic refactoring with functional bug fixes.
- **Preserve Documentation**: Preserve existing comments, type hints, docstrings, and license headers unless explicitly directed to update them.
- **No Ghost Imports**: Never import modules, classes, or packages that are not verified to exist in the environment or codebase. Verify with imports or tests before completing work.

---

## 4. Testing & Verification

- **Automated Verification**: Before declaring work complete, run automated checks (syntax check via `python3 -m py_compile`, unit tests, or test command).
- **Graceful Failure**: If a test or build fails, inspect the error output carefully, isolate the root cause, and correct it without suppressive hacks (e.g., bare `except: pass`).
