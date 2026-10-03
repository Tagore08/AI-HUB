# Analysis Rules

**Last reviewed**: 2026-10-03  
**Scope**: Technical auditing, data evaluation, performance diagnostics, and system assessments.

---

## 1. Rigorous Data Validation

- **Empirical Grounding**: Base all analytical claims on concrete data points, log outputs, benchmark runs, or verified source lines. Avoid speculative assessments without measured evidence.
- **Explicit Assumptions**: When exact metrics are unavailable, state the underlying assumptions explicitly. Label estimates as assumptions, not facts.
- **Edge-Case Sensitivity**: Examine failure boundaries, null inputs, network timeouts, and resource saturation points. Robust analysis accounts for worst-case scenarios, not just typical workflows.

---

## 2. Quantitative & Analytical Discipline

- **Baseline Comparison**: When reporting performance or resource metrics, always provide baseline measurements alongside proposed optimizations.
- **Correlation vs. Causation**: Do not assume that observed symptoms share a single cause without isolating variables. Conduct controlled tests to prove causation.
- **Scope Definition**: Clearly define what is in scope and what is out of scope for the analysis to avoid ambiguous or open-ended interpretations.

---

## 3. Reporting and Recommendation Format

- **Root Cause Identification**: Differentiate between immediate symptoms (e.g., failed process exit) and underlying root causes (e.g., unhandled exception on missing file).
- **Prioritized Recommendations**: Rank findings by severity (Critical, High, Medium, Low) and provide actionable remediation steps for each identified issue.
- **Risk Assessment**: Identify trade-offs, potential regressions, and operational costs associated with each proposed fix.
