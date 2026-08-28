# Survey methods

**The rule that governs everything below: never run a survey before qualitative work.**
A survey can only measure what you already thought to ask, in the words you already thought
to use. Written before the interviews, it measures your assumptions with impressive
precision.

Surveys produce **stated preference**, L2 on the evidence ladder. They tell you what to
test. They do not settle decisions.

---

## Choosing an instrument

| Question | Instrument | Minimum n |
|---|---|---|
| How common is this behaviour? | Prevalence survey with a defined frame | 200+ for a population read |
| Which attributes are expected vs which delight? | Kano | 100 |
| What is the relative value of these attributes? | MaxDiff | 200 |
| What trade-offs will people make, including price? | Conjoint | 250+ |
| What price range is credible? | Van Westendorp | 100 |
| At what price does intent fall off? | Gabor-Granger | 100 |
| Would this segment miss us? | Sean Ellis PMF | 40+, ideally 100 |
| What happened in that specific moment? | In-product intercept | context-dependent |

Scoring for all of these: `scripts/survey_analysis.py`.

---

## Sampling

**The sampling frame is the survey.** Everything else is detail.

State in one sentence: who could possibly have received this, who actually did, and who
responded. Then state who is missing.

**Non-response bias is usually larger than the effect you are measuring.** People who
answer surveys differ systematically from people who do not: more engaged, more opinionated,
more time. A 4 percent response rate to a satisfaction survey tells you about the 4 percent.

**Mitigations:** compare respondent characteristics to the full population on variables you
have, report the response rate always, and never generalise beyond the frame.

**Panels** buy speed and cost representativeness. Professional respondents learn to qualify
for studies. Always include a disqualifying distractor in the screener and an attention
check in the body.

---

## Question design

| Fault | Example | Fix |
|---|---|---|
| Leading | "How useful is the new dashboard?" | "How would you describe the new dashboard?" |
| Double-barrelled | "Is it fast and reliable?" | Two questions |
| Presupposing | "What frustrates you about X?" | "What is your experience of X?" |
| Asking about the future | "Would you use...?" | "When did you last...?" |
| Asking for a frequency estimate | "How often do you...?" | "When was the last time? And before that?" |
| Jargon | "How satisfied are you with our onboarding funnel?" | Use their words, taken from interviews |
| Absolute scale with no anchor | "Rate importance 1-5" | Force a trade-off instead (MaxDiff) |
| Acquiescence-prone | Long agree/disagree batteries | Mix directions, keep batteries short |

**Order effects are real.** Early questions frame later ones. Randomise item order within
a battery, and put demographics last so they do not prime identity.

**Scale points.** Five or seven, labelled at every point, with a neutral midpoint only when
neutral is a real position. Never average the result; report the distribution and top-2-box.

---

## Instrument notes

**Kano.** Functional and dysfunctional pairs per attribute, mapped to the Kano table. Cap
at about ten attributes; respondents tire and the later answers degrade. Categories decay
over time: today's attractive attribute becomes tomorrow's must-be, so rerun annually in a
moving category. A high "questionable" count on an attribute means the question was
misunderstood; discard that attribute rather than interpreting it.

**Van Westendorp.** Four price questions produce a range of acceptable prices, not a price.
Exclude internally inconsistent responses (prices not in ascending order). Requires that
respondents genuinely understand what they are pricing, which is why it fails badly on
novel products. Use the output to choose which prices to test with commitment.

**Gabor-Granger.** Purchase intent at a series of price points, producing a demand curve
under stated intent. Deflate heavily. Stated intent runs well above behaviour, and the gap
is not a constant you can subtract.

**MaxDiff.** Best-worst scaling. Better than rating scales because respondents must give
something up. Counting analysis is enough for a ranking; hierarchical Bayes is worth it only
when you need individual-level utilities for segmentation.

**Conjoint.** Trade-offs across attribute bundles including price. The strongest
stated-preference instrument and the most expensive to design well. Attribute levels must
be realistic and mutually exclusive, and a badly specified attribute list invalidates the
whole study.

**PMF survey.** Only among users who have experienced core value at least twice. The signal
is the composition of the "very disappointed" group, not the headline percentage.

---

## Open-text questions

The most valuable part of most surveys and the most often ignored.

- One or two, placed before the closed questions on the same topic so the options do not
  prime the answer
- Analyse them with the coding protocol in `discovery-synthesis`, not by skimming
- Report source counts per code
- They are the bridge back to qualitative: the language people use in open text is what
  your next interview guide should use
