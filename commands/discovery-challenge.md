---
description: Red-team a discovery plan, a research conclusion, or a decision, ranked by how much each finding would change the answer.
argument-hint: [the plan, conclusion, or decision to challenge]
---

Invoke the `product-discovery` skill and work in CHALLENGE mode on: $ARGUMENTS

Paths written as `references/...`, `assets/...` and `templates/...` below are relative to the `product-discovery` skill's own directory.

Follow the protocol in `references/05-anti-patterns.md`, in order:

1. Decision test: what decision does this change, and what result would flip it?
2. Evidence test: for each load-bearing claim, level, source, sample, date.
3. Alternative-explanation test: the two strongest competing explanations for every causal
   or directional claim.
4. Absent-evidence test: who is not in this sample, and what data was available and unused?
5. Inversion test: if the conclusion is wrong, what would the world look like, and is any of
   that already visible?
6. Method-fit test: can the method used actually answer the question asked?
7. Stopping test: was the analysis stopped at a convenient point?
8. Incentive test: who benefits from this conclusion?

Report in three sections: what would change the answer (ranked, each with the cheapest way
to resolve it), what is worth fixing but would not change the answer, and what holds up.

Always fill the "holds up" section. A challenge that lists only problems is not calibrated
and will be discounted wholesale.
