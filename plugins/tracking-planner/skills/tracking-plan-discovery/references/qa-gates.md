# QA gates

Every check in this file exists because it failed on a real engagement and cost real time. None of them are theoretical. Run them in order. A gate that fails sends you back to the tab that caused it, not forward to the next gate.

The gates are cheap to run and expensive to skip. The single most common failure mode is treating the workbook as finished the moment the last row is written. It is not finished until it has been rendered, looked at, cross-checked against the questions it is supposed to answer, and attacked by someone trying to prove it wrong.

---

## What the script enforces, and what it does not

`scripts/validate_plan.py` implements some of these gates and not others. Knowing which is which
saves you diffing the doc against the code, and stops you trusting a "Clean" result further than it
deserves.

**Enforced, and fails the run:** event naming rules for the destination, parameter budgets against
the platform cap, dimension and metric quotas, user-property name and value lengths, attachment
integrity (a named parameter must exist in its pack), unknown pack ids, dangling event names in
journeys, values that a spreadsheet would parse as a formula, screenshots cited with no folder
present, and counts stated in prose that disagree with the data.

**Enforced as a warning:** missing evidence grades, missing source markers, missing
required/conditional/optional markers, event parameters that repeat a pack parameter, a heaviest
event sitting exactly at the parameter cap, dangling event names in the other tabs, unreferenced
screenshots, an em dash, and a plan where no event at all is graded OBSERVED.

**Not enforced, and still your job:** everything visual. Whether a column wraps mid-word, whether a
repeated header stamps the wrong labels on a second table, whether a row is clipped, whether the
thing reads well. Also every judgement call: whether an event earns its phase, whether a merge lost
a measurement, whether an enum value is real or was invented by someone confident. A script cannot
tell an observation from an assertion, which is the whole reason the evidence grades are written by
hand.

That last group is why the render-and-look step is not optional polish. It is the only pass that
sees what the file will look like to the person you send it to.

## Gate 1: Structural integrity

Consolidation and renaming break references. This is the gate that catches it.

**1.1 No dangling event names.** After any merge, every reference to the merged-away names must be gone. On the real plan, six fulfilment events were consolidated into one `order_status_changed` event carrying an `order_status` parameter. The event tab was updated. Two other tabs were not: the key-event list still named `order_delivered`, and the KPI mapping tab still computed delivery rate from `order_driver_assigned`. Both tabs pointed at events that no longer existed anywhere in the plan. An engineer reading either tab would have built the old six.

Check it mechanically, not by eye. Build the set of event names from the event tab, then extract every event name mentioned in every other tab and in every prose paragraph, and diff the two sets. Anything in the second set but not the first is a break. Anything in the first set but never referenced anywhere is either dead weight or a missing mapping, and both are worth a look.

**1.2 Every derived table is generated, never hand-maintained.** The custom dimensions tab, the parameter index, the pack-to-event matrix, the phase counts: all of these are functions of the event tab and the pack definitions. Generate them from source every time you rebuild.

On the real plan a custom dimension table was hand-kept for two revisions. It drifted. Three parameters had been renamed on the event tab and the dimension table still carried the old names. Registration errors of that kind are not recoverable: a platform that registers a custom dimension against the wrong parameter name collects nothing for that dimension, and it cannot be backfilled once the data has passed. You do not get those weeks back. Regenerating the table takes seconds and removes the failure class entirely.

**1.3 Counts in prose match counts in data.** Every number stated in the summary tab, the readme, the phase notes, or the covering email must be computed from the workbook, not typed from memory. "79 events across three phases, 50 in Phase 1" is a claim that will be checked by the person who has to build it. On the real plan the summary said 52 while the tab held 50, because two events were cut and the sentence was not. Small error, large credibility cost, because it is the first thing the client's data lead counts.

**1.4 The key event list matches the key event flags.** If the workbook has both a boolean column marking key events and a separate list or summary of them, they will diverge. Generate the list from the flags. Then sanity-check the flags themselves against the consolidation rule: anything that must be a conversion cannot be a parameter value, so if a key event is flagged and it was merged into a parameterised parent, that merge was illegal and has to be reversed. `purchase` cannot live inside `order_status_changed` as `order_status = confirmed`, because no analytics platform can condition a conversion on a parameter value.

**1.5 Evidence grade present and defensible on every row.** No blanks. Then spot-check upward: pick five rows graded OBSERVED and confirm each names a screenshot that actually exists in the workbook. On the real plan roughly forty parameter enum values were graded as observed when they had in fact been written from convention, all of them downstream of a checkout button that was never pressed. That is the exact shape this check is for. If the firing moment was not seen, the grade is INFERRED or UNVERIFIABLE, and no amount of confidence changes that.

**1.6 Source marking present and single-sender.** Every event says FE, BE, FE + BE, or SDK. Then check for accidental double senders: an event marked FE that also appears in a backend section, or two events with different names that describe the same moment from opposite sides. Most platforms do not deduplicate custom events, so two senders means every KPI computed from that event is inflated, silently, forever.

---

## Gate 2: Parameter budget

Attribute packs hide their own size. An event that attaches identity, location, vendor, items, order, payment, fulfilment and promotion looks like eight words on the page and is forty-plus parameters in the payload.

Expand every pack attachment into concrete parameter names for the heaviest five or six events, count them, and compare against the platform cap. On GA4 that is 25 event parameters per event, and the automatically collected parameters count against you. On the real plan the checkout event expanded to exactly 25. Exactly at the cap is not a pass. It means the first parameter anyone adds during implementation silently drops, and nobody notices until a report is empty three months later. Aim for headroom of at least three or four parameters on the heaviest events, and if you cannot get it, move something to a user property or a separate event and say so in the notes.

Also check the account-level budgets while you are here: registered custom dimensions against the platform ceiling, and user-scoped properties against theirs. Both are shared across the whole property, so a plan that fits its own events can still be unbuildable in an account that already has half the slots spent. Ask for the current registered list rather than assuming the account is empty.

---

## Gate 3: The spreadsheet formula trap

A cell whose value begins with `=`, `+`, `-` or `@` is parsed as a formula by every major spreadsheet application. It renders as an error, usually `#NAME?`, and the actual text is invisible to the reader.

This bites tracking plans constantly, because the natural way to write a condition is `= 'delivery'` or `-1 if unknown` or `@handle`. In the source data the string is perfectly correct. Nothing in the writing library warns you. The problem exists only in the rendered view.

Two rules follow. First, scan every string cell for a leading `=`, `+`, `-` or `@` before writing the file, and neutralise it by rewriting the phrasing (`equals 'delivery'` instead of `= 'delivery'`) rather than by prefixing an apostrophe, which some readers show literally. Second, and this is the rule that matters:

**Always render the workbook and look at it with your own eyes.** Open it, or convert it to images, or screenshot every tab. Do not certify a workbook you have only written. The formula trap, clipped rows, broken links and lost formatting are all invisible in the source and obvious in the render. On the real engagement this was learned by shipping a file where a whole column of conditional rules displayed as `#NAME?` errors.

---

## Gate 4: Link portability and evidence

Local file hyperlinks do not survive. A link to `/Users/.../screenshots/checkout_01.png` works only on the machine that made it, fails in Excel on any other machine, and fails always in browser-based spreadsheet apps, which is where clients actually open things. The client sees a dead link and concludes the evidence does not exist.

So the evidence lives inside the workbook. Embed the screenshots on a dedicated evidence tab, one per row with a stable identifier, and link from each event to its screenshot with an internal reference to the cell on that tab. Internal links travel with the file.

Check, on the rendered file: every screenshot reference on the event tab resolves to a row that exists on the evidence tab; every embedded image actually appears rather than showing as a broken placeholder; no cell anywhere contains an absolute local path; and every OBSERVED grade has at least one image behind it. An OBSERVED row with no evidence attached is an INFERRED row wearing a better label.

---

## Gate 5: Row heights and wrapping

Spreadsheet writing libraries emit no row heights. Each application then guesses, and they guess differently. Excel on a Mac, Excel on Windows, Google Sheets and Numbers will all show your 400-character definition cell at a different height, and at least one of them will show two lines of a six-line paragraph with the rest cut off. The reader assumes the text is what they can see.

Compute explicit heights instead of hoping. For each row, take the longest wrapped cell, estimate lines as the character count divided by the characters that fit in that column at that font size, multiply by the line height, and add padding. Set the row height explicitly. Set wrap on every long-text column. Freeze the header row and the event-name column so a wide table stays readable when scrolled.

Then confirm it in the render, because this is another failure that only exists visually. Look for clipped text, columns narrower than their content, and any merged cells, which break sorting and filtering and should not be in a working document at all.

---

## Gate 6: Content and voice

The workbook is a consulting deliverable, not a data dump.

Check British spelling throughout, including in event descriptions where American variants creep in from convention. Check that no em dashes survived. Check the banned vocabulary list for the engagement: no alarmist framing about the client's current state, no phrasing that blames the client's team for gaps, no filler sentences that restate the column header.

Definitions must say when the event fires, not what it means in the abstract. "Fires when the user taps Confirm order on the checkout screen, before the network call" is useful. "Tracks order confirmations" is not, because two engineers will place it in two different moments and the funnel will not reconcile.

One exception overrides all of the above: quoted application copy stays verbatim. If the button says "Checkout" and the app is American-spelled, or the empty state says something ungrammatical, quote it exactly as it appears and mark it as quoted. The plan's job is to describe the app that exists. Correcting the app's own words in the plan makes the plan un-matchable against the screen the engineer is looking at.

---

## Gate 7: The plan must answer its own questions

This is the gate that catches a plan which is internally perfect and commercially useless.

Take the contracted KPIs one at a time. For each one, write the calculation using only events and parameters that exist in the workbook, and name the phase each of them lands in. If the calculation needs an event that sits in Phase 3, the KPI cannot be reported until Phase 3, and that has to be said out loud rather than discovered by the client in month two. If the calculation cannot be written at all, the plan has a hole and the gate has done its job.

Watch the denominator specifically. A rate needs both halves instrumented, and the denominator is the half that gets forgotten. Voucher redemption rate needs the grant, not just the redemption, and the grant lives in a different table and often a different system from the redemption. Get the denominator wrong and the metric is not slightly off, it is meaningless.

Then take each named leak, every drop-off or failure the engagement was hired to size, and prove the event set measures it. A leak needs an entry event, an exit event, and enough parameters to say why. If the plan can tell you that people left the checkout but not what they left from, it has not measured the leak, it has only counted it.

Finally, check that no more than a small handful of Phase 1 events fail the admission test: fixes something already broken, or is required to compute a contracted KPI, or is the only measurement point of a leak already costing money. Anything that passes none of the three is padding and belongs in a later phase. Equally, resist over-cutting. The first cut on the real engagement reached 21 events and had to be rebuilt to 50, because a foundation the team must immediately re-open is not a foundation. If Phase 1 cannot answer the questions in the contract, it is too small, whatever the event count says.

---

## Gate 8: The adversarial pass

Confirmation is worthless here. A reviewer asked "does this look right?" will say yes. Brief an independent reviewer, a fresh subagent or a colleague who has not touched the plan, to refute it.

Give them the workbook, the screenshot set, the contracted KPIs and the leak list, and ask them to find:

- Every event graded OBSERVED whose screenshot does not actually show the firing moment, only the surrounding screen.
- Every parameter enum value that appears in no screenshot and in no client document, which is the invented-value failure in its native habitat.
- Every KPI in the contract that cannot be computed from Phase 1, stated as a calculation they attempted and failed to write.
- Every consolidation that merged something the client will later need as a conversion.
- Every event with two possible senders, and the double-count it would cause.
- Every Phase 1 event that passes none of the three admission tests.
- Anywhere the prose count and the tab count disagree.

Ask for findings as specific cell references, not impressions. Then fix what they find and re-run gates 1 through 7, because fixes break structure. A reviewer who returns nothing has either been given a genuinely clean plan or has not been adversarial enough, and on a first pass it is almost always the second.

---

## Final pre-handover checklist

Run this in order. Do not hand over with any item unticked.

1. Every event name referenced anywhere in the workbook exists on the event tab, checked by set difference, not by reading.
2. Every derived tab, custom dimensions, parameter index, pack matrix, phase counts, has been regenerated from source in this build.
3. Every count stated in prose matches the count computed from the data.
4. The key event list is generated from the key event flags, and no key event has been merged into a parameterised parent.
5. Every event row carries an evidence grade, and five randomly chosen OBSERVED rows each resolve to a real embedded screenshot.
6. Every event row carries a source marking, and no moment has two senders.
7. The heaviest events have been expanded pack by pack into concrete parameter counts, and each sits below the platform cap with headroom, not at it.
8. Account-level custom dimension and user property budgets have been checked against what the account already has registered.
9. No cell value begins with `=`, `+`, `-` or `@`.
10. The workbook has been rendered and visually inspected, every tab, by eye.
11. No absolute local file paths anywhere; all screenshot references are internal links to embedded images that display correctly.
12. Explicit row heights are set, wrap is on for long-text columns, panes are frozen, no merged cells, nothing clipped in the render.
13. British spelling, no em dashes, no banned vocabulary, no blame framing, and quoted application copy left exactly as the app writes it.
14. Every contracted KPI has a written calculation using only events in the plan, with the phase each depends on named.
15. Every named leak has an entry event, an exit event, and enough parameters to explain the drop.
16. Every Phase 1 event passes at least one of the three admission tests, and Phase 1 as a whole answers the contract.
17. The adversarial review has been run, its findings fixed, and gates 1 to 7 re-run after the fixes.
18. The file opens cleanly from a different machine or account than the one that built it.
