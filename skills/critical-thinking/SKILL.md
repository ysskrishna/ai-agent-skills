---
name: critical-thinking
description: >
  Critical thinking: clarify claims, weigh evidence, surface assumptions,
  test logic for gaps and fallacies, scan biases, stress-test conclusions.
  Use when the user asks for critical thinking, a belief or argument audit,
  decision-quality review, devil's advocate, steel/straw man check, bias or
  fallacy scan, red-team, "what am I missing", logical stress-test, or
  epistemic or confidence calibration. Skip for execution-only tasks with no
  evaluative angle.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.5.18"
---

# Critical Thinking

**Critical thinking** is disciplined inquiry that keeps **description** separate from **evaluation**: surface assumptions, weigh evidence, test logic, consider alternatives, then state a proportionate conclusion. If the conventional view is well-supported, say so — this is inquiry, not contrarianism by default.

**How to run it with this skill:** one phase per clearly headed section, in the order stated in Setup (default pass unless the user requested otherwise); always close with **Conclusion** (judgment, confidence, falsifiers) unless the user explicitly stops early.

---

## Setup (run before starting)

In one short block:

1. **Focus** — the specific claim, proposal, or question under review
2. **Default pass** — Clarify → Information → Assumptions → Reasoning → Alternatives → Conclusion (state this line so the user sees the path)

If essential context is missing, ask at most 3 questions in one message, then proceed. Note any remaining gaps or working guesses in plain language (no bracket tags in Setup).

If the user asks to **skip or reorder** phases (e.g. fast logic-only pass), follow their sequence and still end with **Conclusion**.

---

## The Phases

### Clarify

Restate the target in one precise sentence. Separate **factual** vs **normative** claims. Name success criteria if a decision is involved.

### Information

What evidence exists? Each bullet starts with **`[CITED]`** or **`[MISSING]`**:

- **`[CITED]`** — a traceable basis (user text, repo, doc, link, study, etc.); in the same bullet, name the basis and one line on strength or limits (no extra strength tags).
- **`[MISSING]`** — no traceable basis yet for that point, or evidence was requested but not available.

### Assumptions

List tacit premises. For each: **Assumption:** … — **If false:** …

### Reasoning

Trace the argument chain. Flag **leaps**, **circular** patterns, **correlation vs causation**, and **missing steps**. No new factual assertions here — only structure.

**Bias and fallacy pass (compact):** add a short sub-list — only items that apply; omit the rest rather than padding.

- **Biases to scan:** confirmation; anchoring; survivorship; undue authority; sunk cost — plus any other bias clearly relevant to the case.
- **Fallacies to name if present** (tie each to the chain above): ad hominem; straw man; false dichotomy; slippery slope; hasty generalization; begging the question.

If none apply, state that plainly in one line.

### Alternatives

Credible competing explanations, plans, or frames. Do not collapse into debate rhetoric; keep alternatives plausible.

### Conclusion

1. **Judgment** — answer the focus question directly
2. **Confidence** — High / Medium / Low with one-line justification tied to how much is `[MISSING]` vs well-supported `[CITED]` evidence
3. **What would change my mind** — concrete falsifiers or new data

---

## Execution Rules

1. Run phases in one response unless the user requests step-by-step pacing.
2. Never merge **Information** and **Reasoning** in the same bullet block.
3. Do not smuggle new unsupported facts into **Conclusion**; only synthesize prior phases.
4. If the user is emotionally fused with a position, name it neutrally and continue the phase plan.
5. Be intellectually honest: acknowledge strong opposing evidence and uncertainty where the phases support it.

---

## Checklist (verify before responding)

- [ ] Setup block: focus + stated pass (or user-requested variant)
- [ ] Each phase is its own section, following the order stated in Setup
- [ ] Information: each bullet starts with `[CITED]` (basis + limits in-bullet) or `[MISSING]`
- [ ] Assumptions use **Assumption** / **If false** pairs
- [ ] Reasoning references only what earlier phases established; bias/fallacy pass done or explicitly "none identified"
- [ ] Conclusion includes judgment, confidence, and falsifiers
