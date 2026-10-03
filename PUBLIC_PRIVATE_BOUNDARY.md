# Public vs. Private AI-HUB Boundary

**Last reviewed**: 2026-10-03  
**Target context**: PUBLIC

---

## The Boundary

- **PUBLIC (`AI-HUB`)**: Reusable framework only. Contains generic rules, instructions, project templates, universal scripts, and generic documentation. Safe for public distribution and open-source collaboration.
- **PRIVATE (`AI-HUB-PRIVATE`)**: Personal knowledge base, custom prompts, trading strategies and financial material, personal logs, private repositories, and actual task deliverables / outputs.

---

## Fundamental Isolation Rules

1. **One-Way Isolation**: Private content must **NEVER** enter the public repository under any circumstance.
2. **Manual Sync Only**: When framework files (instructions, templates, or helper scripts) are improved in either repository, transfer them between public and private repositories manually by hand. Never automate cross-repo pushes or syncing without inspection.
3. **No Cross-Referencing**: Public files must never hardcode or reference local paths pointing to private workspaces or private repositories.
