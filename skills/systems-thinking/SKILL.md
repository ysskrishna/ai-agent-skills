---
name: systems-thinking
description: >
  Use for systems thinking, or when a change may ripple beyond its target: "what are the side effects?", "why does this keep coming back?", "how do these teams or services affect each other?". Maps loops, delays and leverage points. Skip for single-step fixes.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.10.5"
---

# Systems Thinking

See the whole before optimizing a part. End with recommendations that account for loops and delays.

## When to use

- A problem keeps returning after "fixes".
- A change in one team, service or policy may hit others (unintended consequences, incentives, queues, backlogs).
- The user asks for root causes beyond a single person or component, or for a holistic view.

Skip: single-step linear tasks, one-variable calculations, fixes that need no map of interactions.

## Before you start

1. State in one block: **System in focus** (what is inside the boundary) and **Pass** (Boundary, Structure, Dynamics, Delays, Leverage, Synthesis).
2. **Gather first.** Read the code, docs, tickets or metrics that describe how the parts connect before drawing the map. Ask up to 3 scoping questions only for what tools cannot answer.
3. **Light path.** Small ask: 2-3 bullets per phase. Never skip Structure before Leverage, even on the light path.
4. If the user already proposed an intervention, shorten Boundary but keep Structure and Dynamics.

## Phases

### 1. Boundary
What is in and out for this analysis. One sentence on the system's purpose from a stakeholder's view.

### 2. Structure
**Elements** (stocks that accumulate, actors, resources) and **flows** (rates in and out). Short pairs: **From -> To:** what moves.

### 3. Dynamics
At least one reinforcing (R) and one balancing (B) loop where plausible:

> **Loop [R|B]:** ... - **Mechanism:** ...

If no loop applies, say so in one line and why.

### 4. Delays
Where is the lag between action and effect? How does it change behavior (overshoot, oscillation, giving up too early)?

### 5. Leverage
> **Leverage point:** ... - **Why it matters:** ... - **Risk of backfire:** ...

Prefer changes to rules, information flows, incentives or goals over exhorting people to behave differently. Donella Meadows ranks these as stronger levers than adjusting parameters such as limits and budgets.

### 6. Synthesis
1. **System story:** one plain-language paragraph.
2. **Non-obvious consequence:** at least one.
3. **Recommended moves:** 2-3 actions consistent with the loops and delays above.

## Pitfalls

- Jumping to solutions before Structure and a light Dynamics pass.
- Stopping at "X is careless". Translate to the incentive or information gap behind the behavior.
- Drawing every box you can think of. Include only elements that change the answer.
- A fix that works now but triggers a balancing loop later. Check Delays against each recommendation.

Diagrams are optional; the bullets must stand alone. Worked example: [references/example.md](references/example.md).

## Checklist

- [ ] System in focus and Pass stated
- [ ] Boundary and purpose explicit
- [ ] Structure uses elements and From -> To flows
- [ ] Dynamics: R and B loops, or N/A justified
- [ ] Delays considered where time matters
- [ ] Leverage tied to the map, with backfire risk
- [ ] Synthesis tells one coherent story
