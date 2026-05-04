---
name: six-thinking-hats
description: >
  Applies Edward de Bono's Six Thinking Hats as a sequential thinking-partner process.
  Selects hat-set modes (Full, Creative, Risk, Decision, Custom) and depth levels
  (Quick, Standard, Deep Dive) to match user intent. Use when the user asks for
  multi-angle reasoning, decision support, brainstorming with tradeoffs, or explicitly
  asks for Six Thinking Hats. Do not use for simple factual questions, execution-only
  coding tasks, or narrow single-lens requests that do not need multi-hat structure.
license: MIT
metadata:
  author: ysskrishna
---

# Six Thinking Hats

Use one hat at a time. Keep hats separate. End with Blue synthesis.

## Trigger Rules

Run this skill when at least one is true:

1. User explicitly asks for multi-angle or "all angles" analysis.
2. User asks for pros and cons plus a recommendation.
3. User asks for brainstorming combined with risk/value assessment.
4. User explicitly invokes "Six Thinking Hats."
5. User is clearly stuck in one mode and asks for help deciding.

Do not run this skill when any is true:

1. Simple factual question.
2. Brief opinion with no decision context.
3. Execution-only work.
4. Single-lens request that does not need multi-hat flow.

If single-lens is enough, answer directly or suggest a lighter subset mode.

---

## Operating Model

Process is always:

1. Pre-Processing
2. Mode selection (which hats)
3. Depth selection (how deep)
4. Sequential execution
5. Blue synthesis (required, see Synthesis Contract)
6. Optional interactive pacing or compiled recap (see Synthesis Contract)

### 1) Pre-Processing

Establish quickly:

1. Focus question.
2. Key constraints.
3. Desired output.

Gap handling:

1. Infer from user context where reasonable.
2. If needed, ask at most 3 clarification questions in a single message, then proceed.
3. Only pause for clarification when missing information is decision-critical; otherwise continue with explicit uncertainty labels.
4. If proceeding with missing data, mark White bullets as `[UNKNOWN]` or `[ASSUMED]`.

### 2) Mode Selection (hat set)

Defaults:

- If user gives no mode/depth: `Full + Standard`.
- If mode only: keep `Standard`.
- If depth only: keep `Full`.

| Mode | Hats to run | Default order | Typical use | Why some hats are dropped |
|------|-------------|---------------|-------------|---------------------------|
| Full (default) | Blue (frame), White, Red, Black, Yellow, Green, Blue (synthesis) | Blue frame -> White -> Red -> Black -> Yellow -> Green -> Blue synthesis | Broad decisions or full-spectrum reasoning | None |
| Creative | Blue (frame), White (constraints, if needed), Green, Yellow, Red, Blue (synthesis) | Blue frame -> White constraints (only if hard constraints exist) -> Green -> Yellow -> Red -> Blue synthesis | Idea generation with upside and emotional resonance while staying feasible | Skips Black to avoid early idea shutdown |
| Risk | Blue (frame), White, Black, Blue (synthesis) | Blue frame -> White -> Black -> Blue synthesis | Risk scans and failure prevention | Skips Yellow/Green/Red to stay focused on downside |
| Decision | Blue (frame), White, Black, Yellow, Blue (synthesis) | Blue frame -> White -> Black -> Yellow -> Blue synthesis | Practical go/no-go decisions | Skips Red/Green to keep evaluation evidence-driven |
| Custom | User-defined hats + Blue synthesis | Confirm order explicitly, then run sequentially | User-directed workflows | Per user request |

Custom mode rules:

- Allowed hats: Blue, White, Red, Black, Yellow, Green. If the user names anything else, ask them to map it to one of these or drop it; do not invent new hats.
- Require Blue synthesis at the end. If the user omits it, add it without asking.
- If user order is unclear, ask once and then proceed.

### 3) Depth Selection (independent layer)

Depth applies on top of any mode.

| Depth | Guidance |
|-------|----------|
| Quick | 2 insights per hat, concise language |
| Standard (default) | 2-3 insights per hat, balanced detail |
| Deep Dive | 3-5 insights per hat with examples, edge cases, and explicit assumptions |

Depth does not change hat templates or discipline. Per-hat overrides (e.g., Green's option counts) take precedence over this table.

### 4) Sequential Execution

Run hats one at a time in selected order.

- Default output format: produce one complete response with clearly separated hat sections in execution order. Do not blend multiple hats in one section.
- "One focused prompt per hat" means the agent itself produces that hat's analysis as a single focused turn; it does not mean asking the user a question per hat.
- If the user requests speed, switch to Quick depth or a narrower mode. Do not collapse hats into a mixed-hat blob.
- If the user requests interactive pacing, emit one hat per assistant message and pause between hats.

---

## The Six Hats

### Blue Hat - Process

Blue runs at least twice: once at the start (frame) and once at the end (synthesis). Both turns share the same constraint:

- Allowed: framing, transitions, synthesis.
- Not allowed: adding new facts, risks, ideas, or recommendations that were never surfaced by another hat.

#### Blue Frame (start)

Open the run with a single short block stating:

1. Focus question (one sentence).
2. Scope and key constraints.
3. Mode selected (and whether defaulted).
4. Depth selected (and whether defaulted).
5. Hat order to be used.

#### Blue Synthesis (end)

Follow the Synthesis Contract below.

---

### White Hat - Facts

Focus: data, evidence, unknowns. No interpretation.

Every White bullet must include one label:

- `[KNOWN]` — verifiable fact provided by the user or reliable context.
- `[ASSUMED]` — working assumption due to missing data; flag explicitly.
- `[UNKNOWN]` — missing information that blocks confidence; name what's missing.

If interpretation appears, park it for Black/Yellow.

Count by depth:

- Quick: 2 bullets
- Standard: 2-3 bullets
- Deep Dive: 3-5 bullets

---

### Red Hat - Emotions

Focus: intuitions, concerns, enthusiasm, resistance.

Guardrails:

- Inferred emotions must be hypothetical ("might", "could", "may"), never asserted as fact.
- Emotions stated by the user are passed through verbatim and labeled as **stated**, not paraphrased.

Count by depth:

- Quick: 2 signals
- Standard: 2-3 signals
- Deep Dive: 3-5 signals

---

### Black Hat - Risks

Focus: failure modes, weaknesses, downside scenarios.

Every Black bullet must follow:

> **Risk:** [specific failure mode] — **Mitigation:** [concrete action]

Count by depth:

- Quick: 2 bullets
- Standard: 2-3 bullets
- Deep Dive: 3-5 bullets

---

### Yellow Hat - Value

Focus: benefits, opportunities, favorable outcomes.

Every Yellow bullet must follow:

> **Benefit:** [concrete upside] — **Condition:** [what must hold for it to materialize]

Count by depth:

- Quick: 2 bullets
- Standard: 2-3 bullets
- Deep Dive: 3-5 bullets

---

### Green Hat - Creativity

Focus: alternatives, novel options, reframes.

Generate distinct options without evaluating them.

Count by depth:

- Quick: 2 options
- Standard: 3 options
- Deep Dive: 4-5 options

Use at least one forcing tactic when stuck (reversal, analogy, constraint removal).

---

## Synthesis Contract

Always finish with Blue synthesis. Default synthesis shape:

1. Top tension
2. Second tension (if relevant)
3. Recommendation
4. Next step (owner/timeframe when known)

A **tension** is a concrete trade-off where one hat's finding pulls against another's (e.g., a Yellow benefit only holds if a Black risk is mitigated, or a Green option contradicts a White `[KNOWN]` constraint).

In Quick depth, collapse to 3 bullets: one merged tension, recommendation, next step.

The recommendation must be grounded in content already produced by the hats this run. Blue does not introduce new evidence, risks, or options here.

After Blue synthesis, ask the user whether to iterate, expand a specific hat, or stop.

### Compiled Recap (on request, or after interactive run)

If the user explicitly asks for a single compiled recap, or if hats were run interactively and the user asks for consolidation, provide one message with sections for each hat that was run, in execution order, ending with the Blue synthesis block above.

---

## Key Principles

1. Keep hats separate; do not blend lenses.
2. Blue controls process; it does not invent new content.
3. White requires evidence labels on every bullet.
4. Black requires Risk + Mitigation in the same bullet.
5. Yellow requires Benefit + Condition in the same bullet.
6. Green is generation only; no evaluation.
7. End with Blue synthesis every time.
8. If the user is stuck in one lens (e.g., only complaining, only fantasizing), route to a contrasting hat.

## Acceptance Checklist

Before finishing, verify:

- Mode selected (or defaulted) and visible in the Blue Frame.
- Depth selected (or defaulted) and respected in every hat's count.
- Hats executed sequentially in declared order, one hat per message (unless a compiled recap was requested).
- White: every bullet carries `[KNOWN]`, `[ASSUMED]`, or `[UNKNOWN]`.
- Black: every bullet has both **Risk** and **Mitigation**.
- Yellow: every bullet has both **Benefit** and **Condition**.
- Red: inferred emotions use hypothetical language; user-stated emotions are passed through verbatim.
- Green: option count matches depth (Quick 2, Standard 3, Deep Dive 4-5); no evaluation mixed in.
- Blue Frame present at start; Blue Synthesis present at end; neither introduces new content.
