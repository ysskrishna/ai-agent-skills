---
name: critical-thinking
description: >
  Structured critical inquiry: clarify claims, surface assumptions, weigh
  evidence, test logic, and stress-test conclusions. Use when the user asks for
  critical thinking, rigorous evaluation of an argument, a belief audit,
  decision quality review, or explicit devil's-advocate analysis without
  needing a full multi-framework workshop.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.5.17"
---

# Critical Thinking

One lens at a time. Separate description from evaluation. End with a calibrated conclusion.

---

## When to Use

Use when the user wants sharper reasoning about a claim, plan, or document — e.g. "think critically", "stress-test this", "what am I missing logically?", "evaluate this argument". Skip for pure execution tasks with no evaluative angle.

---

## Setup (run before starting)

In one short block:

1. **Focus** — the specific claim, proposal, or question under review
2. **Default pass** — Clarify → Information → Assumptions → Reasoning → Alternatives → Conclusion (state this line so the user sees the path)

If essential context is missing, ask at most 3 questions in one message, then proceed. Mark gaps `[UNKNOWN]` or working guesses `[ASSUMED]`.

If the user asks to **skip or reorder** phases (e.g. fast logic-only pass), follow their sequence and still end with **Conclusion**.

---

## The Phases

### Clarify

Restate the target in one precise sentence. Separate **factual** vs **normative** claims. Name success criteria if a decision is involved.

### Information

What evidence exists? Label each bullet `[STRONG]`, `[WEAK]`, or `[MISSING]` (evidence quality / availability — not emotional strength).

### Assumptions

List tacit premises. For each: **Assumption:** … — **If false:** …

### Reasoning

Trace the argument chain. Flag **leaps**, **circular** patterns, **correlation vs causation**, and **missing steps**. No new factual assertions here — only structure.

### Alternatives

Credible competing explanations, plans, or frames. Do not collapse into debate rhetoric; keep alternatives plausible.

### Conclusion

1. **Judgment** — answer the focus question directly
2. **Confidence** — High / Medium / Low with one-line justification tied to evidence gaps
3. **What would change my mind** — concrete falsifiers or new data

---

## Execution Rules

1. Run phases in one response unless the user requests step-by-step pacing.
2. Never merge **Information** and **Reasoning** in the same bullet block.
3. Do not smuggle new unsupported facts into **Conclusion**; only synthesize prior phases.
4. If the user is emotionally fused with a position, name it neutrally and continue the phase plan.

---

## Checklist (verify before responding)

- [ ] Setup block: focus + stated pass (or user-requested variant)
- [ ] Each phase is its own section, in order
- [ ] Information bullets carry `[STRONG]` / `[WEAK]` / `[MISSING]`
- [ ] Assumptions use **Assumption** / **If false** pairs
- [ ] Reasoning references only what earlier phases established
- [ ] Conclusion includes judgment, confidence, and falsifiers
