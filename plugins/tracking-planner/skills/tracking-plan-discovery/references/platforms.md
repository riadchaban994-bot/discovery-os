# Destination rules

A tracking plan is not portable. The same set of user journeys produces a different plan depending on where the events land, because each destination imposes its own caps, its own billing model, and its own idea of what a "conversion" is. Design against the destination the client actually has, not against an ideal one.

Two working rules before anything else.

**Confirm the destination before writing a single event row.** Ask which tools are live today, which are contracted but not implemented, and which are aspirational. On the food-delivery engagement the answer was GA4 plus Firebase, which is the most constrained combination in common use, and that constraint shaped a third of the design decisions. Had the answer been Amplitude, half of the consolidation work would have been unnecessary.

**Verify current limits before you finalise.** The numbers below were correct when written and platforms move them. Check the vendor's own limits page, or pull current docs, before you publish a plan that depends on a specific ceiling. A plan that busts a cap fails silently: the platform drops the parameter, nobody gets an error, and the gap is discovered months later when a report comes back empty.

---

## GA4 and Firebase

Treat these as one destination. A Firebase app stream and a GA4 property are the same data pipeline with two consoles on top. Anything logged through the Firebase SDK appears in GA4, and the limits are GA4's.

This is the deepest section because GA4 is the most restrictive mainstream destination, and because its restrictions are the reason the method uses consolidation, attribute packs and a strict Phase 1 in the first place.

### The caps that change the design

| Limit | Value | What it forces |
|---|---|---|
| Distinct event names | 500 per app instance | Consolidation, and a hard stop on per-screen event names |
| Parameters per event | 25 | Attribute packs must be attached selectively, not wholesale |
| Event name length | 40 characters | Short, disciplined names |
| Parameter name length | 40 characters | Same |
| Parameter string value length | 100 characters | No free text, no addresses, no product descriptions |
| User properties | 25 per property | Reserve them for slow-changing traits only |
| User property name / value length | 24 / 36 characters | `subscription_tier` fits, `current_subscription_tier_name` does not |
| Event-scoped custom dimensions | 50 | Ration them; not every parameter earns registration |
| User-scoped custom dimensions | 25 | Effectively the same budget as user properties |
| Item-scoped custom dimensions | 10 | Anything item-level beyond this is BigQuery only |
| Custom metrics | 50 | Numeric parameters compete for a separate budget |
| Items in an `items[]` array | 200 per event | Large baskets truncate |
| Key events (conversions) | 30 per property | Forces a decision about what genuinely counts |

The 25-parameter cap is the one that bites. A generously specified `purchase` event with identity, location, vendor, order, payment, fulfilment and promotion packs all attached blows past it immediately. This is exactly why attribute packs allow a named subset: attach the pack, then list the fields the event carries. Count the parameters on every event before publishing. Do it as an arithmetic check on the workbook, not by eye.

Note that GA4 automatically appends its own parameters, and the 25 applies to the custom ones you send. Do not run to exactly 25 and hope.

### Reserved names and prefixes

Event names, parameter names and user property names must not begin with `firebase_`, `google_` or `ga_`, and must not start with an underscore or a digit. Names must be letters, digits and underscores only, starting with a letter.

A set of event names is reserved and will be silently rejected or will collide with automatic collection: `first_open`, `first_visit`, `session_start`, `screen_view`, `page_view`, `user_engagement`, `app_update`, `os_update`, `app_remove`, `app_clear_data`, `app_exception`, `in_app_purchase`, `error`, the `ad_*` family, the `notification_*` family, the `dynamic_link_*` family, and the `app_store_subscription_*` family.

Two practical consequences. First, never name a custom error event `error`; use `app_error` or `api_error`. Second, do not re-log `screen_view` manually while automatic screen tracking is on, because you will double every screen count and the doubling is invisible in the UI.

### Custom definitions never backfill

This is the single most expensive GA4 fact and the one teams learn late.

A parameter you send is stored in the event, but it does not appear in any standard or exploration report until it is registered as a custom dimension or metric in the GA4 admin. Registration applies from the moment it is created onwards. It does not reach back. If the release ships in March and someone registers `vendor_id` in June, March to May is gone from the UI permanently.

So the plan must carry a registration step that happens **before** the release ships, and the workbook needs a tab or column that lists every parameter requiring registration, its scope, and its display name. Hand that list to whoever administers the property and treat it as a release blocker, not a follow-up task.

The BigQuery export is the exception. It contains every parameter sent, registered or not, from the day the export was switched on. That is the argument for enabling the export on day one even if nobody is querying it yet.

### Key events cannot be conditioned on a parameter

A key event is marked at the level of the event name. There is no way to say "count `purchase` as a key event only when `order_status = delivered`", or "count `sign_up` only when `method = phone`". Audiences can filter on parameters. Key events cannot.

This is a hard constraint on consolidation and it is the reason consolidation has forbidden cases. Two rules follow.

**If a moment must be a conversion, it needs its own event name.** Activation is the standard example. If the business defines activation as first completed order, it cannot be a parameter value on a generic `purchase` or on a consolidated order-status event. It needs a dedicated event, fired once, for example `first_order_completed`, so it can be marked as a key event and used as an audience trigger and a campaign objective.

**The consolidation win survives anyway, with one carve-out.** On the food-delivery plan, six fulfilment events collapsed into one server-side event carrying an `order_status` parameter, taking six backend integration points down to one hook on the status-transition table. That merge was correct because none of those six states needed to be a conversion in the ad platform. Had the client wanted to optimise ad spend on delivered orders specifically, `order_delivered` would have had to stay separate. Ask the question explicitly: does marketing need to bid on this moment? If yes, it keeps its name.

Also worth knowing: importing key events into Google Ads works on the event name too, so the same rule governs ad optimisation.

### Recommended events and the items array

GA4 has a set of recommended event names that populate prebuilt reports, particularly the ecommerce set: `view_item_list`, `select_item`, `view_item`, `add_to_cart`, `view_cart`, `remove_from_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, `purchase`, `refund`, `view_promotion`, `select_promotion`, `add_to_wishlist`.

Use these names exactly where the semantics match. A custom `cart_add` gets nothing from GA4's monetisation reports; `add_to_cart` populates them for free. The cost of a bespoke name is real reporting capability, and the client pays it forever.

The ecommerce events carry an `items[]` array with its own item-scoped parameters (`item_id`, `item_name`, `item_category` through `item_category5`, `item_variant`, `price`, `quantity`, `item_brand`, plus up to 10 custom item parameters). Item-scoped parameters do not count against the event's 25.

In a marketplace or delivery context, map the catalogue sensibly and consistently:

- `item_id`: the dish or SKU identifier, stable across sessions
- `item_name`: the dish name in a single language, not the localised display string
- `item_brand`: the vendor or restaurant, so vendor-level revenue works in standard reports
- `item_category`: cuisine or menu section
- `item_variant`: size or option set
- `item_list_id` / `item_list_name`: which list the item was chosen from, so search results, home carousels and category browse can be compared

`purchase` requires `transaction_id`, `currency` and `value`, and `currency` must be a valid ISO 4217 code or revenue reporting breaks. If the app operates in a currency with unstable or informal rates, record the local amount and the currency honestly, and hold any converted figure as a separate numeric parameter rather than lying in `value`.

### Measurement Protocol

Server-side events reach GA4 through the Measurement Protocol. It works and it is the right tool for backend-truth events such as order status transitions, refunds and subscription renewals, but it has real gaps that must be recorded in the plan.

- No automatic session attribution. Events do not join a session unless you pass a matching `session_id`, and the client is the only place that knows it. If session-scoped analysis matters for an event, it belongs on the client.
- No campaign attribution. Measurement Protocol events do not acquire source, medium or campaign on their own. A purchase sent only from the server will not credit the acquisition channel unless the identifiers are passed through and stitched.
- Identity is mandatory and fragile. You must send `client_id` (web) or `app_instance_id` (app). If the backend does not store it against the user, the event lands as a new anonymous user and inflates user counts. Confirm the backend actually holds this identifier before designing any BE-only event. If it does not, that is a Phase 1 engineering prerequisite, not a detail.
- Events with a timestamp older than roughly 72 hours are dropped, which rules out naive historical backfill.
- Validation is weak. The debug endpoint catches schema errors; nothing catches a semantically wrong value. Server events need their own QA pass.
- Batches are capped (25 events per request) and payload size is limited.

The FE + BE pattern in the plan, where the client fires and the server backfills only if the client event never arrives, exists because of these gaps: client events carry attribution, server events carry truth. Never let both fire unconditionally, because GA4 does not deduplicate custom events and the KPI doubles.

### BigQuery export is the raw truth

Enable the export early. It gives you every parameter regardless of registration, no cardinality bucketing, no sampling, no 25-registration budget, and the ability to reconstruct any metric later. The `events_` tables store parameters as a repeated record, which is awkward to query but complete.

Two behaviours in the GA4 UI that BigQuery is immune to, and that should be flagged in the plan wherever a high-cardinality parameter appears: values beyond the daily row limit collapse into an `(other)` bucket, and standard data retention defaults to a short window (commonly two months) for exploration, which quietly caps how far back any custom analysis can look. Set retention to the maximum on day one; it is one click and it is also not retroactive.

---

## Amplitude, Mixpanel and PostHog

Different products, similar shape, and all three relax the constraints that dominate GA4.

**Billing is volume-based**, on events ingested or on monthly tracked users. This inverts one incentive and leaves another intact. There is no cap on distinct event names worth designing around, so consolidation stops being a technical necessity. But volume costs money, so high-frequency events (scroll, impression, every keystroke in search) need a commercial justification, not just an analytical one. Consolidation still helps, because merging six events into one parameterised event does not reduce volume, but removing an event that nobody will query does.

**There is no hard parameter cap** in the GA4 sense. Practical limits still exist: property counts in the hundreds or thousands per event type, string values truncated at around 255 to 1024 characters depending on the platform, and array sizes capped. The real limit is comprehension. An event with 60 properties is not a richer event, it is an undocumented one. Keep attribute packs disciplined for human reasons even when the platform allows sprawl.

**Group analytics changes the design.** All three support an account or organisation dimension, which GA4 does not do natively. In a marketplace this means the vendor can be a first-class entity rather than a parameter, so vendor-level retention, vendor cohorts and vendor-level funnels become native rather than derived. If the destination supports groups, add a group definition to the plan (typically vendor, and in B2B contexts the customer account) and state which events set group properties. Note that group analytics is a paid tier on Amplitude and Mixpanel, so confirm entitlement before designing around it.

**Conversions are not a schema-level concept.** Funnels and any step in them are defined at query time, and steps can filter on properties. This removes the "activation needs its own event" constraint entirely. If the plan may be ported to GA4 later, keep the dedicated activation event anyway; it costs one event name and saves a re-instrumentation.

**Identity resolution is stronger.** Amplitude and Mixpanel merge anonymous and identified histories on identify, and PostHog does the same when a person profile is created. This makes pre-login behaviour analysable in a way GA4 struggles with, so the identity pack matters more, not less. Be explicit about when `identify` is called and with which ID.

**Schema governance tooling exists and should be used.** Amplitude has a taxonomy and governance layer, Mixpanel has Lexicon, PostHog has a data management view. The workbook is the source of truth; these are where it gets enforced. Note in the plan that the event and property definitions should be loaded into the destination's schema tool at implementation, so unplanned events show up as violations rather than as normal traffic.

One PostHog-specific point: anonymous events cost materially less than events attached to a person profile. If a high-volume event has no need for person-level analysis, capture it without a profile.

---

## Segment and other CDPs

A CDP is not a destination, it is a routing layer. The instrumentation is written once against the CDP's API and the CDP fans it out to GA4, Amplitude, the warehouse, the ad platforms and the email tool.

The model is small: `track` for actions with properties, `identify` for user traits, `group` for account or organisation traits, `page` and `screen` for surfaces, `alias` for stitching identities. The plan maps cleanly onto it. Events become `track` calls, the identity pack becomes `identify` traits, and the vendor pack in a marketplace becomes `group` traits where group analytics is in play downstream.

Three things to get right.

**The plan must still be written against the strictest downstream destination.** Segment does not rescue you from GA4's 25-parameter cap or its 40-character names. It will happily accept a 60-property event and quietly drop most of it on the GA4 leg. If GA4 is in the destination list, design to GA4's limits and let the richer destinations receive the same clean payload.

**Naming convention is a routing decision.** Segment's convention is `Object Action` in title case with a space, for example `Order Completed`. GA4 requires `snake_case` with no spaces. Pick one canonical form for the plan and note the transformation. Most teams write `snake_case` throughout and let the GA4 destination pass it through unchanged, which is the lower-risk direction because the transformation that has to be right is the one nobody sees.

**Use the tracking-plan enforcement feature if the client has it.** Segment Protocols (and equivalents in RudderStack or mParticle) accept the schema and block or flag violations at the edge. That turns the workbook from a document into a control. Where it exists, add a row to the implementation notes stating that the plan is to be uploaded and enforcement set to warn first, block later.

Billing on CDPs is usually per monthly tracked user or per API call, so the event-volume discipline from the previous section applies here too, once, at the source.

---

## Destinations that store no properties

Some tools in a stack accept events but discard everything except the event name, the user identifier and the timestamp. Product-adoption scoring tools of the Accoil type work this way, and so do some lightweight lifecycle-messaging and in-app-guidance integrations.

This breaks consolidation completely. A single `order_status_changed` event carrying `order_status = delivered` arrives at that destination as an undifferentiated `order_status_changed`. Every state looks identical. The scoring model sees noise.

Handle it in the routing layer, never by damaging the core plan:

1. Keep the consolidated, parameterised event as the canonical definition. It is right for the warehouse, right for GA4, right for the product analytics tool.
2. In the CDP or the server-side routing layer, expand the specific distinctions that the property-less destination needs into named events, for example `order_delivered` and `order_cancelled`, and route those **only** to that destination.
3. Record this in the workbook as a destination note on the affected event, not as extra rows in the event list. The mobile and backend teams must not see extra events to build; the expansion is configuration, not code.

If there is no routing layer and the client fires directly to the property-less tool, then that tool's needs must be met with genuinely separate event names, and consolidation is limited accordingly. Say so explicitly in the plan with the reason, because the next analyst will otherwise "tidy up" the redundancy and break the scoring model.

---

## Decision table

| Destination | What changes in the plan |
|---|---|
| GA4 / Firebase | Hard caps drive everything: 25 parameters per event, 40-character names, 100-character values. Consolidate aggressively. Register every custom dimension before release because nothing backfills. Give any conversion moment its own event name. Use recommended ecommerce names and `items[]`. Enable BigQuery export and maximum retention on day one. Document Measurement Protocol gaps on every BE event. |
| Amplitude | No name cap, so consolidate for clarity rather than survival. Design for volume-based cost. Use group analytics for vendor or account as a first-class entity if entitled. Funnel steps filter on properties, so no dedicated conversion events are needed. Load the schema into the governance layer. |
| Mixpanel | As Amplitude. Group analytics is a paid add-on, confirm before designing on it. Load definitions into Lexicon. Watch property value truncation. |
| PostHog | As Amplitude. Billed per event ingested; capture high-volume events without person profiles where person-level analysis is not needed. Up to five group types. |
| Segment or another CDP | Design once against the strictest downstream destination, then route. Map events to `track`, identity pack to `identify`, vendor or account pack to `group`. Fix one canonical naming form and document the transformation. Upload the plan to the enforcement layer where available. |
| Property-less destination (Accoil type) | Distinctions must live in the event name. Keep the consolidated event canonical and expand named variants in the routing layer for that destination only. Record as a destination note, not as new build rows. |
| Warehouse only (BigQuery, Snowflake) | Almost no constraints. Cardinality, cost and schema evolution are the real limits. Favour richer events and fewer of them. Still fix a naming convention, because SQL written against inconsistent names is where the analysis time goes. |
| Ad platforms as a downstream destination | Optimisation targets are event names. Anything marketing needs to bid on cannot be a parameter value, whatever the analytics destination allows. |

---

## Universal rules

These hold whatever the destination, and they belong in the plan regardless.

**One convention, applied without exception.** `snake_case`, `object_action` order, past tense, for example `vendor_viewed`, `cart_item_added`, `checkout_started`. Do not mix `add_to_cart` and `cart_add` in the same plan. Where a destination's recommended name conflicts with the convention, the recommended name wins and the exception is noted.

**A parameter name means the same thing everywhere.** If `vendor_id` is the vendor's primary key on one event, it is the vendor's primary key on all of them, never the display name and never a slug. This is what makes attribute packs work and what makes cross-event joins possible without a translation table.

**One sender per event.** Most platforms do not deduplicate custom events. Two senders means double-counted KPIs and no error anywhere. Where the plan says FE + BE, it means the server fires only when the client event did not arrive, which requires a shared idempotency key, usually the order or transaction identifier. If the backend cannot implement that check, the event is FE or BE, not both.

**Enumerated values are closed lists, declared in the plan.** An open string field becomes forty spellings of "cash" within a quarter. Every enum value must be OBSERVED in the app or explicitly marked as a hypothesis to confirm; the forty invented enum values on the food-delivery engagement all sat downstream of a checkout button that was never pressed.

**No PII in event parameters.** No names, phone numbers, email addresses, delivery addresses or free-text notes. GA4 will delete data found to contain it, and every other destination creates a deletion-request problem. Send stable pseudonymous identifiers, and send location as an area or zone identifier rather than coordinates or a street address.

**Conditional means absent, not null.** A parameter that applies only in a named circumstance is simply not sent otherwise. Sending `null`, `""`, `0` or `"none"` creates a value in the enum, pollutes cardinality, and makes the difference between "did not apply" and "failed to populate" unrecoverable.

**Timestamps in UTC, one format.** Client clocks are wrong. Where event ordering matters, particularly for status transitions, the server timestamp is authoritative and the plan says so.

**Version the plan and stamp the release.** Record the app version that first carries each event. When a funnel breaks, the first question is always which build changed, and without the stamp the answer costs a day.
