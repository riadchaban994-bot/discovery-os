---
description: Grade every claim in a PRD, roadmap, business case, or research readout against its evidence, and list the cheapest ways to close the gaps.
argument-hint: [file path or pasted document]
---

Invoke the `product-discovery` skill and work in AUDIT mode on: $ARGUMENTS

Paths written as `references/...`, `assets/...` and `templates/...` below are relative to the `product-discovery` skill's own directory.

Read `references/03-evidence-ledger.md` and follow the AUDIT protocol:

1. Extract every claim: any sentence asserting something about customers, market,
   competitors, costs, behaviour, or causes. Ignore intentions and plans.
2. Grade each: evidence level L0-L7, confidence, source.
3. Identify the load-bearing claims, the ones that break the recommendation if false.
   Usually three to five. Check those hardest.
4. Flag causal language on non-experimental results.
5. Flag sample crimes: percentages below n=30, subgroup claims below 30, "users" from fewer
   than five sources, missing denominators.
6. Flag survivors: numbers with no source, quotes with no participant code, benchmarks with
   no citation, the word "validated".
7. Report as the audit table from the skill, then the three actions that would most raise
   the document's overall confidence.

Be neutral and specific. The audit is about the document, never about its author. Name the
issue and the fix, not the failing.
