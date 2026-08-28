# The fidelity ladder

Fidelity has four independent dimensions. Teams treat it as one dial, which is why they
build the wrong thing.

| Dimension | Low | High |
|---|---|---|
| **Visual** | Grey boxes, no styling | Final design, real brand |
| **Content** | Placeholder text and numbers | Real copy, real records |
| **Interaction** | Static images | Fully responsive, real states |
| **Data** | Hard-coded happy path | Live data, edge cases, errors |

**Choose each dimension independently, based on the question.**

| Question | Visual | Content | Interaction | Data |
|---|---|---|---|---|
| Is the concept understood? | Low | High | Low | Low |
| Does the structure work? | Low | High | Medium | Low |
| Can they complete the task? | Medium | High | High | Low |
| Do they trust it? | High | High | Medium | Low |
| Does it survive reality? | Medium | High | High | High |
| Will they take a step toward it? | High | High | Low | Low |

**Content fidelity is high in every row.** That is the point of the table. Real words and
real numbers are almost always required; visual polish rarely is.

---

## The cost of getting it wrong

**Too low.** People cannot react to something they cannot understand. A grey-box prototype
with lorem ipsum tests only whether the participant is willing to imagine, and different
participants imagine different products. The feedback is about their imagination, not your
design.

**Too high.** Three problems, all expensive:
1. Politeness. People will not criticise something that looks finished, and they will not
   suggest that it should be different in kind
2. Sunk cost. The team defends what it spent a week on
3. Anchoring. High fidelity ends divergent thinking. Nobody proposes a different approach to
   something that looks shipped

---

## When to move up the ladder

Move up when the current fidelity has stopped producing new information, not when the
calendar says so.

**Signals to move up:** participants ask what something would look like, the same
misunderstanding recurs and you cannot tell whether it is the concept or the presentation,
you need to test trust or credibility, or you need a commitment step.

**Signals to stay low:** the concept is still changing between sessions, participants are
proposing fundamentally different approaches, or you are still learning about the problem
rather than the solution.

---

## Throwaway versus foundation

Decide before building, and write it down.

**Throwaway** is the default for discovery. Speed over quality, no tests, no
maintainability, deleted after the decision.

**Foundation** only when the prototype is already in production-grade shape and the team has
agreed to maintain it.

**The trap:** a throwaway prototype that quietly becomes the production codebase. This
happens by drift, not by decision, and it is how teams end up maintaining code that was
written in a day to answer a question that was answered months ago. Name the intent at the
start, and put it in the repository README.
