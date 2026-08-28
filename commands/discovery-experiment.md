---
description: Map the assumptions behind an idea and design the cheapest test that would actually change your mind, with the threshold set before it runs.
argument-hint: [the idea or solution to test]
---

Invoke the `discovery-experiments` skill for: $ARGUMENTS

Paths written as `references/...`, `assets/...` and `templates/...` below are relative to the `discovery-experiments` skill's own directory.

1. Surface the assumptions across all five categories: desirability, usability, feasibility,
   viability, ethical. Write each as a falsifiable statement, not a topic. Ask "what would
   have to be true for a smart person to think this is a bad idea?"
2. Map them on importance against evidence. Only the high-importance, low-evidence quadrant
   gets tested. Order by kill potential.
3. For the top assumption, choose the cheapest method that would actually move belief, using
   `skills/product-discovery/references/02-method-index.md` and the runbook in
   `references/experiment-library.md`. Apply the cheapness and extravagance tests.
4. Check the preconditions against the user's real evidence state. If traffic is
   insufficient for the design, run
   `skills/discovery-quant/scripts/sample_size.py` and say so rather than planning an
   underpowered test.
5. Produce the test card from `skills/product-discovery/templates/test-card.md` with the success threshold, the
   failure threshold, and the inconclusive band, all derived from the business case and all
   set before any data exists.
6. For a controlled experiment, produce the full pre-registration from
   `skills/product-discovery/templates/experiment-plan.md`.

Never propose a test whose success criterion could be decided afterwards.

Before finalising any deceptive test (fake door, painted door, Wizard of Oz), check the
contraindications on the method card itself, not only the ethics file. **Do not run one at
all** where the concealed output is a clinical, diagnostic, financial, legal or safety
judgement, or on a statutory service. Shadow mode is the substitute. Every fake door needs
an honest close firing on the click and takes no money.
