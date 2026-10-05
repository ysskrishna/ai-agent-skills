---
name: design-thinking
description: >
  Use for design thinking, or when a product or service problem needs user understanding before solutions: "what do users really need?", "how might we...", "plan a discovery sprint", "validate this concept". Skip when the spec is frozen or the task is code maintenance.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.10.5"
---

# Design Thinking

Fall in love with the problem, not the first solution. End with **what to learn next**, not just ideas.

## When to use

- A product, service or UX problem where the real user need is unclear.
- "How might we" framing, discovery sprints, concept validation before building.
- Reframing a request using what users actually do or say.

Skip: the spec is fully frozen and no discovery is wanted, or the task is code-only maintenance with no user problem to frame.

## Before you start

1. State in one block: **Design challenge** (who is affected, in what situation) and **Pass** (Empathize, Define, Ideate, Prototype, Test plan).
2. **Gather first.** Read tickets, interview notes, support threads, analytics or the product itself before writing Empathize. Ask up to 3 questions only for users, constraints or success signals that tools cannot answer.
3. **Light path.** Small ask: 1-2 lines per stage, 3 ideas, one prototype, 2 signals.
4. If Empathize has no real user input, say so in Define and keep the POV narrow. Never invent research.

## Stages

### 1. Empathize
- **Who:** primary user or stakeholder. Mark facts from the user versus `[INFERRED]`.
- **Jobs, pains, gains:** what they are trying to do and what hurts.
- **Context:** when and where the need shows up.

No fabricated quotes. Paraphrase only what the user supplied.

### 2. Define
- **Insight:** a non-obvious tension connecting pains and context.
- **POV:** "**[User]** needs **[verb]** because **[insight]**."
- **How Might We:** 2-3 well-scoped questions opened by the POV.

### 3. Ideate
Quantity and variety, using each HMW as a prompt. Tag each idea `desirable`, `feasible` or `viable` as a **hypothesis**, not a fact. Default 8-10 ideas unless the user sets a number.

### 4. Prototype
Describe low-fidelity artifacts: paper flow, roleplay script, landing-page smoke test, clickable sketch. For each: **Purpose:** the question it answers. **Fidelity:** one line placing it between sketch-only and interactive.

### 5. Test plan
- **Learning goals:** what would convince you the idea is wrong?
- **Participants:** who and how many, or "to be decided".
- **Signals:** behaviors or metrics to observe, stated so they can fail.
- **Next iteration:** what changes if results are mixed.

## Pitfalls

- A POV that restates the solution ("users need a dashboard").
- HMW questions that are too broad ("improve the experience") or too narrow (they hide the solution).
- Treating desirable / feasible / viable tags as proven.
- A Test plan with no signal that could show the idea is wrong.

Worked example: [references/example.md](references/example.md).

## Checklist

- [ ] Challenge and Pass stated
- [ ] Empathize separates facts from `[INFERRED]`
- [ ] POV and HMW before Ideate
- [ ] Ideas tagged desirable, feasible or viable as hypotheses
- [ ] Prototype gives purpose and a fidelity line
- [ ] Test plan has learning goals and falsifiable signals
