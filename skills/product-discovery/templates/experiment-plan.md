# Experiment pre-registration: [name]

Written: [YYYY-MM-DD] · Owner: [ ] · Reviewed by: [ ]
**Shared before launch. Any change after launch is an amendment below, with a reason and a
timestamp. Not a silent edit.**

## Hypothesis
[Specific, directional, falsifiable.]

## Primary metric (exactly one)
Name: [ ]
Definition: [event, window, population, exclusions]
Direction: [increase / decrease]

## MDE
Smallest effect worth acting on: [ ]
Derived from: [the business case, not from what the sample can detect]

## Guardrail metrics
| Metric | Threshold that stops the rollout |
|---|---|
| | |

## Secondary metrics (exploratory, corrected or labelled)
[ ]

## Design
Unit of randomisation: [user / session / account / geo / time block]
Why that unit: [interference reasoning]
Allocation: [50/50]
Eligibility: [ ]
Exclusions, defined now: [ ]

## Sample and duration
n per group: [ ] · Calculation: [alpha, power, baseline, MDE]
Daily eligible: [ ] · Planned duration: [dates, whole weeks]
Stopping rule: [fixed horizon / sequential method / K looks with correction]

## Analysis
Test: [ ] · Alpha: [ ] · Multiple comparison handling: [ ]
Pre-launch checks: A/A test [yes/no] · SRM check before reading [yes]

## Decision rules
SHIP IF: [ ]
DO NOT SHIP IF: [ ]
INCONCLUSIVE IF: [ ]

## Threats to validity
Interference: [ ] · Novelty: [ ] · Seasonality: [ ] · Concurrent changes: [ ]

## Ethics
Could either arm be harmed: [ ] · Harm guardrails: [ ] · Immediate-stop conditions: [ ]

## Amendments
| Date | Change | Reason |
|---|---|---|
