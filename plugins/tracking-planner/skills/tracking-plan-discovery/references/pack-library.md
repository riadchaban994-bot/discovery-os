# Attribute Pack Library

A starter taxonomy so nobody invents one from scratch for every app. Take the packs that apply, rename
values to match what the app actually shows, delete the rest. Everything here is a starting shape, not
a fact about the product in front of you. A pack copied from this file and never seen in the app is
INFERRED, and it is graded INFERRED in the workbook however obviously correct it looks.

## Why packs exist

Listing parameters event by event guarantees drift. The same field ends up called `vendor_id` on one
event and `restaurant_id` on another, and six months later nobody can join the two. A pack is one
definition attached in many places. Change it once and every event that attaches it changes with it.

Attach packs by name on the event row, naming a subset in brackets when the full pack is overkill:

```
identity, location(city_id, area_id), vendor, items, order
```

## Conventions for every pack below

- `snake_case` names, lower snake enum values. Never mix `Cash` and `cash`.
- Name the unit in the parameter when a number could be read two ways: `distance_m`, `duration_sec`,
  `total_minor`, `weight_g`. A field called `distance` is metres to one engineer and kilometres to the next.
- R means required and its absence fails QA. C means conditional, present only in a named circumstance.
  O means optional and absence means nothing.
- A conditional parameter is absent, never `null`, never `"none"`, never `-1`. Null-filling turns a
  clean absence into a value that pollutes every average and every enum breakdown.
- No raw personal data as a value. IDs, hashes and coarse buckets only. Never an email, a phone number,
  a street address or a card fragment.
- Respect platform ceilings. GA4 allows 25 parameters per event, 40 character names, 100 character
  values, 50 event-scoped custom dimensions and 25 user properties. A 30-field pack is a design error.
- High-cardinality values such as a search term or a full item name are fine as plain parameters but
  poor choices for a registered custom dimension. Register the ID, keep the label for debugging.

---

# Universal core

## `identity`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `user_id` | string | C | `usr_9f31c0a4`, present once authenticated |
| `is_logged_in` | boolean | R | `true` |
| `account_type` | enum | O | `guest`, `registered`, `business`, `staff` |
| `auth_method` | enum | C | `otp_sms`, `password`, `google`, `apple`, `biometric` |
| `account_age_days` | integer | O | `412` |
| `lifetime_order_count` | integer | O | `27` |
| `loyalty_tier` | enum | C | `none`, `silver`, `gold` |

`user_id` must be the identifier the backend uses, not a client-generated one, or client and server
events will never join.

## `session_device`

Do not build this pack. It is documented so nobody rebuilds it. Every mainstream SDK already collects
platform, OS version, app version, device model, screen size, language, country, network type, session
ID, session number and first-open state. Re-sending them burns the custom dimension budget, doubles
payload size and creates a second set of values that quietly disagrees with the first. Add by hand only
what the SDK cannot know: `app_locale` (`ar-SY`, the in-app language toggle rather than the OS locale),
`push_permission_status` (`granted`, `denied`, `not_asked`) and `location_permission_status`
(`while_in_use`, `denied`).

## `location`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `city_id` | string | R | `city_lisbon` |
| `area_id` | string | C | `area_mezzeh` |
| `address_id` | string | C | `adr_5512` |
| `address_type` | enum | O | `home`, `work`, `other` |
| `location_source` | enum | R | `gps`, `saved_address`, `manual_pin`, `ip_fallback` |
| `has_saved_address` | boolean | O | `true` |
| `delivery_distance_m` | integer | C | `2840` |

Never send raw latitude and longitude on a behavioural event. Send the area or a geohash bucket.

## `search`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `search_term` | string | R | `shawarma` |
| `search_type` | enum | R | `global`, `in_vendor`, `in_category`, `voice` |
| `search_result_count` | integer | R | `43` |
| `is_zero_result` | boolean | R | `true` |
| `search_source` | enum | O | `manual_typed`, `recent`, `suggestion`, `trending_chip` |
| `applied_sort` | enum | O | `relevance`, `rating`, `delivery_time`, `price_asc` |

Zero-result search is the cheapest demand signal in any catalogue product and is almost always missing.
Make `is_zero_result` required rather than deriving it at query time.

## `engagement`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `screen_name` | string | R | `vendor_menu` |
| `content_type` | enum | C | `banner`, `carousel_card`, `story`, `push_card` |
| `content_id` | string | C | `bnr_ramadan_2026_03` |
| `list_id` | string | C | `home_top_picks` |
| `list_position` | integer | C | `7`, one-based, top to bottom |
| `entry_point` | enum | O | `home`, `search`, `deep_link`, `push`, `reorder` |
| `time_on_screen_s` | integer | O | `24` |

`list_id` plus `list_position` is what makes merchandising measurable. Without position you cannot tell
a bad banner from a banner nobody scrolled to.

## `error`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `error_code` | string | R | `PAY_DECLINED_INSUFFICIENT_FUNDS` |
| `error_type` | enum | R | `validation`, `network`, `server`, `payment`, `permission` |
| `error_surface` | string | R | `checkout_payment_step` |
| `is_user_recoverable` | boolean | O | `true` |
| `retry_count` | integer | O | `1` |

Use a stable machine code, not the user-facing string. The string gets reworded by a copy change and the
whole series breaks.

## `experimentation`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `experiment_id` | string | C | `exp_checkout_single_page` |
| `variant_id` | string | C | `variant_b` |
| `feature_flag_key` | string | C | `new_home_ranking` |
| `flag_value` | string | C | `enabled` |

Attach only to events inside the experiment surface, and mirror the assignment as a user property so
cohort analysis works without joining on every event.

## `messaging`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `message_id` | string | R | `msg_reorder_nudge_v3` |
| `campaign_id` | string | C | `cmp_2026_08_dormant_30d` |
| `channel` | enum | R | `push`, `in_app`, `sms`, `email`, `whatsapp` |
| `message_type` | enum | R | `promotional`, `transactional`, `lifecycle`, `system` |
| `deep_link_target` | string | O | `app://vendor/vnd_4821` |
| `audience_segment` | string | O | `dormant_30_60d` |

## `support`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `ticket_id` | string | C | `tkt_88301` |
| `contact_channel` | enum | R | `in_app_chat`, `call`, `whatsapp`, `faq` |
| `issue_category` | enum | R | `missing_item`, `late_delivery`, `payment`, `account`, `other` |
| `related_order_id` | string | C | `ord_5512930` |
| `resolution_type` | enum | C | `refund`, `credit`, `redelivery`, `no_action` |

---

# Commerce packs

## `vendor`

Call it whatever the product calls it: vendor, store, merchant, brand, provider, publisher.

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `vendor_id` | string | R | `vnd_4821` |
| `vendor_name` | string | O | `Abu Shaker Shawarma` |
| `vendor_category` | enum | R | `restaurant`, `grocery`, `pharmacy`, `flowers` |
| `vendor_status` | enum | R | `open`, `closed`, `busy`, `pre_order_only` |
| `vendor_rating` | float | O | `4.6` |
| `is_sponsored` | boolean | C | `true` |
| `estimated_delivery_min` | integer | O | `35` |
| `minimum_order_minor` | integer | O | `25000` |

`vendor_status` at the moment of the event matters more than it looks. A large share of the drop-off
between browse and cart is people landing on a closed vendor, and that is invisible after the fact.

## `items`

An array, one object per line item, identical shape everywhere.

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `item_id` | string | R | `itm_66120` |
| `item_name` | string | O | `Chicken Shawarma Wrap` |
| `item_category` | string | R | `sandwiches` |
| `quantity` | integer | R | `2` |
| `price_minor` | integer | R | `18000`, per unit before quantity |
| `item_discount_minor` | integer | C | `2000` |
| `option_ids` | array | O | `["opt_extra_garlic","opt_no_pickles"]` |
| `item_position` | integer | O | `4` |

State in the workbook that item price is per unit before quantity. Half of all implementations get this
backwards and revenue lands out by a factor of the basket size.

## `order`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `order_id` | string | R | `ord_5512930` |
| `cart_id` | string | C | `crt_a91f` |
| `item_count` | integer | R | `4` |
| `subtotal_minor` | integer | R | `72000` |
| `delivery_fee_minor` | integer | R | `1500` |
| `discount_minor` | integer | C | `5000` |
| `tip_minor` | integer | C | `2000` |
| `total_minor` | integer | R | `70500` |
| `currency` | string | R | `EUR` |
| `is_first_order` | boolean | R | `false` |
| `order_type` | enum | R | `delivery`, `pickup`, `scheduled`, `dine_in` |

## `payment`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `payment_method` | enum | R | `cash`, `card`, `wallet`, `bank_transfer`, `on_delivery_card` |
| `payment_provider` | string | C | `sham_cash` |
| `is_saved_instrument` | boolean | C | `true` |
| `payment_status` | enum | R | `authorised`, `captured`, `failed`, `pending`, `refunded` |
| `wallet_balance_used_minor` | integer | C | `10000` |
| `payment_attempt_number` | integer | O | `2` |

`payment_method` is the highest-risk enum in any commerce plan. In cash-dominant markets the real values
bear no relation to the ones in the SDK documentation. Ship only values seen on the payment step.

## `fulfilment`

The consolidation pack. One server event carrying a status, not six events.

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `order_id` | string | R | `ord_5512930` |
| `order_status` | enum | R | `confirmed`, `refused`, `driver_assigned`, `picked_up`, `delivered`, `cancelled` |
| `status_reason` | string | C | `vendor_out_of_stock` |
| `actor` | enum | R | `customer`, `vendor`, `driver`, `agent`, `system` |
| `driver_id` | string | C | `drv_331` |
| `minutes_since_order` | integer | R | `41` |
| `promised_eta_min` | integer | O | `35` |

One hook on the status transition table replaces six backend integration points. The rule that breaks the
merge: a state the business needs as a platform conversion cannot live as a parameter value, because no
mainstream analytics platform can condition a conversion on a parameter. `delivered` is usually the state
that has to stay a separate event.

## `promotion`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `promotion_id` | string | R | `promo_free_delivery_aug` |
| `promotion_type` | enum | R | `voucher_code`, `auto_applied`, `free_delivery`, `bundle`, `first_order` |
| `promotion_source` | enum | R | `push`, `banner`, `manual_code`, `referral`, `wallet_offer` |
| `discount_minor` | integer | C | `5000` |
| `discount_percent` | integer | C | `20` |
| `is_grant` | boolean | R | `true`, the offer was issued to this user |
| `grant_id` | string | C | `grt_77120` |

Grant and redemption must be separately countable or redemption rate is uncomputable. The grant table is
the only correct denominator. Counting redemptions against impressions, or against all users, produces a
number that looks like a redemption rate and is not one.

## `subscription`

| Parameter | Type | Req | Sample |
|---|---|---|---|
| `plan_id` | string | R | `plan_plus_monthly` |
| `plan_tier` | enum | R | `free`, `plus`, `pro` |
| `billing_period` | enum | R | `monthly`, `annual`, `weekly` |
| `price_minor` | integer | R | `4900` |
| `is_trial` | boolean | R | `true` |
| `subscription_status` | enum | R | `active`, `trialing`, `past_due`, `cancelled`, `expired` |
| `cancel_reason` | enum | C | `too_expensive`, `not_using`, `missing_feature`, `switching` |
| `renewal_count` | integer | O | `6` |

---

# Industry variants

What carries over, what changes, what to add, and the two or three events worth arguing about in the
phase 1 review.

## Food delivery and q-commerce

Carries over unchanged: identity, location, search, engagement, error, messaging, support, items, order,
payment, promotion. Changes: `vendor_category` becomes `restaurant`, `grocery`, `pharmacy`, `sweets`, and
`payment_method` is usually cash-first. Add: `fulfilment`, plus a small `basket_edit` pack with
`edit_type` (`quantity_up`, `quantity_down`, `remove`, `option_change`) and `time_in_cart_s`.

- `vendor_view` with `vendor_status: closed`, `entry_point: search`. Closed-vendor views are the leak
  nobody counts.
- `add_to_cart` with `item_id: itm_66120`, `quantity: 2`, `price_minor: 18000`.
- `order_status_changed` (BE) with `order_status: refused`, `status_reason: vendor_out_of_stock`,
  `actor: vendor`, `minutes_since_order: 4`. Vendor refusal is usually the biggest revenue leak and is
  invisible in a client-only plan.

## General e-commerce and retail

Carries over: identity, search, engagement, items, order, payment, promotion, error. Changes: `vendor`
becomes `brand` or `seller` and is often optional, `item_category` needs two or three levels, and
fulfilment statuses become `packed`, `shipped`, `out_for_delivery`, `delivered`, `returned`. Add: `stock`
(`variant_id`, `is_in_stock`, `size`, `colour`) and `returns` (`return_reason`, `refund_minor`).

- `view_item` with `variant_id: sku_88213_m_navy`, `price_minor: 24900`, `is_in_stock: false`.
- `begin_checkout` with `item_count: 3`, `subtotal_minor: 61200`.
- `return_requested` with `return_reason: wrong_size`, `days_since_delivery: 6`.

## Fintech and banking

Carries over: identity (where `auth_method` carries real weight), error, messaging, support,
experimentation. Changes: requiredness tightens everywhere, because a missing field is a compliance
question rather than an analytics gap. Add: `transaction` (`transaction_type`, `amount_minor`,
`counterparty_type`) and `kyc` (`kyc_step`, `kyc_status`, `failure_reason`). Never send an account number,
IBAN, card PAN or counterparty name. Send `account_ref: acc_3f19` and keep the mapping server-side.

- `kyc_step_completed` with `kyc_step: liveness`, `kyc_status: failed`,
  `failure_reason: blurry_document`, `attempt_number: 2`. Fintech onboarding drop-off is a KYC story.
- `transaction_submitted` with `transaction_type: transfer_out`, `amount_minor: 250000`,
  `counterparty_type: new_payee`, `fee_minor: 500`.
- `transaction_failed` with `error_code: LIMIT_EXCEEDED_DAILY`, `is_user_recoverable: true`.

## Media and streaming

Carries over: identity, search, engagement, messaging, error, subscription, experimentation. Changes:
`items` becomes content, and `list_id` with `list_position` moves from optional to required because it
carries the whole recommendation story. Add: `content` (`content_id`, `content_type`, `series_id`,
`duration_sec`, `is_premium`) and `playback` (`playback_position_s`, `percent_complete`, `quality`,
`is_autoplay`, `buffer_event_count`, `playback_source`).

- `playback_started` with `content_id: ep_88_s2e04`, `playback_source: continue_watching`,
  `is_autoplay: true`.
- `playback_progress` at fixed milestones (`percent_complete: 25`), never on a timer, or event volume
  will dwarf everything else in the property.
- `playback_abandoned` with `percent_complete: 8`, `buffer_event_count: 3`. Early abandonment plus
  buffering is a quality problem wearing a content problem's clothes.

## SaaS and B2B tools

Carries over: identity, error, engagement, experimentation, subscription, support. Changes: every event
carries the account as well as the user, or usage cannot be rolled up to a renewal conversation. Add:
`account` (`account_id`, `account_plan`, `seat_count`, `is_trial`), `workspace_object` (`object_type`,
`object_id`, `collaborator_count`, `is_template_used`) and `permissions` (`user_role`).

- `object_created` with `object_type: dashboard`, `is_template_used: true`, `account_plan: team`,
  `user_role: editor`. First object created is the activation moment in most tools.
- `invite_sent` with `invite_count: 3`, `seat_count: 4`. Team expansion predicts renewal better than
  session count.
- `feature_gate_hit` with `feature_key: advanced_export`, `account_plan: free`. This is the upgrade
  funnel and it is almost never instrumented.

## Marketplaces, two-sided

Carries over: identity, search, location, items, order, payment, messaging, error. Changes: add
`actor_side` (`buyer`, `seller`) to identity and make it required, or supply-side behaviour is silently
mixed into demand-side funnels. Add: `listing` (`listing_id`, `listing_category`, `listing_price_minor`,
`photo_count`, `is_promoted`) and `enquiry` (`enquiry_channel`, `response_time_min`, `offer_amount_minor`).

- `listing_published` with `listing_category: mobiles`, `photo_count: 5`, `listing_price_minor: 4200000`.
- `enquiry_sent` with `enquiry_channel: in_app_chat`, `listing_age_days: 2`, `actor_side: buyer`.
- `enquiry_first_response` (BE) with `response_time_min: 210`. Seller response time is the strongest
  predictor of liquidity and only the server can measure it honestly.

## Travel and booking

Carries over: identity, search, location, payment, promotion, messaging, error, support. Changes: search
is the product, so the travel search fields are all required and `order` becomes `booking`. Add:
`trip_search` (`origin_code`, `destination_code`, `depart_date`, `pax_adults`, `cabin_class`,
`days_to_departure`) and `booking` (`booking_type`, `supplier_id`, `nights`, `is_refundable`,
`ancillary_ids`).

- `trip_search_performed` with `origin_code: DXB`, `destination_code: BEY`, `days_to_departure: 21`,
  `pax_adults: 2`, `search_result_count: 118`.
- `fare_selected` with `price_minor: 189000`, `is_refundable: false`, `cabin_class: economy`.
- `booking_confirmed` (BE) with `booking_type: flight`, `ancillary_ids: ["bag_20kg"]`. Client-side
  confirmation in travel is unreliable because payment redirects break the session.

## Health

Carries over: identity (heavily restricted), engagement, error, messaging, support, experimentation.
Changes: most fields drop to optional or disappear, because the safe default is to log the interaction and
not the content. Never send a diagnosis, medication, symptom, test result or free text a patient typed.
Add: `care_interaction` (`interaction_type`, `speciality_id`, `provider_id`, `wait_days`,
`is_first_visit`) and `programme` (`programme_id`, `day_in_programme`, `adherence_streak_days`).

- `appointment_booked` with `speciality_id: spec_dermatology`, `wait_days: 9`, `is_first_visit: true`.
- `teleconsult_started` with `wait_minutes: 4`, `channel: video`.
- `programme_task_completed` with `programme_id: prg_smoking_cessation`, `day_in_programme: 12`.

Get named sign-off from whoever owns data protection before this is built. In health an over-collected
parameter is a legal exposure, not a tidy-up job.

## Education

Carries over: identity, engagement, search, error, messaging, subscription, experimentation. Changes:
content becomes learning objects and progress replaces conversion as the core metric. Add:
`learning_object` (`course_id`, `lesson_id`, `object_type`, `difficulty`, `estimated_minutes`) and
`assessment` (`attempt_number`, `score_percent`, `is_passed`, `time_taken_s`, `hint_used_count`).

- `lesson_completed` with `course_id: crs_arabic_a1`, `lesson_id: lsn_014`, `time_taken_s: 420`.
- `assessment_submitted` with `score_percent: 62`, `is_passed: false`, `attempt_number: 2`.
- `streak_broken` with `streak_length_days: 11`. Streak loss is the clearest churn precursor in consumer
  education and is rarely captured as an event.

## Gaming

Carries over: identity, error, messaging, promotion, experimentation. Changes: session and progression
replace the funnel, and event volume becomes the main design constraint, so aggregate hard and never fire
per frame or per tap. Add: `progression` (`level_number`, `progression_status`, `attempt_number`,
`duration_sec`, `score`), `economy` (`currency_type`, `amount`, `balance_after`, `transaction_reason`) and
`ads` (`ad_placement`, `is_rewarded`, `ad_revenue_minor`).

- `level_completed` with `level_number: 34`, `attempt_number: 5`, `duration_sec: 96`. Attempts per level is
  the difficulty curve and the only reliable churn diagnostic in a puzzle game.
- `currency_spent` with `currency_type: hard`, `amount: 120`, `transaction_reason: spend_on_booster`,
  `balance_after: 40`.
- `ad_completed` with `ad_placement: rewarded_continue`, `is_rewarded: true`, `ad_revenue_minor: 3`.

---

# Currency, money and units

Money causes more silent breakage than any other field. Four rules, all learned from real damage.

**Send integers in minor units and name the unit.** `total_minor: 70500` with `currency: "EUR"`, not
`total: 705.00`. Floats accumulate rounding error across a sum, and a bare `total` gets sent in major units
by one team and minor units by another. The suffix is what stops that argument reaching production.

**Send the currency code with every amount, even in a single-currency product.** It costs three bytes and
it is the only thing that saves the historical series when a second market opens or the currency changes.
A table of amounts with no currency column is unrecoverable.

**Never mix scales inside one parameter.** If `price_minor` is minor units on one event it is minor units
on every event, including the ones added a year later. Do not let a discount arrive as a percentage on one
event and an amount on another. Use `discount_minor` and `discount_percent`, each conditional.

**Plan for redenomination.** On a real engagement a currency was revalued 100 to 1 mid-series. Every
figure below the cut date was suddenly a hundred times smaller than every figure above it. Averages,
cohort revenue curves and any year-on-year comparison became nonsense, and the fix had to be applied
retroactively across every dashboard. The defence is cheap beforehand: carry `currency` on every monetary
event, carry a `currency_version` or `fx_rate_to_usd` alongside it where redenomination or heavy
devaluation is plausible, and store a stable-currency amount such as `total_usd_minor` on high-value
events so at least one series survives. In a high-inflation market that stable-currency field is required,
not optional.

Non-money units follow the same discipline. `duration_sec` not `duration`, `distance_m` not `distance`,
`weight_g` not `weight`, `size_bytes` not `size`. One unit per concept across the whole plan, and never
convert at the client.