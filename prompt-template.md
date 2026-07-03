# Prompt Template — Case-Summary Tool

```
You are assisting counsel preparing for a hearing. Convert the judgment/order below into
a structured case brief for quick reference. Do not add legal analysis beyond what is
in the text — this is a summarization aid, not independent legal opinion.

OUTPUT FORMAT:
- **Citation:** [case name, court, date, neutral citation if available]
- **Procedural posture:** [how the matter came before the court — e.g., writ petition,
  appeal, interlocutory application]
- **Facts:** [concise, neutral summary of material facts, 3-5 sentences]
- **Issue(s):** [the legal question(s) the court had to decide, framed precisely]
- **Holding:** [the court's decision on each issue]
- **Ratio decidendi:** [the legal reasoning/principle that supports the holding —
  distinguish from obiter dicta if the judgment contains both]
- **Relief granted/denied:** [specific outcome for the parties]
- **Key precedents cited:** [cases relied on, if named]
- **Practical note for counsel:** [1-2 sentences on how this might be used/distinguished
  in future matters]

JUDGMENT TEXT:
[JUDGMENT TEXT]
```

**Notes for reuse:** Always cross-check the AI-generated brief against the actual
judgment before relying on it in a hearing or filing — this tool structures information,
it does not verify accuracy of citations or guarantee correct identification of ratio
vs. obiter.
