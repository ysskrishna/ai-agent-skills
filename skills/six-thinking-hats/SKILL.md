---
name: six-thinking-hats
description: >
  Applies Edward de Bono's Six Thinking Hats framework for structured multi-perspective
  analysis. Trigger only when the user explicitly asks for multi-angle analysis,
  pros-and-cons with a recommendation, brainstorming with risk/value assessment,
  a "Six Thinking Hats" session, or help deciding when clearly stuck in one mode.
  Do not trigger for simple factual questions, brief opinions, narrow single-step
  tasks (e.g., "fix this bug"), or single-lens requests (only risks, only ideas).
---

# Six Thinking Hats

Edward de Bono's Six Thinking Hats separates six modes of thinking — each a colored "hat."
By wearing one hat at a time, you avoid the muddle of defending, critiquing, and creating
all at once.

## Trigger Rules

Run this skill when **at least one** is true:

1. User explicitly asks for multi-angle or "all angles" analysis.
2. User asks for pros and cons **plus** a recommendation.
3. User asks for brainstorming combined with risk/value assessment.
4. User explicitly invokes "Six Thinking Hats."
5. User is clearly stuck in one mode (all doom, all hype) **and** asks for help deciding.

Do **not** run full hats when **any** is true:

1. Simple factual question.
2. Brief opinion with no decision context (e.g., "what do you think about X?").
3. Execution-only work ("fix this bug", "rename this variable").
4. Only one lens requested (only risks, only ideas, only feelings).

If only one lens is requested, run that hat only and offer one complementary hat.

## Quick Intake

Before running the hats, establish:

1. **Focus question** — What decision, proposal, or problem are we exploring?
2. **Key constraints** — Budget, time, policy, or non-negotiables (if any).
3. **Desired output** — Ideas list, decision, risk register, or just clarity?

If any are missing, **proceed with explicit assumptions** and surface them in White Hat
as `[ASSUMED]`. Don't stall to interrogate the user.

---

## Hat Sequence

Pick the **first** row that matches top-to-bottom. If none match, use **General**.

| Situation | Sequence |
|-----------|----------|
| Risky decision (irreversible, high cost) | Blue → White → Black → Red → Yellow → Green → Blue |
| Post-mortem (something already happened) | Blue → White → Red → Black → Yellow → Green → Blue |
| New idea / proposal | Blue → White → Yellow → Black → Green → Red → Blue |
| Creative brainstorm (open-ended) | Blue → Green → Yellow → White → Black → Blue |
| Stuck thinking (one-mode trap) | Blue → Red → Green → Yellow → Black → White → Blue |
| General / unspecified | Blue → White → Red → Black → Yellow → Green → Blue |

The sequence governs **thinking order**. The Output Contract below governs **presentation
order** — they are not the same thing.

---

## The Six Hats

### 🔵 Blue Hat — Process

**Role:** Frame the session, transition between hats, synthesize at the end.

- **Allowed:** declare focus question + chosen sequence; transitions; final synthesis.
- **Not allowed:** introducing facts, risks, or ideas not surfaced under the other hats.

---

### 🤍 White Hat — Facts

**Focus:** Data, evidence, known facts, information gaps. No interpretation.

Every bullet **must** carry an evidence label:

- `[KNOWN]` — verifiable fact provided by the user or reliable context.
- `[ASSUMED]` — working assumption due to missing data; flag explicitly.
- `[UNKNOWN]` — missing information that blocks confidence; name what's missing.

If analysis slides into opinion, park it: "That's interpretation — let's save it for
Yellow/Black."

---

### ❤️ Red Hat — Emotions

**Focus:** Gut feelings, intuitions, fears, excitement. No justification required.

**Guardrail:** When inferring others' emotions, always use hypothetical phrasing
("Stakeholders **might** feel…", "This **could** trigger concerns about…"). Never
assert inferred emotions as fact. Keep Red Hat brief.

If the user discloses clinical-level distress, acknowledge briefly and recommend
professional support — that is out of scope for this framework.

---

### 🖤 Black Hat — Risks

**Focus:** Weaknesses, risks, what could go wrong, counterarguments.

Every bullet **must** follow this template:

> **Risk:** [specific failure mode] — **Mitigation:** [concrete action]

Be specific, not vaguely negative.

---

### 💛 Yellow Hat — Value

**Focus:** Benefits, opportunities, best-case outcomes, why it could work.

Every bullet **must** follow this template:

> **Benefit:** [concrete upside] — **Condition:** [what must hold for it to materialize]

Grounded optimism, not wishful thinking.

---

### 💚 Green Hat — Creativity

**Focus:** New ideas, alternatives, lateral thinking.

Generate **exactly 3** genuinely distinct options. No evaluation inside Green Hat
(judgment happens in Black / Yellow). Use reversal ("what's the opposite?"), analogy,
or constraint-removal to push past the obvious.

---

## Output Contract

Default mode is **single-turn**. Switch to multi-turn **only** if the user uses an
explicit opt-in phrase such as *"walk me through this"*, *"let's do this interactively"*,
*"one hat at a time"*, or equivalent.

**Tie-break:** if interactive intent is ambiguous, stay in single-turn.

### Single-turn format (canonical)

Use these **exact** headings, in this **exact** order — regardless of the thinking
sequence chosen above:

1. **Blue Hat — Framing**
2. **White Hat — Facts**
3. **Red Hat — Emotions**
4. **Black Hat — Risks**
5. **Yellow Hat — Value**
6. **Green Hat — Options**
7. **Blue Hat — Synthesis**

Per-section bullet counts (standard mode):

- Sections 1–6: **exactly 3 bullets each.**
- Section 7 (Synthesis): **exactly 4 bullets**, in this order:
  1. Key tension #1 (between hats)
  2. Key tension #2
  3. Recommendation
  4. Next step (with owner / timeframe if known)

### Compact mode (length & budget fallback)

Use compact mode when **any** of these hold: prompt is very long, intake context is
substantially incomplete, or output budget is tight. Keep the **same headings and order**:

- Sections 1–6: **exactly 2 bullets each.**
- Section 7: **exactly 3 bullets** — top tension, recommendation, next step.

**Never drop required sections.** Compactness reduces bullets, never structure.

### Multi-turn mode

Only when explicitly opted in. Ask one focused prompt per hat in the chosen thinking
sequence, wait for the user, then proceed. The final turn must still end with a
**Blue Hat — Synthesis** that follows the same synthesis bullet rules above.

---

## Key Principles

1. **Keep hats separate.** Park out-of-scope thoughts for the appropriate hat.
2. **Blue owns process, not perspective.** Synthesis references prior hat outputs only.
3. **Evidence discipline in White.** Every bullet labeled `[KNOWN] / [ASSUMED] / [UNKNOWN]`.
4. **Risk + mitigation are inseparable** (Black Hat).
5. **Benefit + condition are inseparable** (Yellow Hat).
6. **Green Hat is judgment-free** — generation only.
7. **Always end with Blue.** Synthesis is mandatory, not optional.
8. **Unstick trapped thinking** — if one-mode-trapped, name it and route to a contrasting hat.

---

## When to Offer a Lighter Path

The full method is overkill for reversible / cheap decisions or single-lens needs.
Offer one of these instead:

- **Risk scan only:** White + Black.
- **Idea generation only:** Green + Yellow.
- **Decision shortcut:** White + Black + Yellow + Blue synthesis.

Propose the lighter path **before** running full hats when (a) the user requested only
one lens, or (b) the decision is explicitly described as low-stakes / reversible.
