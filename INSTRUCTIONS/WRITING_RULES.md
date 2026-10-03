# Writing Rules

**Last reviewed**: 2026-10-03  
**Scope**: Documentation, communication, summaries, and commit messages.

---

## 1. Tone and Structure

- **Density Over Volume**: Prioritize information density over prose length. Prefer structured bullet points, clear tables, and concise summaries over multi-paragraph narratives.
- **Eliminate AI Filler**: Avoid rhetorical introductions, pleasantries, generic conclusions, and boilerplate cheerleading (e.g., "Certainly!", "I hope this helps!", "In today's fast-paced digital world..."). State the facts directly.
- **Hierarchical Clarity**: Use predictable markdown headings (`#`, `##`, `###`) to ensure documents scan easily on both desktop workstations and mobile screens.

---

## 2. Technical Precision

- **Exact References**: Wrap filenames, paths, shell commands, function names, and environment variables in backticks (e.g., `SETUP_LOG.md`, `main`, `find`).
- **LaTeX and Math Notation**: When presenting mathematical expressions, use standard KaTeX syntax (`$...$` for inline, `$$...$$` for display blocks). Escape literal dollar signs as `\$`.
- **Actionable Steps**: Instructions and walkthroughs must provide exact, copy-pasteable commands and complete, unambiguous steps rather than high-level generalizations.

---

## 3. Git Commit Messages

- **Imperative Mood**: Use short, present-tense imperative messages (e.g., `add canonical rules`, `update .gitignore`, `fix link reference`).
- **Atomic Commits**: Keep commit scopes small and coherent. Do not bundle unrelated changes together.
- **Clear Context**: Explain the rationale behind non-obvious modifications within the commit body when necessary.
