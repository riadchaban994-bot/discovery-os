# Prototype types

Each entry: what it proves, what it cannot prove, and what it costs.

---

## Paper sketch / storyboard
**Proves:** whether the concept is understood, whether the sequence makes sense to someone
who did not design it.
**Cannot prove:** usability, desirability, trust, anything visual.
**Cost:** an hour. **Fidelity:** none. **Evidence:** L2.
**Best for:** the very first reaction, and for concepts that involve a sequence of events
over time rather than a screen.

## Wireframe (static)
**Proves:** information hierarchy, whether the right things are on the right screen.
**Cannot prove:** whether people can complete a task, since nothing responds.
**Cost:** hours. **Evidence:** L2.

## Clickable prototype
**Proves:** task completion, navigation, where people get lost.
**Cannot prove:** behaviour with real data, edge cases, performance, whether they want it.
**Cost:** one to two days. **Evidence:** L4 for usability, L2 for value.
**Requirement:** realistic content. A clickable prototype full of placeholder text tests
nothing about comprehension.

## High-fidelity visual prototype
**Proves:** first impression, credibility, comprehension of the value, visual hierarchy.
**Cannot prove:** long-term use, real-data behaviour, willingness to pay.
**Cost:** three to five days. **Evidence:** L2 to L4.
**Warning:** the closer it looks to finished, the more polite the feedback becomes.

## Live-data prototype
**Proves:** whether the concept survives real records: long names, missing fields, edge
cases, volume, the messy 5 percent.
**Cannot prove:** demand.
**Cost:** about a week. **Evidence:** L4.
**Underused.** Most concepts that look good on designed data fall apart on real data, and
this is where you find out cheaply. (Cagan's live-data prototype.)

## Feasibility prototype
**Proves:** the risky technical part can be built at acceptable performance.
**Cannot prove:** anything about users.
**Cost:** one to five days, engineer-owned, throwaway code.
**Rule:** it is thrown away. A feasibility prototype that becomes production code is how
teams inherit the worst codebase they will ever maintain.

## Fake door / painted door
**Proves:** whether people will take a real step toward it.
**Cannot prove:** satisfaction after use, retention, whether the thing would actually work.
**Cost:** one to two days. **Evidence:** L5.
**Requires:** live traffic and an honest close.

## Landing page + paid traffic
**Proves:** whether a proposition attracts a defined audience, and the relative strength of
competing propositions.
**Cannot prove:** anything absolute. Read only as a comparison.
**Cost:** three to five days plus media spend. **Evidence:** L5.

## Concierge
**Proves:** whether the outcome is valuable when delivered, and what the real workflow is.
**Cannot prove:** whether it scales, or whether an automated version delivers the same value.
**Cost:** two to six weeks. **Evidence:** L6 if they pay and return.

## Wizard of Oz
**Proves:** behaviour with a working product before the product works.
**Cannot prove:** anything that depends on the automation's real quality or latency.
**Cost:** one to three weeks. **Evidence:** L5 to L6.
**Do not run** where the concealed output is a clinical, diagnostic, financial, legal or
safety judgement, or on a statutory service. A human silently generating recommendations a
professional believes came from a checked system is a safety hazard and very likely a
regulated-device or professional-practice violation. Use shadow mode instead: the new logic
runs and is logged but is never shown.
**Especially good for AI features:** it tells you what accuracy the experience actually
needs, which is nearly always lower than the team assumed, and sometimes much higher.

## Video prototype
**Proves:** whether the story of the product lands, at scale, cheaply.
**Cannot prove:** usability.
**Cost:** two to five days. **Evidence:** L2, or L5 if paired with an intent capture.

## Data mock / API stub
**Proves:** integration shape, contract feasibility, what the front end actually needs.
**Cost:** one to two days.

## Operational prototype (pilot)
**Proves:** whether the whole service works end to end, including support, billing and the
humans in the loop.
**Cannot prove:** scale economics.
**Cost:** weeks. **Evidence:** L6.
**Essential for:** service, marketplace, logistics, government and healthcare products,
where the software is the smallest part of the system.
