# App walkthrough: the field playbook

This is how you actually walk an app before you write a single event name. The tracking plan is only as good as what you saw. Every rule below exists because skipping it once produced a plan that engineers could not build, or built wrong.

The output of a walkthrough is three things: a folder of ordered screenshots, a walkthrough log that records what the user sees and what the app does on each surface, and an explicit list of what you could not reach. That third one matters as much as the first two. An unreached surface that is not declared becomes an INFERRED event that reads like a spec.

## Before you touch the app

Set up the capture folder first. Retrofitting names onto ninety screenshots is a wasted hour.

```
walkthrough/
  screens/          SCR-01_first-open-splash.png ...
  walkthrough-log.md
  unreachable.md
```

Ask the client for four things before you start, because two of them gate what you can see at all:

1. A test account with order history, or confirmation that no such account exists.
2. Whether a test payment method or sandbox mode exists. If not, the entire post-conversion lifecycle is unreachable and you need to say so on day one, not in the final workbook.
3. The build you are given: production, staging, or a release candidate. A staging build may show unlaunched features that must not enter Phase 1.
4. Any existing analytics access (GA4 property, Firebase project, dataLayer). Existing events are the cheapest evidence you will ever get.

Set the app to the language most of the user base actually uses. On an Arabic-first product, walking the English build gives you a different surface inventory: different empty states, different string lengths that hide or reveal controls, and sometimes entirely different components in right-to-left layout.

## The universal journey checklist

This applies to any app in any industry. The nouns change (vendor, listing, course, policy, ticket) but the shape does not. Walk them in this order, because each one leaves you in the state the next one needs.

**1. First open and onboarding.** Install fresh, or clear app data, so you get the true first-run experience. Capture the splash, every onboarding slide, the language picker, the permission prompts (location, notifications, tracking) and, crucially, what happens when you deny each one. A denied location permission usually produces a completely different home screen, and that fallback path is where the drop-off lives.

**2. Auth, and every gate a signed-out user hits.** Walk the whole app signed out first. Note precisely which action triggers the login wall: browsing, adding to cart, viewing a saved list, or only checkout. Then walk sign-up, sign-in, OTP entry, OTP resend, wrong OTP, social sign-in if present, and password reset. Capture the moment after successful auth: does the app return you to what you were doing, or dump you on the home screen? That difference is the whole design of your auth funnel events.

**3. The browse or discovery surface.** The home screen is rarely one surface. Capture each distinct module: banners or carousels, category tiles, curated rows, the main list or feed, the filter and sort controls in both closed and open state, and the state after each filter is applied. Note whether the list is paginated, infinite-scrolled, or fixed. Note position: if a card carries a rank, an event will need it.

**4. Search, including the zero-result state.** Capture the empty search field, the recent or suggested terms, the type-ahead suggestions mid-query, the results, and then deliberately search for nonsense to capture the zero-result screen. Zero-result search is one of the highest value events in most plans and it is the one people forget to screenshot. Also try a term that returns results in one vertical only, and a term with a typo, to see whether the app does correction or synonym matching.

**5. The detail view.** The item, listing or vendor page. Capture the header, the tabs or sections, the variant and option pickers in both closed and open state, the reviews block, the share control, the favourite or save control, and the add or commit button in both enabled and disabled state. If the app has more than one vertical, walk the detail view in every vertical. They are frequently different products wearing the same brand.

**6. The cart or equivalent commitment step.** Empty cart, cart with one item, cart with items from two sources if that is allowed, quantity increase, quantity decrease to zero, remove, promo code field with a valid code and an invalid code, and every blocking rule (minimum order value, unavailable item, closed vendor, out of delivery range). Capture each blocking dialog exactly as it appears and note which action triggered it.

**7. The checkout or conversion flow, every branch.** Address selection and address creation, delivery or collection choice, scheduled versus immediate, tip, notes, and every payment option the app offers, each one opened. Capture the summary screen and the final confirm button. Do not press it. What you can legitimately capture stops at that button, and everything past it is a hypothesis until the client confirms it.

**8. The post-conversion lifecycle.** Order tracking, status changes, driver or fulfilment updates, chat with support or courier, modify, cancel, reorder, rating and review, refund request. On a test account with history you can often reach the read-only versions of these from the orders list even without transacting. If you cannot, this whole block is unreachable and goes in `unreachable.md`.

**9. Account and settings.** Profile edit, saved addresses (add, edit, delete flow up to the confirm dialog), payment methods, notification preferences, language, wallet or credit balance, loyalty tier, referral, subscription or paid tier, delete account (open it, never confirm it). Settings toggles are cheap, high-signal events that almost every plan under-specifies.

**10. Support.** Help centre, FAQ articles, contact channels, ticket creation form, live chat entry point. Note whether support is in-app or a web view, because a web view usually means the events must be planned for a different property.

**11. Notifications and messaging.** In-app inbox, badge counts, push permission prompt, and any deep link you can trigger. On Android you can fire a deep link directly with `adb shell am start -a android.intent.action.VIEW -d "<uri>"` and see exactly where it lands, which tells you what the campaign attribution events must carry.

**12. Empty, error and blocked states.** Nobody checks these and they are where instrumentation gaps hide. Deliberately produce: no network (aeroplane mode), slow network, empty cart, empty order history, empty favourites, empty address book, session expired, location outside service area, app version forced-update, and a server error if you can provoke one. Each of these is a surface a real user hits, and each usually has no event at all today.

## Working systematically

**Screenshot every distinct surface, not every tap.** A surface is distinct when what the user can do changes. A modal over a screen is a distinct surface. A list scrolled by 200 pixels is not.

**Name files so they sort in journey order:** `SCR-nn_what-it-shows.png`, zero-padded, sequential across the whole walkthrough rather than restarted per journey. `SCR-34_cart-minimum-order-dialog.png` tells a reader what it is without opening it, and the number lets an event reference "SCR-34" forever. Do not rename files after the fact, because the workbook will already point at them.

**Log two columns for every surface: what the user sees, and what the app does.** The second one is the part people skip. "Cart screen showing two items, subtotal 18.00, a red banner saying minimum order is 25.00" is what the user sees. "Banner appears immediately on cart open when subtotal is under the vendor minimum, and the checkout button is disabled until it clears" is what the app does. Only the second sentence tells you where the event fires and what condition it carries.

**Write down the firing moment, in words, at the time.** Not "cart_viewed" but "fires when the cart screen becomes visible, including when returning from checkout via back". Firing moments reconstructed from memory a week later are how duplicate and mis-timed events get specified.

**Record every enum value you see, and mark the ones you suspect are incomplete.** If a payment list shows three options and the list is scrollable, you have three of an unknown number. Write "3 seen, list scrollable, count unconfirmed" rather than treating three as the enum.

**Note the entry points into each surface.** The same detail screen reached from search, from a banner and from a reorder button needs a source parameter, and you can only know the values by walking each route.

## Driving each platform

### Android emulator via adb

Launch and wait for a real boot rather than sleeping a fixed number of seconds:

```bash
emulator -avd demo_device -no-snapshot-load &
adb wait-for-device
adb shell 'while [[ -z $(getprop sys.boot_completed) ]]; do sleep 1; done'
adb install -r /path/to/app.apk
adb shell monkey -p com.example.app -c android.intent.category.LAUNCHER 1
```

Grant permissions up front when you want to skip the prompt, but walk the deny path at least once first:

```bash
adb shell pm grant com.example.app android.permission.ACCESS_FINE_LOCATION
adb emu geo fix 36.2765 33.5138     # longitude first, then latitude
```

Longitude comes first in `geo fix`. Getting it backwards drops you in the sea and the app shows an out-of-service-area state that you may mistake for a bug.

Interaction:

```bash
adb shell input tap 540 1720
adb shell input swipe 540 1600 540 700 300
adb shell input text 'pizza'                 # spaces must be %s
adb shell input keyevent 66                  # enter; 4 is back
adb exec-out screencap -p > SCR-12_search-results.png
```

Stop guessing coordinates. Dump the view hierarchy and read the exact bounds:

```bash
adb shell uiautomator dump /sdcard/ui.xml && adb pull /sdcard/ui.xml
```

This also gives you element text, which is more reliable for capturing enum labels than reading pixels off a screenshot.

**The hw.keyboard gotcha.** If the AVD has `hw.keyboard=no` in its `config.ini`, `adb shell input text` silently does nothing. No error, no typed characters, and you will waste twenty minutes assuming the field is broken. Set `hw.keyboard=yes` and cold boot the device. Separately, `input text` cannot send Arabic or any non-ASCII string. For those, either paste through the clipboard or tap the on-screen keyboard, and accept that a Latin-script test query may not exercise the same search path.

**Read the existing events while you are in there.** This is the highest-value ten minutes of any Android walkthrough, because it converts guesswork into observation:

```bash
adb shell setprop debug.firebase.analytics.app com.example.app
adb logcat -s FA FA-SVC
```

Every event the app already fires, with its parameters, scrolls past as you tap. That tells you what exists, what is misnamed, and what fires twice.

### iOS simulator

```bash
xcrun simctl list devices
xcrun simctl boot "iPhone 16"
open -a Simulator
xcrun simctl install booted /path/to/App.app
xcrun simctl launch booted com.example.app
xcrun simctl location booted set 33.5138,36.2765   # latitude first here
xcrun simctl io booted screenshot SCR-12_home.png
xcrun simctl openurl booted "myapp://order/123"
```

Note the coordinate order flips between adb and simctl. There is no `simctl input`, so taps, swipes and typing go through the simulator control tooling available in the session, using device points with the origin at the top left. Confirm the point dimensions once at launch and reuse them, because a screenshot's pixel size is usually two or three times the point size and mixing the two puts every tap in the wrong place.

### Web

Drive the browser with automation rather than a human. Read the accessibility tree instead of relying on screenshots for text: it gives you exact labels, exact option lists, and disabled states, which is precisely where clipped screenshots mislead you. Take screenshots as well, because the workbook needs the visual evidence, but take enum values from the tree.

Two web-only advantages worth using every time. First, inspect `window.dataLayer` and the network calls to `google-analytics.com/g/collect` as you walk: you see the current implementation live, including parameter values, which grades a lot of events OBSERVED that would otherwise be INFERRED. Second, walk at mobile viewport as well as desktop, because responsive layouts routinely hide or collapse whole modules, and a module that only exists on one breakpoint needs that noted.

### Figma, for pre-release designs

Use the Figma MCP to read frames, flows and prototype links. Two hard rules.

Everything derived from Figma is INFERRED at best. A frame proves an intention, not a behaviour, and it says nothing about whether the backend can source a field on that screen.

Frames are not surfaces. Designers duplicate frames for annotation, leave dead variants in the file, and rarely draw the error and empty states. Ask which frames are current, and treat every missing state as a question for the team rather than a screen that does not exist.

## What you can and cannot verify without transacting

Be explicit about this, in writing, in the workbook. The ceiling is real and it is always in the same place.

Without placing a genuine order, paying real money, or subscribing to a paid tier, you cannot verify: the confirmation screen and its contents, payment success and failure branches, order status transitions, driver or fulfilment updates, delivery completion, cancellation by either side, refunds, post-order rating and review, reorder from a real order, loyalty accrual, wallet debits and credits, and anything behind a paid tier. On the reference engagement that is exactly where the damage happened: roughly forty parameter enum values were invented rather than observed, and every one of them sat downstream of a checkout button that was never pressed.

There are three legitimate ways past the ceiling, in order of preference: a client-provided sandbox or test payment method, a client-provided account with real order history that lets you read the post-order screens without creating one, or a screen-share session where a client operator drives a real order while you capture. If none is available, say so plainly, grade every downstream event UNVERIFIABLE, and put the confirmation of those enums on the client's implementation checklist. An unverifiable event with a stated question is useful. An unverifiable event dressed as a specification is a bug that ships.

Unlaunched features are the same problem in a different coat. If the build shows a subscription tab that has not launched, it cannot be OBSERVED and it cannot be Phase 1.

## Safety and etiquette

Never place a real order. Never complete a payment, including cash on delivery, because a cash order dispatches a real driver to a real address and costs the client money and goodwill.

Never enter credentials on the user's behalf. If a login is needed, ask the client to sign the test device in, or ask the user to type it themselves.

Never submit a form that reaches another human: support tickets, chat messages to a vendor or courier, ratings on a real order, referral invitations. Compose them, screenshot the composed state, and stop at send.

Confirm before anything that costs money, is visible to other people, or cannot be undone. Deleting a saved address on a live account, cancelling an order, and deleting the test account all qualify. Open the dialog for the screenshot, then close it.

Clean up afterwards: remove test addresses you added, clear items from the cart, remove any favourites you set, and tell the client exactly what you touched. If you triggered anything visible on their side, such as a support ticket or an abandoned cart notification, say so before they find it.

## The traps that produced wrong plans

Each of these came from a real walkthrough that produced a plan that had to be redone.

**The picker that was opened but never used.** The address picker was opened, screenshotted and closed. The event that matters fires on selection, not on open, and the list of address types was never captured. Opening a control proves it exists. Only using it shows the resulting state, the values it can return, and whether the screen behind it changes. Always complete at least one selection in every picker, dropdown and date control.

**The enum read from a clipped screenshot.** A payment list showed three methods in the visible area and the plan shipped with three enum values. The list scrolled. Two more existed. Whenever a list can scroll, scroll it to the end, or read the values from the view hierarchy or accessibility tree rather than from pixels.

**The flow that behaves differently signed out.** Browsing and search worked signed out, so the whole walkthrough was done signed in and the auth wall was never seen in context. In reality the login gate fired at add-to-cart, not at checkout, and after login the user was returned to the home screen rather than the cart. Two events and the entire shape of the auth funnel were wrong. Walk the app signed out first, always, and note the exact action that triggers the wall.

**A vertical with a completely different item model.** The plan was designed on the restaurant vertical, where a dish has a detail screen with options. The grocery vertical had no detail screen at all: items are added straight from the grid, quantity is set inline, and there is no options step. An item-view event designed for restaurants simply does not exist in grocery, and the item identifier means a different thing in each. If an app has more than one vertical, category or content type, walk each one end to end and compare the item models explicitly before writing a single shared event.

**A blocking dialog at the wrong step.** The minimum-order dialog was assumed to fire at checkout. It actually fires when the cart opens. Placing that friction event at checkout put the modelled drop-off one step later than the real one, which would have sent the team optimising a screen that was not the problem. When you see a blocking rule, record which action triggered it and re-trigger it once to confirm.

**The button that was never pressed.** Covered above, and worth repeating as a trap rather than a limitation, because the failure is not that checkout was unreachable. The failure is that the plan did not say so. Grade it, declare it, and hand the client the list of enums to confirm.

Two smaller ones worth watching. Time-dependent surfaces: walking at night when every vendor is closed gives you the closed state and none of the open ones, so check at least one surface in both conditions. And identical-looking screens with different entry points: the same list reached from a banner and from a category tile needs a source parameter, and if you only ever arrive one way you will never know the parameter is needed.

## Closing the walkthrough

Before you move to designing events, produce three artefacts and check them against each other.

The screenshot set, ordered and named, with no gaps in the numbering. The walkthrough log, one entry per surface, each recording what the user sees, what the app does, and the firing moments you noticed. And `unreachable.md`, listing every surface you could not reach, why, and what would unblock it.

Then do one pass over the journey checklist above and mark each of the twelve journeys as fully walked, partly walked, or not reachable. That mapping is what sets the evidence grade on every event you are about to write. An event whose surface appears in the screenshot set and whose firing moment appears in the log is OBSERVED. An event whose surface was seen but whose branch was never exercised is PARTIAL. Everything else is INFERRED or UNVERIFIABLE, and the grade is not a formality: it is the difference between a plan a team can build and a plan that quietly instructs them to build fiction.
