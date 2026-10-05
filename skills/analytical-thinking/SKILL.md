---
name: analytical-thinking
description: >
  Use for analytical thinking, or when a question needs breaking down and evidence: "why did metric X drop?", "what drives this?", "break this down", "what data do we need?". Builds a tree, hypotheses and evidence, ends with an answer and key uncertainty. Skip for quick verdicts.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.10.5"
---

# Analytical Thinking

Clarity beats cleverness. End with an answer tied to structure and a stated confidence.

## When to use

- Explaining or predicting a number: a metric moved, a cost is high, a funnel leaks.
- A messy question that needs a driver tree, hypotheses and a plan for what data to collect.
- Comparing concrete alternatives against criteria when the user wants the reasoning laid out.

Skip: open-ended idea generation with nothing to measure, or a short verdict with no decomposition asked for.

## Before you start

1. State in one block: **Analytical question** (precise, ideally falsifiable) and **Pass** (Frame, Decompose, Hypotheses, Evidence, Synthesis).
2. **Gather first.** If you can query data, read dashboards, logs or code, do that before listing Evidence. Ask up to 3 questions only for definitions or data that tools cannot supply.
3. **Light path.** Small ask: a 2-level tree, 2 hypotheses, one observation each, answer in 3 lines.
4. If the user is choosing among concrete options, insert an **Options matrix** after Evidence: rows are options, columns are criteria (state any weights), cells are `-`, `0` or `+` with a one-line reason. Then Synthesis.

## Steps

### 1. Frame
**Question type** (estimate, compare, explain, predict, optimize), **unit of analysis**, and **baseline** (even a hypothetical one).

### 2. Decompose
A tree or table of drivers or workstreams. Aim for branches that do not overlap and together cover the question well enough for the decision.

### 3. Hypotheses
Ranked H1, H2, H3. For each: what would we see if it were true, and what would **falsify** it?

### 4. Evidence
For each hypothesis: **Observation:** ... - **Strength:** one sentence on how much it supports or undermines the hypothesis and its main limit. **Caveat:** ...

No real data? Replace this step with a section titled **Thought experiment (no data)**. Inputs you guess are shown as ranges and marked `[ESTIMATED]`.

### 5. Synthesis
1. **Answer** to the analytical question.
2. **Key uncertainty:** the one unknown that swings the answer most.
3. **Next data or step:** what to collect or run next.

## Pitfalls

- Mixing Hypotheses and Evidence in one list. Keep them separate.
- Reading a pattern from a few data points. State sample size or window.
- Ignoring base rates (how often this happens anyway) and confounders (what else changed).
- A single point estimate from guessed inputs. Use ranges and show which input moves the result most.
- A tree whose branches overlap, so the same cause is counted twice.

Worked example: [references/example.md](references/example.md).

## Checklist

- [ ] Question and Pass stated (Options matrix noted if used)
- [ ] Frame gives question type and baseline
- [ ] Decompose is scannable
- [ ] Hypotheses have falsifiers
- [ ] Evidence (or Thought experiment) maps to hypotheses; guesses marked `[ESTIMATED]`
- [ ] Synthesis: answer, key uncertainty, next step
