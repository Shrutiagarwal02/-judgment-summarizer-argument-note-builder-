# Extension — Argument Note Builder

**Repositioning, not a new build:** this extends the case-briefing workflow one step
further — from summarizing a single judgment to organizing multiple case briefs into a
structured argument note for a hearing. Matches the "Judgment Summarizer & Argument
Note Builder" framing.

**Important scope boundary:** this tool organizes precedent and structures arguments —
it does not decide which argument to run or predict how a court will rule. The lawyer
selects which authorities to lead with and how to sequence them based on the specific
bench, opposing counsel, and case posture. Presenting this as "AI legal strategy" would
overstate it in the same way the playbook generator's negotiation framing needed a
boundary — this is organization and drafting support, not judgment substitution.

## Prompt Template

```
You are helping counsel prepare an argument note for a hearing, using case briefs
already prepared (via the case-summary workflow). You are organizing and structuring,
not deciding which argument is strongest — that is counsel's call.

Given the case briefs below and the issue for the hearing, produce:
- **Issue for hearing:** [restate the precise question before the court]
- **Supporting authorities:** [list each brief's citation, holding, and ratio, grouped
  by which sub-argument they support]
- **Anticipated counter-argument:** [what the opposing side is likely to argue, based on
  the facts/issues in the briefs, if apparent]
- **Distinguishing points:** [for any authority that could be read against your
  position, note how it might be distinguished on facts or procedural posture]
- **Suggested structure:** [a logical order to present the authorities — e.g.,
  strongest/most on-point first, or chronological if building a line of reasoning]

Do not state a conclusion on how the court should rule or which argument is strongest
— present the organized material for counsel's judgment.

CASE BRIEFS:
[PASTE ONE OR MORE OUTPUTS FROM prompt-template.md / real-example-jindal-v-wb.md]

ISSUE FOR HEARING:
[STATE THE ISSUE]
```

## Worked Example

Using the real case brief already built in `real-example-jindal-v-wb.md` (*Jindal
(India) Ltd v. State of West Bengal*), applied to a hypothetical hearing issue:

**Issue for hearing:** Whether a tribunal may disregard cross-examination evidence on
a matter not expressly pleaded in the written statement, where the parties otherwise
litigated the substance of that issue.

**Supporting authorities:**
- *M/S. Jindal (India) Ltd v. State of West Bengal* (Calcutta HC, 2025:CHC-AS:1160) — holding that substance prevails over form in pleading-based exclusion; cross-examination evidence should not be disregarded on a technical pleading gap where the parties understood and litigated the issue.
- (In a real matter, additional briefs would be added here from other precedents on point.)

**Anticipated counter-argument:** Opposing counsel will likely argue that pleadings
exist precisely to give fair notice of the case to be met, and permitting evidence on
unpleaded matters undermines that function and risks prejudice.

**Distinguishing points:** If opposing counsel raises a case where a pleading defect
caused genuine prejudice (e.g., surprise evidence with no opportunity to respond),
distinguish on the basis that *Jindal* turned on the parties already having litigated
the substance — no surprise or prejudice was shown there.

**Suggested structure:** Lead with the *Jindal* holding and its "substance over form"
rationale; pre-empt the fair-notice counter-argument immediately after, rather than
waiting for it to be raised, given it's the obvious rejoinder.

## CV / Interview Note

Frame as: "I extended the case-briefing tool one step further into an argument-note
organizer — it structures precedent and anticipates counter-arguments, but doesn't
decide the argument itself. That's still counsel's judgment call, informed by things
the tool doesn't see: the bench, opposing counsel's tendencies, and case-specific
strategy."
