---
name: discovery-prototyping
description: Use when an idea needs to become something people can react to, when choosing prototype fidelity, when building a clickable prototype, fake door page, or Wizard of Oz operator console, when preparing to test a design with users, or when deciding how much to build before testing.
---

# Discovery prototyping

## Core principle

A prototype exists to answer one question. Build only what that question needs, and no more.
The most common prototyping failure is building a beautiful artifact that answers nothing,
because nobody decided what it was for.

Second principle: **fidelity is a choice, not a stage.** Low fidelity is not a step on the
way to high fidelity. It is the right tool when the question is about concept, structure or
flow, and the wrong tool when the question is about comprehension, trust or desirability.

## Choose by the question

| The question | Prototype | Fidelity | Time |
|---|---|---|---|
| Is this concept understood at all? | Sketch, storyboard, or a written description | Paper | Hours |
| Does the structure make sense? | Wireframe or clickable wireframe | Low | Hours |
| Can people complete the task? | Clickable prototype, realistic content | Medium | 1-2 days |
| Do people find it credible and desirable? | High-fidelity visual, real copy, real data | High | 3-5 days |
| Will people take a real step toward it? | Fake door or landing page | Live | 1-2 days |
| Does it work with real data and real edge cases? | Live-data prototype | High | 1 week |
| Is the value real when delivered? | Concierge or Wizard of Oz | Operational | 1-3 weeks |
| Can it be built? | Feasibility prototype, throwaway code | Technical | 1-5 days |

Cagan's four types (*Inspired*): feasibility, user, live-data, and hybrid prototypes. The
list above expands them by question rather than by artifact type.

## The fidelity rules

**Content fidelity matters more than visual fidelity.** Lorem ipsum and placeholder data
make a prototype untestable for comprehension, because half of what a user reacts to is the
words and the numbers. Real content, low visual polish beats the reverse.

**Match fidelity across compared options.** If you are testing two approaches, the polished
one wins on polish. Equal fidelity or the comparison is invalid.

**Low fidelity gets more honest feedback.** People are politer about things that look
finished, and more willing to redesign something that looks provisional.

**Higher fidelity is required for:** trust, credibility, purchase intent, first-impression
comprehension, and anything visual. You cannot test whether people trust a payment flow with
a wireframe.

## What to build, concretely

`references/prototype-build-guide.md` has working patterns you can generate directly:

- Clickable HTML prototype from a described flow, no dependencies, runs from a file
- Fake-door landing page with intent capture and the honest close
- Wizard of Oz operator console: user-facing surface plus an operator view
- Data mock layer so a prototype can use realistic records
- Printable paper prototype sheets

These are real, buildable artifacts. Prototype in the medium the test needs, not in the
medium you have a licence for.

## Testing a prototype

Full protocol in `references/prototype-testing.md`. The essentials:

- Tasks in the user's words, never the interface's labels
- Think-aloud
- Do not rescue until the task is genuinely dead
- Two or three options, counterbalanced, never one alone
- Collect the story before showing anything
- Five participants per round per segment, three rounds, fixing between rounds
- Severity-rate the findings

## The prototype is not the evidence

A well-received prototype demonstrates that people understood it and were polite about it.
It is L2 to L4 depending on how it was tested. Demand evidence requires a commitment step.
Say this plainly whenever a prototype test comes back positive, because a positive prototype
test is the single most over-interpreted result in product discovery.

## Read next

| File | For |
|---|---|
| `references/prototype-types.md` | The full type list, what each proves and cannot prove |
| `references/fidelity-ladder.md` | Choosing fidelity, and the cost of getting it wrong |
| `references/prototype-build-guide.md` | Working patterns to generate |
| `references/prototype-testing.md` | Running the session |

## Red flags

- Building before the question is written down
- Lorem ipsum in a comprehension test
- One option shown alone
- Unequal fidelity across compared options
- A prototype that took longer to build than the decision it informs is worth
- Positive prototype feedback being reported as demand
- A prototype that has quietly become the production codebase
