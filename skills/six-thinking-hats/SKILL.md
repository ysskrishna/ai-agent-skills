---
name: six-thinking-hats
description: >
  Applies Edward de Bono's Six Thinking Hats framework for structured multi-perspective
  thinking. Triggers on requests like "think through X from all angles", "pros and cons",
  "brainstorm ideas", "analyze this decision", "Six Thinking Hats session", or when a user
  seems stuck in one thinking mode (only risks, only optimism). Also applies to casual
  requests like "what do you think about X?" when structured analysis would help.
---

# Six Thinking Hats

Edward de Bono's Six Thinking Hats separates six modes of thinking — each a colored "hat."
By wearing one hat at a time, you avoid the muddle of defending, critiquing, and creating
all at once.

## Quick Intake

Before running the hats, establish:

1. **Focus question** — What decision, proposal, or problem are we exploring?
2. **Key constraints** — Budget, time, policy, or non-negotiables (if any).
3. **Desired output** — Ideas list, decision, risk register, or just clarity?

If the user wants to start immediately, proceed with what you have — don't stall.

---

## Hat Sequence

Choose the sequence that fits the situation. **If none match, use the General row.**

| Situation | Sequence |
|-----------|----------|
| General / unspecified | Blue → White → Red → Black → Yellow → Green → Blue |
| New idea / proposal | Blue → White → Yellow → Black → Green → Red → Blue |
| Risky decision | Blue → White → Black → Red → Yellow → Green → Blue |
| Stuck thinking | Blue → Red → Green → Yellow → Black → White → Blue |
| Creative brainstorm | Blue → Green → Yellow → White → Black → Blue |
| Post-mortem | Blue → White → Red → Black → Yellow → Green → Blue |

---

## The Six Hats

### 🔵 Blue Hat — Process

**Role:** Frame the session, transition between hats, synthesize at the end.

- Opens with: "We're exploring [focus question]"
- Transitions: "Now let's look at risks..." 
- Closes with: tensions between hats, key themes, recommended action

**Important:** Blue Hat manages process. Synthesis at the end *references* hat outputs
to identify tensions and conclusions — this is its job, not opinion-bleeding.

---

### 🤍 White Hat — Facts

**Focus:** Data, evidence, known facts, information gaps. No interpretation.

- What do we know for certain?
- What data is missing?
- What would we need to research?

**Discipline:** If analysis slides into opinion, park it: "That's interpretation —
let's save it for Yellow/Black and stick with raw data here."

---

### ❤️ Red Hat — Emotions

**Focus:** Gut feelings, intuitions, fears, excitement. No justification required.

- How does this feel?
- What's the instinctive reaction?
- What are the hopes and fears?

**Guardrail:** When inferring others' emotions, always use hypothetical framing:
"Stakeholders might feel..." or "This could trigger concerns about..." Never assert
emotions as fact. If the user shares difficult emotions, acknowledge briefly but
note this isn't therapy — recommend professional support for clinical concerns.

**Discipline:** Brief — a few sentences capturing emotional tone is enough.

---

### 🖤 Black Hat — Risks

**Focus:** Weaknesses, risks, what could go wrong, counterarguments.

- What could fail?
- What assumptions might be wrong?
- Who would object and why?

**Discipline:** Be specific, not vaguely negative. Pair risks with mitigation cues:
"This is a risk because X — which means we'd need to..."

---

### 💛 Yellow Hat — Value

**Focus:** Benefits, opportunities, best-case outcomes, why it could work.

- What's the upside if this succeeds?
- Who benefits and how?
- What strengths does this build on?

**Discipline:** Grounded optimism. "This could work because..." not wishful thinking.

---

### 💚 Green Hat — Creativity

**Focus:** New ideas, alternatives, lateral thinking, what-ifs.

- What if we approached this differently?
- What's the unconventional option?
- What would a different industry do?

**Discipline:** Suspend judgment. Generate 3-5 genuinely distinct ideas. Use reversal
("what's the opposite?"), analogy, or constraint removal to push beyond the obvious.

---

## Output Format

Structure your response with each hat clearly labeled. Keep each section focused
(3-6 bullets or a short paragraph). End with Blue Hat synthesis.

**Single-turn mode (default):** Complete all hats in one response.

**Multi-turn mode:** If the user explicitly wants to think interactively ("let's work
through this together"), ask one prompt per hat and wait for their input before
proceeding to the next.

---

## Key Principles

1. **Keep hats separate** — Don't mix risk assessment (Black) into data gathering (White).
   Park off-topic thoughts for the appropriate hat.

2. **Blue Hat owns process, not perspective** — Frame, transition, synthesize. The closing
   synthesis references hat outputs to identify tensions — that's structural, not opinion.

3. **Black Hat needs mitigation** — After surfacing a risk, invite "so what would address this?"

4. **Green Hat is judgment-free** — If self-censoring happens, redirect: "We'll evaluate
   in Black Hat — Green is for generating options."

5. **Always end with Blue** — Synthesize tensions and recommend a next step.

6. **Unstick trapped thinking** — If someone is stuck in one mode (all doom = Black,
   overconfident = Yellow), name it and invite a contrasting hat.

---

## When to Skip Full Hats

The full method is overkill for reversible/cheap decisions or single-lens needs. Offer
a lighter structure: "You mainly need a risk scan — want just Black + White Hat instead
of the full six?"
