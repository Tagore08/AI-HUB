# Maintenance Routine

**Last reviewed**: 2026-10-03  
**Scope**: Ongoing maintenance triggers, cadence reviews, and hygiene policies for AI-HUB.

---

## 1. Event-Driven Triggers

### ON ADD (New repository, skill, template, or major document)
1. **Inventory**: Confirm directory location and ensure no empty scaffolding was created.
2. **Scan**: If adding a skill or executable code, scan for unauthorized network calls, shell execution risks, or external dependencies.
3. **Classify**: Determine sensitivity domain (PUBLIC reusable framework vs. PRIVATE data/notes).
4. **Map**: Add relevant topic entries to `INDEX/topics-map.md` if the asset represents a new key workflow.
5. **Register**: Add required metadata or documentation entries.
6. **Regenerate Index**: Run `python3 SCRIPTS/index/generate_index.py` and verify all relative links resolve.

### ON UPDATE (Modifying existing assets or instructions)
1. **Detect Change**: Review git diffs before modifying to identify cascading effects.
2. **Check Version**: Verify backward compatibility with existing project templates and rules.
3. **Refresh Map**: Update `INDEX/topics-map.md` if paths, names, or file roles have shifted.
4. **Regenerate Index**: Re-run `python3 SCRIPTS/index/generate_index.py` and `python3 SCRIPTS/context/build_instructions.py` if instructions changed.

### ON REMOVE (Retiring an asset, tool, or template)
1. **Remove Registry Entry**: Delete all references from `INDEX/topics-map.md` and related docs.
2. **Archive Context**: Move deprecated files to the appropriate `archive/` or `ARCHIVED/` directory rather than permanently deleting history.
3. **Regenerate Index**: Run `python3 SCRIPTS/index/generate_index.py` and verify no broken links remain.

---

## 2. Periodic Cadence

### MONTHLY Review
- **Stale & Abandoned Repos**: Review active projects in `PROJECTS/ACTIVE/`. Archive finished or dormant tasks to `PROJECTS/ARCHIVED/`.
- **Duplicate Capabilities**: Check prompts and templates for redundant or overlapping roles.
- **Unused Skills & Scripts**: Identify scripts or skills that are never invoked; trim or consolidate them.
- **Broken Link Sweep**: Run index generation to catch dead links or missing references across markdown docs.
- **Security & Secrets Review**: Run `python3 SCRIPTS/maintenance/check_public_leaks.py` to confirm no credentials or sensitive keywords were committed.

### QUARTERLY Review
- **Architecture Review**: Evaluate directory layout, context footprint size, and prompt token efficiency.
- **Remove Dead Knowledge**: Prune stale notes, superseded specifications, and obsolete guidelines from `KNOWLEDGE/`.
- **Consolidate Instructions**: Merge duplicate instructions between domain rules and `INSTRUCTIONS/CANONICAL.md`.

---

## 3. The Golden Rule of Maintenance
If a file keeps growing and is never read, delete it, archive it, or shrink it into a concise summary.
