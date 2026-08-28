# Assumption mapping

Source: David Bland's assumption mapping, as used in *Testing Business Ideas* (Bland and
Osterwalder, 2019). Categories follow Cagan's four risks plus Torres's ethical risk.

---

## Surfacing assumptions

Work through the solution and ask, for each category, "what must be true?"

**Desirability / value**
- Customers have this problem, often enough to matter
- They are aware they have it, or will recognise it when shown
- They are dissatisfied enough with the current solution to change
- They will change behaviour, not just express interest
- The value is legible before they commit
- Our segment is reachable

**Usability**
- They can find it
- They understand what it does without training
- They can complete the core task unaided
- It fits the context of use: device, environment, interruptions, time pressure
- It works for people with different abilities and different languages

**Feasibility**
- We can build it with the team and time we have
- Required data exists, at the quality and freshness needed
- Third-party dependencies behave as documented, at our volume
- Performance holds at the required percentile
- We can operate and support it

**Viability**
- Unit economics work at realistic volume
- We can reach the segment at a viable acquisition cost
- Price is acceptable and collectable in this market
- It does not cannibalise something more valuable
- Legal, regulatory and licensing permit it, here
- Support load is bearable
- Partners and channel will cooperate

**Ethical**
- Nobody is harmed by it working as intended
- Nobody is harmed by it failing, without recourse
- We would defend it if reported accurately in public
- The data it creates is proportionate and protected
- It does not exclude people who need it
- The worst-behaved user cannot weaponise it

**Prompt that surfaces the ones people hide:** "What would have to be true for a smart
person to think this is a bad idea?"

---

## Writing an assumption properly

| Not an assumption | Assumption |
|---|---|
| Pricing | Merchants will pay 5% of order value |
| Technical risk | The delivery partner API returns a quote in under 800ms at p95 |
| Onboarding | A new merchant can complete setup unaided in under 10 minutes |
| Market size | At least 3,000 merchants in this city fulfil 20+ orders a week |
| Adoption | At least 30% of merchants who see the offer will try it once |

**Test:** could a result prove it false? If not, rewrite it.

---

## Mapping

**Importance axis.** If this is false, does the solution collapse, or does it just get
harder? Only collapse is high importance.

**Evidence axis.** What do we already have, and at what level on the evidence ladder? L0-L1
is low evidence. L4+ from a relevant sample is high.

**The quadrants:**

| Quadrant | Action |
|---|---|
| High importance, low evidence | **Test now.** This is the queue |
| High importance, high evidence | Monitor. Note what would change it, and when to recheck |
| Low importance, low evidence | Leave. Revisit only if importance rises |
| Low importance, high evidence | Ignore |

**Do this as a group, silently first.** Individual placement before discussion prevents the
most senior voice anchoring the map. Where people disagree strongly on importance, that
disagreement is itself a finding and usually points at an unstated difference in strategy.

---

## Ordering the test queue

Within the top-right quadrant, order by:

1. **Freeze date.** Which assumptions stop being changeable, and when? Anything that
   becomes irreversible at a tooling, BOM, licence or public-commitment freeze gets tested
   before that date, whatever it costs, because after it the answer is unusable
2. **Kill potential.** Which assumption, if false, ends the project? Test that first. A
   cheap test that can kill the project is worth more than an expensive one that refines it
3. **Cost of being wrong later.** How much will be spent before this surfaces on its own?
4. **Test cost.** Cheapest first among assumptions of similar importance
5. **Dependency.** Some assumptions only matter if another holds. Sequence them

**The common failure:** testing usability before value. Usability testing is comfortable,
concrete and well tooled. It also tells you nothing about whether anyone wants the thing.
If value is unevidenced, test value first, even though it is harder.

---

## Output

```
| # | Assumption | Category | Importance | Evidence | Freezes on | Test | Threshold | Owner | Status |
|---|-----------|----------|------------|----------|------------|------|-----------|-------|--------|
| 1 | Merchants pay 5% of order value | Viability | Collapse | L0 | Pre-sale to 20 | 5 of 20 | | queued |
| 2 | Partner API p95 under 800ms | Feasibility | Collapse | L1 | Spike, 2 days | p95<800ms | | running |
| 3 | Setup under 10 min unaided | Usability | Harder | L0 | 5 usability sessions | 4 of 5 | | queued |
```

Review it weekly. Assumptions that have been tested move out; new ones surface as the
solution takes shape.
