# Judgment Summarizer & Argument Note Builder
*(working name: Case-Summary Tool)*

Built by **Shruti Agarwal** (LL.M., Commercial & Corporate Law, Queen Mary University
of London) — a structured AI prompting workflow that converts judgments into
standardized case briefs, extended into an argument-note builder for hearings.

**Live showcase:** *[add Streamlit Community Cloud URL here once deployed]*

**Validated against real material:** tested against a real, current Calcutta High
Court judgment (*M/S. Jindal (India) Ltd v. State of West Bengal*, July 2025) — see
`real-example-jindal-v-wb.md`, fully verifiable on
[Indian Kanoon](https://indiankanoon.org/doc/139122637/).

**Important:** this is a prompting workflow on a general-purpose LLM (Claude/ChatGPT),
not a fine-tuned model. It organizes precedent and structures arguments — it does not
decide which argument to run or predict how a court will rule; that remains counsel's
judgment. See `cv-summary.md` and `argument-note-extension.md` for the full scope
boundary.

### Running the showcase locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

This is a **static showcase app** — it displays the prompts, samples, and
already-generated outputs below. It does not call any LLM API live.

---

**What it is:** A structured LLM workflow that converts a judgment/order into a
standardized case brief (facts, issues, holding, ratio decidendi, procedural posture) —
formalizing the case-brief work you already do for court hearings and client
conferences.

**Why it matters:** Case briefing is repetitive, high-volume work in litigation practice.
A consistent, structured format makes briefs faster to produce and easier for senior
counsel to scan quickly before a hearing.

## Files

- `prompt-template.md` — the reusable prompt
- `sample-judgment.md` — a synthetic judgment excerpt (writ jurisdiction matter)
- `sample-output.md` — the generated case brief
- `cv-summary.md` — CV line, LinkedIn post, interview talking points
