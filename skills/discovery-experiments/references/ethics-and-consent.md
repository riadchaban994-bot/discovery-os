# Ethics and consent

Discovery is done on people. These rules are preconditions, not considerations, and they
apply whether or not a regulator is watching.

---

## Research participation

**Consent** is informed, explicit, and recorded. The participant knows who is collecting,
what for, how it is stored, how long, who sees it, and that they can stop or withdraw
afterwards.

**Recording** needs its own explicit yes, captured on the recording itself.

**Withdrawal** is honoured, including from data already coded. Build the artifacts so this
is possible: a participant code that can be found and removed.

**Data minimisation.** Participant codes in artifacts, never names. The identity mapping
lives separately, with access controlled and a deletion date.

**Incentives** are fair for the time given, disclosed before the session, and never
contingent on what the participant says or on completing "successfully".

**Power imbalance.** Employees, users in a support dispute, people in financial or health
distress, and anyone dependent on your organisation cannot freely decline. Take extra care,
make declining easy and consequence-free, and consider whether the session should happen
at all.

**Vulnerable participants.** Minors need guardian consent. Health, financial distress,
migration status and similar contexts need a considered protocol, not an improvised one.

**Language.** Consent in the participant's strongest language, always. Consent obtained in a
language someone reads poorly is not consent.

---

## Deceptive tests

Fake doors, painted doors, Wizard of Oz and Pinocchio tests involve some concealment. That
is acceptable within limits.

**Permitted:**
- Concealing that a feature is not yet built, provided the user is told immediately on the
  click and no obligation is created
- Concealing that a human is doing the work, provided output quality matches what is
  promised, no sensitive data reaches the operator undisclosed, and the output is **not** a
  clinical, diagnostic, financial, legal or safety judgement. Where it is, this is prohibited
  outright rather than conditional, and shadow mode is the substitute
- Testing a price without building the product, provided nothing is charged, or the charge
  is refunded promptly and this was stated

**Never:**
- Taking real money for something that will not be delivered and not refunding promptly
- Creating a legal or financial obligation the user did not knowingly accept
- Concealing a material safety, health, financial or legal fact
- Testing on people who cannot consent, or in a context where they cannot walk away
- Running any deceptive test in a clinical, safety-critical or statutory-service context.
  Not "without checking the local rule first". Not at all
- Letting a deceptive test run past the decision it was designed to inform

**The honest close is mandatory.** Every deceptive test ends with a truthful message to the
participant, and if they gave you contact details, an actual follow-up when the decision is
made, including when the decision is not to build.

**The public test.** Would you be comfortable if this test were described accurately in a
news report, with your organisation's name on it? If not, redesign it.

---

## Live experiments on users

**Not everything can be A/B tested.**

- **No experiment may knowingly harm the control group or the treatment group.** Degrading
  someone's experience to measure the degradation needs a much higher bar than a normal test,
  and usually a shorter window and a smaller slice.
- **Pricing experiments** must comply with local law on price discrimination and must not
  disadvantage existing customers. Test on new customers, and check the jurisdiction.
- **Safety, health, financial and accessibility features** are not experiment material for
  removal. You can test improvements; you cannot test taking them away.
- **Dark patterns are not experiments.** Testing whether a harder-to-find cancel button
  reduces cancellations will succeed and should not be run.
- **Guardrails must include harm.** Complaints, support contacts, uninstalls, accessibility
  failures, and error rates for the affected group.
- **Stop rules for harm** are absolute and are not subject to the statistical stopping rule.
  If a guardrail breaches badly, stop immediately without waiting for significance.

---

## AI-specific

**Disclosure.** If a model is moderating a session, generating a response the participant
will read, or making a decision about them, they are told.

**Synthetic data never becomes evidence.** See
`../product-discovery/references/07-ai-boundary.md`. The reason is partly integrity and partly
harm: decisions made on invented customer data affect real customers.

**Model-driven features need a bias and exclusion assessment before build:** who is
misclassified, what it costs them, whether they can tell, and what recourse exists.

**Training on research data** requires its own consent. Consent to participate in research
is not consent to be training data.

---

## Data protection

- Establish the lawful basis before the first session, not after
- Store recordings and transcripts in one controlled location with a retention period
- Keep identity mapping separate from research content
- Cross-border transfer rules apply to recordings and transcripts
- In government and regulated contexts, get the relevant sign-off before recruiting, because
  retrofitting it is usually impossible

---

## The ethical assumption

Add this to every assumption map, and answer it in writing before build:

> Who could be harmed by this working exactly as intended?

Not by it failing. By it succeeding. The answer is often nobody, and writing that down after
actually thinking about it is a different thing from never asking.

Follow with: who is harmed if it fails and how would they know; what does the worst-behaved
one percent of users do with it; who is excluded by the rule, the model or the design, and
what recourse do they have; what data does this create, who can see it, and what happens if
it leaks.
