# Opportunity solution tree

Teresa Torres's structure, built and maintained properly. *Continuous Discovery Habits*
(2021).

```
                        OUTCOME
                           |
        +------------------+------------------+
        |                  |                  |
   OPPORTUNITY        OPPORTUNITY        OPPORTUNITY
        |                  |
   +----+----+        +----+----+
   |         |        |         |
SOLUTION  SOLUTION  SOLUTION  SOLUTION
   |
+--+--+
|     |
TEST TEST
```

---

## The outcome

One outcome per tree. It is a change in customer behaviour or a business result, never an
output.

| Not an outcome | Outcome |
|---|---|
| Ship the mobile app | Merchants complete a sale away from the counter |
| Improve onboarding | New merchants reach their first completed order within 48 hours |
| Increase engagement | Weekly active merchants who log at least one order rise from X to Y |

**Test:** could you achieve it without building anything? If yes, it is an outcome. If the
only way to achieve it is to ship the named thing, it is an output wearing a metric.

**Product outcomes versus business outcomes.** "Revenue up 20 percent" is a business
outcome a product team cannot act on directly. Find the customer behaviour that drives it
and set that as the tree's root. The business outcome stays visible above the tree.

---

## Opportunities

An opportunity is an unmet need, a pain, or a desire, expressed in the customer's language
and tied to a moment.

**Rules:**
- Customer language, from the corpus, not from the product
- Contains no product noun, no feature name, no technology
- Tied to a situation: when, during what
- Cites at least one source
- Sits at one level of abstraction with its siblings
- Belongs to exactly one parent. If it fits under two, the tree structure is wrong

**Structuring the layer.** Big opportunities decompose into smaller ones. Two or three
levels is normal. The bottom level should be specific enough that a solution could
plausibly address it, and the top level broad enough to matter to the outcome.

| Rejected | Rewritten |
|---|---|
| Needs better reporting | Cannot tell which items made money this week without exporting to a spreadsheet |
| Wants an app | Has to go back to the counter to check stock while serving a customer |
| Poor onboarding experience | Set the account up, could not work out how to add the first product, and left it for three weeks |
| Needs AI recommendations | Scrolls for ten minutes at closing time and orders the same thing as last week |

**The sizing question, per Torres:** opportunity size (how many, how often, how much it
costs them), market factors, company factors, customer factors. Compare opportunities
against each other rather than scoring them in isolation; comparative judgement is more
reliable than absolute scoring.

---

## Solutions

Solutions sit under exactly one opportunity. If a solution addresses three opportunities,
either it is a platform bet that belongs in strategy, or the opportunities are actually
one.

**Generate at least three per opportunity before choosing.** The first idea is the one you
already had, and testing it alone will produce a warm reception. Comparison is what
produces information.

---

## Assumption tests

Below each solution being pursued, the assumptions that must hold, and the test for each.
Categories: desirability, viability, feasibility, usability, ethical.

See `discovery-experiments` for mapping and designing them.

---

## Keeping it alive

- Update after every interview, not after every quarter
- New opportunities get added with their source; opportunities without sources get removed
- When an opportunity is chosen, mark it, and record why the others were not
- When a solution fails a test, keep it on the tree marked as tested and failed with the
  date. This is what stops it being re-proposed in six months
- The tree is a working artifact for the trio, not a stakeholder deliverable. Do not
  prettify it for presentation; make a summary instead

---

## Common failures

| Failure | Symptom | Fix |
|---|---|---|
| Solutions in the opportunity layer | Product nouns in the opportunity text | Rewrite as the need underneath |
| Multiple outcomes | The tree has two roots or the root has an "and" | Split into two trees |
| Opportunities from a workshop | No source citations | Go and get the sources, or delete them |
| Built once, never updated | Last edit was three months ago | Fold it into the weekly cadence |
| Every opportunity has one solution | The tree is a roadmap | Generate two more per opportunity |
| Tree used to justify a pre-existing plan | Every branch leads to the thing already being built | Say this out loud. It is the most common failure and the least often named |
