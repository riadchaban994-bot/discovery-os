# Anti-patterns and CHALLENGE mode

Thirty ways discovery produces confident nonsense, and the protocol for red-teaming a plan
or a conclusion.

---

## A. Framing failures

**1. No decision behind the research.** The study runs, the readout is admired, nothing
changes. *Test:* name the decision and the result that flips it. If you cannot, stop.

**2. The question is a solution.** "Should we build a dashboard" cannot be researched, only
confirmed or denied. *Fix:* what job is the dashboard for, and how is that job done today.

**3. Answering a question nobody asked.** Research scoped to what is easy to study rather
than what is blocking. *Test:* who is stuck right now, and does this unstick them.

**4. Discovery after the decision.** The build started, the research is being run to
justify it. *Fix:* say so. Advocacy is legitimate; mislabelled advocacy corrupts the
evidence base for years.

**5. Solving for the loudest customer.** One enterprise account's requests become the
roadmap. *Test:* how many customers have this need, and what is the revenue concentration
risk of building only for one.

**6. The outcome is an output.** "Launch the feature by Q3" is not an outcome. An outcome
is a change in customer behaviour or business result.

---

## B. Sampling failures

**7. Interviewing only current, active users** when the question is about non-adoption or
churn. The people who could answer are the ones who left.

**8. Convenience sampling presented as representative.** Whoever answered the email is not
the market. *Fix:* state the sampling frame in one sentence in every readout.

**9. Survivorship bias.** Studying successful users to learn why users succeed, without
looking at those who did not.

**10. Missing segment.** The sample contains no one from the segment the decision affects
most. *Test:* list who is absent before analysing.

**11. Sample size theatre:** n=500 on a badly-worded stated-preference question beats
nothing but is still L2. Sample size does not upgrade evidence type.

**12. Recruiting for agreement.** Screening out sceptics, or recruiting from the
enthusiast community, then reporting enthusiasm.

---

## C. Instrument failures

**13. Leading questions.** "How frustrating is the current process?" presupposes
frustration. *Fix:* "Walk me through the last time you did it."

**14. Asking about the future.** Intent predicts behaviour weakly, and worst for
discretionary purchases. Downgrade to L2 and act accordingly.

**15. Pitching in an interview.** Once you describe your idea, everything afterwards is
politeness. Show solutions last, always, after the story is collected.

**16. Feature voting.** Ranking a list measures how vividly each item was described.
*Fix:* trade-offs (MaxDiff, conjoint) or commitment.

**17. Survey before qualitative.** The questions encode the author's assumptions, so the
answers confirm them.

**18. Double-barrelled and loaded items.** "How satisfied are you with the speed and
reliability?" cannot be answered.

**19. Scale abuse.** Averaging Likert responses and reporting one decimal place. Report
distributions.

**20. The moderator rescues the participant.** Every rescue destroys the finding. Let the
silence run.

---

## D. Analysis failures

**21. Confirmation coding.** Codes are created to match the hypothesis; disconfirming
segments get coded as edge cases. *Fix:* code before forming the conclusion, and have a
second coder on a sample.

**22. Percentages from small n.** See Constitution rule 9.

**23. Cherry-picked quotes.** Three quotes that support the point, from a corpus that
contains twelve that do not. *Fix:* report how many segments carry each theme, out of how
many sources.

**24. Simpson's paradox.** The aggregate moves while every segment holds. The mix changed.
Check segment mix on every aggregate movement.

**25. Correlation dressed as cause.** "Users who use feature X retain better, so let's
push X." Users who choose X are different from users who do not, in ways that also cause
retention. *Fix:* an experiment, or say "associated with".

**26. Averaging away the finding.** The mean hides a bimodal distribution where two
segments behave oppositely. Always look at the shape.

**27. Multiple comparisons.** Testing twenty metrics and reporting the one that reached
significance. *Fix:* pre-register the primary metric, correct the rest, or label them
exploratory.

**28. Peeking.** Watching a running experiment and stopping when it looks good.
Dramatically inflates false positives. *Fix:* fixed horizon, or a sequential method
designed for continuous monitoring.

**29. Ignoring the null.** A negative result is a finding, and the most valuable one, since
it prevents spend. Publish it with the same care as a positive.

**30. Novelty and primacy effects.** Early experiment results move because the change is
new, not because it is better. Run long enough to see the effect settle.

---

## E. Organisational failures

**31. The research repository nobody reads.** Findings are filed and re-discovered a year
later. *Fix:* a one-page living summary per outcome, plus decision records that cite
evidence ids.

**32. Handoff discovery.** A researcher discovers, a PM writes a spec, engineers build. The
learning does not travel. *Fix:* the trio attends the sessions.

**33. Insight without owner.** A finding with no name against it changes nothing.

**34. The quarterly research project.** Discovery batched into a phase, so the answer
arrives after the commitment.

**35. Metrics chosen for reportability.** Vanity metrics survive because they always go up.
*Test:* can this metric go down if we do a bad job.

---

## CHALLENGE mode protocol

When asked to review a plan, a conclusion, or a document, work in this order and report
findings ranked by how much each would change the answer. Do not report everything; report
what matters.

**1. The decision test.** What decision does this change? What result would flip it? If no
answer, that is finding number one.

**2. The evidence test.** For each load-bearing claim: level, source, sample, date. Which
claims are doing the most work and have the least support?

**3. The alternative-explanation test.** For each causal or directional claim, generate the
two strongest competing explanations. Seasonality, mix shift, selection, measurement
change, concurrent release, external event, regression to the mean.

**4. The absent-evidence test.** Who is not in this sample? What would the missing segment
say? What data was available and not used?

**5. The inversion test.** Assume the conclusion is wrong. What would the world look like?
Is any of that visible in the data already?

**6. The method-fit test.** Can the method used actually answer the question asked? This
catches more errors than anything else on the list. Surveys asked to explain why. Interviews
asked to establish prevalence. Before-and-after asked to establish cause.

**7. The stopping test.** Was the analysis stopped when it reached a convenient answer?
Was the experiment stopped on a good day? Was the interview stopped when the participant
agreed?

**8. The incentive test.** Who benefits from this conclusion? Not an accusation, a
calibration. Findings that cut against the author's interest deserve more weight, and
findings that flatter it deserve a harder look.

**Report format:**

```
## Challenge: [artifact]

Would change the answer:
1. [finding]: [why it changes the conclusion]: [cheapest way to resolve]

Worth fixing, would not change the answer:
- ...

Holds up:
- [say this explicitly. A challenge that lists only problems is not calibrated and will
  be discounted wholesale]
```

Always include the "holds up" section. A red team that never confirms anything gets
ignored, and being ignored is worse than being wrong.
