---
name: critical-thinking
description: >
  Use for critical thinking, or when the user wants a claim, plan or decision checked for weak spots: "is this right?", "what am I missing?", "poke holes", "sanity check", "devil's advocate", "red team this". Skip for execution-only tasks and wording edits.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.10.5"
---

# Critical Thinking

Disciplined inquiry that keeps **description** apart from **evaluation**: surface assumptions, weigh evidence, test logic, consider alternatives, then give a proportionate conclusion. If the conventional view is well supported, say so. This is inquiry, not contrarianism.

## When to use

- The user asks whether a claim, argument, plan, estimate or belief holds up.
- Phrases like "what am I missing", "steelman", "red team", "devil's advocate", "bias check", "is my reasoning sound".
- A decision about to be made on thin or one-sided evidence.

Skip: execution-only tasks, wording or tone edits, open-ended brainstorming with no request to audit reasons.

## Before you start

1. State in one block: **Focus** (the claim or plan under review) and **Pass** (Clarify, Information, Assumptions, Reasoning, Alternatives, Conclusion).
2. **Gather first.** If you can read the repo, docs or data, check them before marking anything `[MISSING]`. Ask up to 3 questions only for what tools cannot answer.
3. **Light path.** Small ask: 1-3 lines per phase, same order, Conclusion always included.

## Phases

### 1. Clarify
Restate the target in one precise sentence. Split **factual** from **normative** claims. Name the success criteria if a decision is involved.

### 2. Information
Each bullet starts with `[CITED]` or `[MISSING]`.
- `[CITED]`: name the basis (user text, file, doc, link, study) and one line on its strength or limits.
- `[MISSING]`: no traceable basis yet, or it was requested and not available.

### 3. Assumptions
**Assumption:** ... - **If false:** ...
When the Focus mixes "is" and "should", add **Value premise:** ... - **If rejected:** ...

### 4. Reasoning
Trace the argument chain. Flag leaps, circularity, correlation vs causation, missing steps. Add no new facts here. A premise never established in Information is an **ungrounded premise** (a structural gap, not a fact).

Bias and fallacy pass, only items that apply (or one line saying none):
- Biases to consider (examples): confirmation, anchoring, survivorship, authority, sunk cost.
- Fallacies to name if present: ad hominem, straw man, false dichotomy, slippery slope, hasty generalization, begging the question.

### 5. Alternatives
Credible competing explanations, plans or frames. Keep them plausible, not debate rhetoric.

### 6. Conclusion
1. **Judgment** answering the Focus. When facts and values both matter, separate what follows from the cited evidence from what depends on value premises. End with one plain sentence on how strong the case is given `[CITED]` vs `[MISSING]`.
2. **What would change the judgment:** concrete new data or falsifiers, phrased for the Focus.

## Pitfalls

- Inventing a citation to avoid writing `[MISSING]`. Say it is missing.
- Smuggling new facts into Reasoning or Conclusion.
- Listing every bias in the book. Name only those that bite this case.
- Manufacturing objections to a sound argument. Proportionate beats exhaustive.
- Arguing with a person's position instead of its chain. If the user is emotionally attached, name it neutrally and continue.

Worked example: [references/example.md](references/example.md).

## Checklist

- [ ] Focus and Pass stated
- [ ] Phases in order; Conclusion present
- [ ] Information bullets start with `[CITED]` (basis + limits) or `[MISSING]`
- [ ] Assumptions carry If false (and Value premise when facts and values mix)
- [ ] Reasoning adds no facts; ungrounded premises flagged; bias pass done or "none"
- [ ] Conclusion: judgment, strength sentence, what would change it
