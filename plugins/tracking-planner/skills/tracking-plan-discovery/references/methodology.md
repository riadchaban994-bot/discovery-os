# Methodology

This is the analytical core of tracking-plan discovery. The workflow files cover how to drive an
emulator and build the workbook. This file covers how to decide what goes in it.

Every rule below exists because something went wrong without it on a real engagement. The reason is
given with the rule, because a rule without its reason gets discarded the first time it is
inconvenient.

---

## 1. The evidence ladder

Every event, and every enum value inside every parameter, carries an evidence grade. This is the
spine of the method. Without it a design document reads as a specification, engineers build whatever
it says, and that includes the parts you made up.

### The four grades

**OBSERVED.** You saw the surface in the running app and you saw, or can state precisely, the moment
the event fires. You know the control that triggers it and what is on screen at that moment. A
screenshot exists. Example: `add_to_cart` on a dish detail sheet where you pressed the plus control
and watched the cart badge increment.

**PARTIAL.** You saw the surface but at least one branch was never exercised. The event is real,
some of its values are not confirmed. Example: a payment selector showing four rails where only cash
was ever selected. Grade the event PARTIAL and grade the unexercised enum values individually.

**INFERRED.** You never saw it. It comes from convention, from a platform's standard taxonomy, from
a client document, or from your own model of how such products usually work. Example: a `refund`
event designed because operations notes mention refunds, on a surface that never appeared.
INFERRED is legitimate. Presenting it as OBSERVED is not.

**UNVERIFIABLE.** It cannot be checked without doing something you will not do in discovery: placing
a real order, paying real money, subscribing, or waiting for a feature that has not launched.
Everything downstream of the checkout button on a live consumer app is usually UNVERIFIABLE, as is
any server-side status transition on a database you cannot see.

`SDK` is a fifth label, not a grade. It marks events the platform collects automatically
(`first_open`, `session_start`). Nothing to verify, nothing to build, so the ladder does not apply.

### How to decide

Ask two questions in order. Did I see the surface? Did I see the moment? Two yeses is OBSERVED. Yes
then no is PARTIAL. No then no is INFERRED, unless the reason you did not see it is that seeing it
would have required a real transaction, in which case it is UNVERIFIABLE.

Grade downward when unsure. An event wrongly marked PARTIAL costs one line of confirmation in a
workshop. An event wrongly marked OBSERVED costs engineering time on fiction, and costs your
credibility the first time someone opens the app and finds the screen does not exist.

Grade the parameter values, not only the event. This is where the real damage happens. On the
engagement this method came from, roughly forty parameter enum values turned out to be invented
rather than observed, all of them downstream of a checkout button that was never pressed. The events
above them looked reasonable. The values inside them were fiction: refusal reasons the vendor app
does not offer, cancellation actors that are not distinct states, payment error codes copied from a
different gateway. An engineer implementing that list builds an enum that can never be populated,
and an analyst querying it gets an empty bucket and concludes the tracking is broken.

### Why hiding uncertainty is worse than having none

A plan that says "we are not sure about these fifteen events" is directly actionable. It converts
into a one hour workshop agenda with engineering, and the workshop closes it. A plan that presents
the same fifteen events in the same typeface as the confirmed ones produces no workshop, ships to
sprint, and surfaces four weeks later as an integration that cannot be built. The uncertainty did
not go away when you hid it. It moved to a more expensive place to find it.

State the distribution on the workbook cover: 19 OBSERVED, 25 PARTIAL, 5 INFERRED, 21 UNVERIFIABLE,
11 SDK. Anyone reading then knows what kind of document they are holding. And write the governing
sentence in those words: every non-OBSERVED row is a hypothesis to confirm, never an instruction to
implement.

---

## 2. Attribute packs

A pack is a named, reusable bundle of parameters. Events attach packs rather than listing
parameters. Define once, attach everywhere, change in one place.

Listing parameters per event instead produces a workbook where `vendor_id` appears in thirty rows
with four slightly different descriptions and two different types. When the definition changes,
thirty rows need editing and two get missed.

The standard set: identity, location, vendor or catalogue, items, cart and order, payment,
fulfilment, promotion, subscription, search, engagement, support, error, rating, messaging,
experimentation, plus a core context pack for whatever the SDK collects automatically. Not every
product needs all of them. Most consumer transactional products need most.

### What belongs in a pack

Parameters that travel together and are defined by the same thing. `vendor_id`, `vendor_name`,
`vendor_type`, `vendor_status` all describe one entity that is either in context or is not. That is
a pack. `payment_type`, `payment_attempt`, `wallet_balance_sufficient` all describe the money rail
of one attempt. That is a pack.

### How to draw pack boundaries

**The lifecycle test.** Parameters that become known at the same moment belong together. A vendor's
identity is known the instant a vendor page opens. A fulfilment delay is not known until delivery.
Different moments, different packs, even though both describe the same order.

**The co-occurrence test.** If two parameters attach to substantially different sets of events, they
are two packs. If you keep writing a named subset because half the pack never applies, split it.

**The ownership test.** If one team supplies half a pack and a different team the other half, split
it. Packs get implemented by people, and a pack that crosses an ownership line is a pack nobody
finishes.

Keep packs small enough to attach whole, roughly four to ten parameters. A twenty parameter pack is
a filing cabinet, and it will always be attached as a subset, which defeats the point.

### The attachment rule

State this verbatim in the workbook's governance tab. It is the rule engineers get wrong.

> Send every parameter of an attached pack that is defined at the moment the event fires. Omit the
> rest entirely. Never null-fill. Where a pack is listed with named parameters in brackets, send
> only those.

Three things follow. First, *defined at the moment the event fires* is the test, not defined
somewhere in the app. `delivery_actual_min` exists in the domain but is undefined at order
placement, so `order_submitted` omits it even while attaching the fulfilment pack.

Second, omit rather than null-fill. A missing parameter and a parameter carrying null, empty string
or "unknown" are different things in every analytics platform. The first is correctly absent. The
second creates a real enum value called "unknown" that appears in reports, pollutes cardinality, and
hides the fact that the parameter was never wired up. Null-filling is how a plan silently degrades
into a plan that only looks implemented.

Third, a named subset in brackets is a hard restriction. Write it as `VEN (vendor_id, vendor_type)`.
This is how you respect platform parameter caps on high-fan-out events while keeping the full pack
on browse events where the cap is not under pressure.

### Event-specific parameters never repeat a pack parameter

An event may carry extra parameters of its own, strictly additive. If a parameter already exists in
an attached pack it must not be redefined on the event, not even identically. The moment one name is
defined in two places the definitions drift and the workbook stops being a single source of truth.
If an event needs a pack parameter with different semantics, that is a different parameter and it
needs a different name.

---

## 3. Consolidation

Merging sibling events into one parameterised event is where a plan becomes buildable. On the real
engagement, consolidation took 121 event names down to 79 with no analytical loss. The saving is in
what has to be written, not in what can be measured.

### Spotting a mergeable family

Look for events sharing three properties: the same trigger location in the code, the same parameter
shape, and a name that differs only by an outcome or a step. Five payment failures named by cause.
Five address steps named by step. Six order lifecycle events named by status. Each set is one event
wearing different names.

The decisive test is implementation. Ask where the code would live. If all six would be written at
the same place, a status transition table, a form step handler, a payment error handler, they are
one event and their difference is a parameter.

### The parameter that carries the distinction

Name it after the dimension, not the event: `order_status`, `payment_context`, `step_name`. Its
values are the old event names minus the shared prefix. Register it as a custom dimension, otherwise
the merge does cost you something real.

The canonical example. Six events, `order_confirmed`, `order_refused`, `driver_assigned`,
`order_picked_up`, `order_delivered`, `order_cancelled`, become one server event
`order_status_changed` with `order_status` taking those six values. Status-specific parameters ride
conditionally: `refusal_reason` only on refused, `cancel_actor` and `cancel_reason` only on
cancelled, `time_to_assign_sec` only on driver_assigned, `delivery_promised_min` and
`delivery_actual_min` only on delivered. The union is sixteen parameters but no single fire carries
more than ten, so the platform cap is never breached. Six backend integration points become one hook
on the status transition table, the single largest engineering saving available in a delivery-shaped
plan.

### What is lost

Two things, both small, both worth stating so nobody discovers them later. Funnel builders in some
platform interfaces are easier to configure on distinct event names than on one event filtered by
parameter, so the analyst does slightly more work per funnel. And alerting that keys on event name
must now key on name plus parameter. If the client's alerting stack cannot do that, do not merge
that family.

### The four forbidden merges

**Conversions.** Anything that must be a conversion or key event cannot become a parameter value,
because analytics platforms cannot condition a conversion on a parameter. `first_order` stays
separate from `purchase` for exactly this reason: `is_first_order` as a parameter could never be a
conversion, so first-order acquisition could never be optimised against or exported to ad platforms.
Check the conversion list before every merge.

**Platform-native ecommerce events.** `view_item`, `add_to_cart`, `begin_checkout`, `purchase`,
`refund` and their siblings come with built-in reporting, native revenue handling and standard funnels.
Merge them into a custom event and you lose all of it and gain nothing. `refund` in particular nets
revenue natively and keeps the average order value basis honest; folded into a status parameter it
would not.

**Events whose delta from each other is the measurement.** If the number you care about is the gap
between two events, they stay two events. `order_submitted` fires on the client when the button is
pressed; `purchase` fires on the server confirmation. The difference between the counts is the
server-side failure rate. Merge them and that number stops existing. Same for a login wall: attempt
and success stay separate because the drop between them is the diagnosis.

**Merges that put a client sender and a server sender on one event name.** Most platforms do not
deduplicate custom events. Two senders on one name means double counting on every KPI built from it,
and it is invisible because both sends look valid. If a family splits across client and server, it
is at least two events.

A fifth, softer reason: audience readability. If a finding is the headline of the engagement, a
discrete event name lets a team with no analyst practice see it without configuring a filter. That
is a legitimate judgement call, but write it down as deliberate so it does not read as an oversight.

---

## 4. Phasing

### The Phase 1 admission test

An event enters Phase 1 only if it passes at least one of three tests.

1. It fixes something already broken. There is a named defect in current measurement and this event
   is the fix.
2. It is required to compute a contracted KPI. Name which one.
3. It is the only measurement point of a leak that is already costing money.

Everything else waits. Write the passing reason in a `why_p1` column, one sentence, naming the
defect, the KPI or the leak. An event with an empty `why_p1` is not a Phase 1 event whatever
anyone's instinct says. That column also protects the boundary in the room: when a stakeholder
pushes an event forward, the question is not whether it is useful but which test it passes.

### The theoretical minimum is the wrong target

The first cut on the real engagement was 21 events. Defensible on paper, every event justified,
nothing wasted. It was also wrong, and had to be rebalanced to 50.

Cutting to the theoretical minimum leaves a foundation the team must immediately reopen. Two things
had been deferred that could not be: search, the only measurement point of the search-to-purchase
ratio and the zero-result rate, and the subscription product, which was live and being sold that
week. Both came back. Reopening a shipped tracking plan four weeks after launch costs a second
mobile release, a second QA cycle and visible confidence in the plan. Shipping eight more events in
the first release costs a few hours inside a release that is happening anyway.

The right target is the smallest set that does not need reopening. Phase 1 answers every question
the client has contracted for and every question the diagnosis already raised. Phase 2 answers the
questions Phase 1's answers will provoke.

### What earns Phase 2

Depth behind Phase 1's breadth: promotion impressions, favourites, sharing, option-level
abandonment, live-tracking views, onboarding step detail. Each serves a *why* behind a Phase 1
*what*. None serves a contracted KPI and none fixes something broken, which is precisely why they
wait.

Phase 2 is pulled item by item when a Phase 1 result raises a question you cannot answer. It is
never shipped as a batch, because shipping it as a batch reproduces exactly the
over-instrumentation the phasing exists to prevent.

### What gates Phase 3

Phase 3 is not a priority level. It is a list of events blocked on something that has not happened:
a payment method not yet launched, an SMS provider not integrated, a helpdesk with no API
connection, a referral programme with no reward economics defined. Each row names its gate. When the
gate opens the event moves to build with no further debate, because the design work is already done.

Keeping these in the plan rather than dropping them is how the plan stays the source of truth as the
product grows, instead of a snapshot that goes stale on the first launch.

---

## 5. Required, conditional, optional

Every parameter carries one of three obligations. QA tests against this column, so vagueness here
produces an untestable plan.

**Required.** Absent is a bug and QA should fail the build. Use it only where that claim genuinely
holds. `vendor_id` on a vendor-scoped event is required because every vendor analysis joins on it
and it is always known at fire time. If you cannot honestly say a missing value should block a
release, it is not required.

**Conditional.** Present only in a named circumstance and simply absent otherwise. Write the
circumstance out: "on `order_status = cancelled` only", "when the user is authenticated", "market
vertical only". Never null-filled when the circumstance does not hold. A conditional parameter with
an unnamed condition is an optional parameter with ambition.

**Optional.** Absence means nothing and nobody should investigate it. This is where display twins
and descriptive extras live, the fields useful in a report but never in a join.

### The unsourceable rule

Anything that cannot be sourced today is conditional, however important it looks. If the value lives
in a system the client has not integrated, a field the backend does not write, or a third party not
yet contracted, marking it required creates an event that fails QA on every fire from day one. Teams
respond by weakening QA, and then the required marking on every other parameter stops meaning
anything.

Mark it conditional, name the condition as the missing dependency, and put the dependency in the
open questions tab. When it becomes sourceable it is promoted in one edit.

---

## 6. Naming conventions

Lower snake case throughout: events, parameters, enum values. No spaces, no camel case, no capitals.

Events are `object_verb` in the past tense: `cart_viewed`, `order_submitted`, `voucher_applied`. Not
`viewCart`, not `submit_order`. Past tense because an event records something that happened, and the
tense stops people writing events that describe intentions.

Parameters name the thing, not the event carrying them: `vendor_id`, never
`vendor_page_vendor_id`. The same value under the same name on every event that carries it is what
makes cross-event analysis possible at all.

Booleans read as assertions, prefixed `is_` or `has_`: `is_first_order`, `has_promo_applied`.
Durations carry their unit in the name: `delivery_delay_min`, `time_to_assign_sec`. Never a bare
`duration`, because six months later nobody remembers whether it was seconds or milliseconds. Enum
values are stable: renaming one after launch splits every historical series in two.

Never reuse a platform reserved name, and never re-send a parameter the SDK already collects. The
SDK's version wins, and yours is discarded or, worse, silently doubles.

### The honest exception

Platform-standard names break these rules and you use them anyway. GA4's ecommerce taxonomy gives
you `view_item`, `add_to_cart`, `begin_checkout`, `purchase`, `add_shipping_info`, and parameters
like `value`, `currency`, `items`, `transaction_id`. None is `object_verb` past tense. `purchase` is
a noun. `value` names nothing.

Use them exactly as defined regardless. Standard names give you native ecommerce reporting, revenue
handling, predictive audiences and ad platform export. A consistent naming scheme is worth a few
hours of analyst comfort; native revenue reporting is worth considerably more. Say so explicitly in
the workbook so nobody "fixes" the inconsistency later. The rule is that the platform's taxonomy
wins where it exists, and your convention governs everything it does not cover.

---

## 7. Sample values

Every parameter needs an example value, because the example is what an engineer actually reads.
Inventing them is how fiction enters the plan, so derive them instead.

**Take observed values first.** If you saw the value in the app, use it exactly, including its
capitalisation and format. A vendor status of `closed` seen on a search result with a lock icon is
worth more than any plausible alternative you could write.

**Derive the rest from the industry, not from imagination.** Food delivery order statuses follow a
known shape across the category: placed, confirmed, refused, assigned, picked up, delivered,
cancelled. Payment rails in a given market are a knowable list, not a guess. Ratings are one to five
in almost every consumer product. Use the category's real vocabulary, and mine any client documents
first, because their words become the values engineers implement.

**Show shape, not just a value.** For identifiers show format and cardinality: `"v_00184", ~900
values`. For strings show the length constraint. For numbers show the unit and a realistic
magnitude. Cardinality is what tells an engineer whether a field can be a registered custom
dimension.

**Mark every value that was never observed.** Split the enum in the parameter's notes:
"`restaurant` and `market` OBSERVED 25 Aug on the home vertical switcher; `electronics` and `other`
appear in the API but were never browsed and never visible in the app, so confirm the real vertical
list with the team before implementing." That note is what stops an engineer building an enum with
two live values and two that can never be populated.

**Reserve values belonging to unlaunched features.** If a card launch is coming, add `card` to the
enum but mark it reserved, not to be emitted until the launch release, with no such row in the
current build. Engineering gets the complete target without licence to ship a value that appears in
reports as a real but permanently empty rail.

**Do not invent failure taxonomies.** Refusal reasons, cancellation reasons and payment error codes
are the highest risk values in any plan, because they sit downstream of a transaction you never
completed and they look easy to guess. They are not guessable. Whatever the gateway or the vendor
app actually offers is what the enum must be. Until you have that list from engineering, the
parameter is conditional, the values are marked INFERRED, and the question goes in the open
questions tab.