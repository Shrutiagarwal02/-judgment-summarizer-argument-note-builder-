"""
Judgment Summarizer & Argument Note Builder — Static Showcase

This is a STATIC showcase, not a live tool: it displays pre-run prompts, sample
inputs, and real outputs already produced and verified. It does not call any LLM
API and accepts no user input beyond navigation, by design — no cost exposure, no
reliability risk, and no ambiguity about what's "live" vs. demonstrated.
"""

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Judgment Summarizer & Argument Note Builder",
    page_icon="\U00002696",
    layout="wide",
)

ROOT = Path(__file__).parent

FILES = [
    ("Overview", "README.md"),
    ("Prompt", "prompt-template.md"),
    ("Sample Judgment", "sample-judgment.md"),
    ("Output", "sample-output.md"),
    ("Real Example — Calcutta HC Judgment", "real-example-jindal-v-wb.md"),
    ("Argument Note Extension", "argument-note-extension.md"),
    ("CV Summary", "cv-summary.md"),
]


def load(rel_path: str) -> str:
    p = ROOT / rel_path
    if not p.exists():
        return f"*(file not found: {rel_path})*"
    return p.read_text(encoding="utf-8")


st.title("Judgment Summarizer & Argument Note Builder")
st.caption("Shruti Agarwal — Litigation & Dispute Resolution Practice")

st.info(
    "**This is a static showcase, not a live demo.** Every prompt, sample, and "
    "output below was actually run and is displayed as-is — nothing here calls an "
    "AI model live.",
    icon="ℹ️",
)

tabs = st.tabs([label for label, _ in FILES])
for tab, (label, filename) in zip(tabs, FILES):
    with tab:
        st.markdown(load(filename))

st.sidebar.markdown("### About")
st.sidebar.markdown(
    "Converts a judgment into a structured case brief (facts, issues, holding, "
    "ratio decidendi vs. obiter dicta), then organizes multiple briefs into an "
    "argument note for a hearing."
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "[LinkedIn](https://www.linkedin.com/) &nbsp;|&nbsp; "
    "shrutiagarwal.new@gmail.com"
)
