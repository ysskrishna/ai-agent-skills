---
name: analytical-thinking
description: >
  Decompose problems, define metrics and hypotheses, structure evidence, and
  synthesize findings with explicit uncertainty. Use when the user asks for
  analytical thinking, structured breakdowns, quant reasoning framing,
  root-cause trees, or decision tables — not pure brainstorming or ethics-first
  deliberation alone.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.5.17"
---

# Analytical Thinking

Clarity beats cleverness. End with answers tied to structure and stated confidence.

---

## When to Use

Use for problems that benefit from decomposition: metrics, prioritization, debugging complex situations, business case structure, research planning. Skip when the user only wants empathy or creative divergence without measurement framing.

---

## Setup (run before starting)

In one short block:

1. **Analytical question** — precise, ideally falsifiable
2. **Default pass** — Frame → Decompose → Hypotheses → Evidence → Synthesis (state this line)

Up to 3 questions on data availability and definitions; otherwise tag `[ASSUMED]` for baselines.

If the user is **choosing among concrete alternatives**, after **Evidence** insert **Options matrix**: rows = options, columns = criteria (state weights if any), qualitative scores (− / 0 / + or 1–5) with one-line justification per cell — then finish with **Synthesis**.

---

## The Steps

### Frame

**Question type** (estimate, compare, explain, predict, optimize). **Unit of analysis** and **baseline** (even if hypothetical).

### Decompose

Tree or table: factors, drivers, or workstreams. Each child node should be **MECE-ish** (mutually exclusive where it matters; collectively exhaustive enough for the decision).

### Hypotheses

Ranked **H1, H2, H3** — what would we expect to observe if each were true? What would **falsify** each?

### Evidence

For each hypothesis: **Observation:** … — **Strength:** Strong / Moderate / Weak — **Caveat:** …

If no real data, run a **thought experiment** section instead — label bullets `[THEORETICAL]`.

### Synthesis

1. **Answer** — direct response to the analytical question
2. **Key uncertainty** — what single unknown swings the answer most
3. **Next data / step** — what to collect or run next

---

## Execution Rules

1. Do not conflate **Hypotheses** and **Evidence** in the same bullet list.
2. Numbers: if inputs are guessed, show **ranges** and label `[ESTIMATED]`.
3. Prefer **structure** over long prose.

---

## Checklist (verify before responding)

- [ ] Setup: analytical question + default pass (note if Options matrix used)
- [ ] Frame states question type and baseline
- [ ] Decompose is scannable (tree or table)
- [ ] Hypotheses have falsifiers
- [ ] Evidence (or `[THEORETICAL]`) mapped to hypotheses
- [ ] Synthesis: answer, uncertainty, next step
