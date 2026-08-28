---
description: Diagnose a product discovery question and route it to the right method for the evidence you actually have.
argument-hint: [the question, decision, or situation]
---

Invoke the `product-discovery` skill and work in ASSESS mode on: $ARGUMENTS

Paths written as `references/...`, `assets/...` and `templates/...` below are relative to the `product-discovery` skill's own directory.

Follow the skill exactly:

1. Identify the real question behind what was asked. If the user's framing and the real
   question differ, say so once, then route on the real one.
2. Fill the Minimum Viable Intake. Infer what you can from what the user wrote, state your
   inferences as a draft they can correct, and ask at most three questions about the slots
   that are both missing and load-bearing. If the Decision slot cannot be filled, fill it
   first before anything else.
3. Read `references/01-intake-and-routing.md` and route on the evidence inventory, not on
   preference. Apply the evidence overrides.
4. Produce the output contract from the skill, in order: what is being decided, what we know
   and how well, the biggest unknown, the recommended method with why it beats the
   alternatives here, what it will not tell you, cost, open assumptions, next action.

Give one recommendation, not a menu. Mark every inference as an assumption. Do not invent
any number, quote, or customer.
