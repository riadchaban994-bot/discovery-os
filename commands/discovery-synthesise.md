---
description: Turn raw research into coded, traceable findings with confidence levels and a disconfirming-evidence section.
argument-hint: [path to transcripts, tickets, notes, or survey export]
---

Invoke the `discovery-synthesis` skill on: $ARGUMENTS

Paths written as `references/...`, `assets/...` and `templates/...` below are relative to the `discovery-synthesis` skill's own directory.

Run the pipeline in order. Do not skip from raw to themes.

1. Inventory the corpus: source, type, date, participant code, segment, sampling frame.
2. Segment into units of meaning, keeping verbatim text and a locator.
3. Code openly in the participant's language, then build the codebook with inclusion AND
   exclusion rules, and show it to the user for approval before coding at scale.
4. Code the corpus against the approved codebook. Cite the exact span justifying every code.
   Propose new codes; never adopt them silently.
5. Compute saturation per segment with
   `skills/discovery-quant/scripts/qual_saturation.py saturation --csv codes.csv`.
6. Categorise, then theme. Every theme needs at least three independent sources.
7. Count sources, not mentions. No percentages below n=30.
8. Hunt for disconfirming evidence. Run negative case analysis on the strongest theme.
9. Convert to opportunities in customer language, with no product nouns.
10. Run the quality gates in `references/synthesis-quality-gates.md` before delivering.

Output the readout from `skills/product-discovery/templates/research-readout.md`, including the saturation statement
and the disconfirming section. Never write a composite or cleaned-up quote.
