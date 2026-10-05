---
name: first-principles-thinking
description: >
  Use for first principles thinking, or when the user questions an inherited default: "why do we do it this way?", "is this cost really necessary?", "should we copy what competitors do?". Strips analogies and rebuilds from fundamentals. Skip for convention-following checklists.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.10.5"
---

# First Principles Thinking

Question inherited baggage. Rebuild only from **bedrock** you can defend.

## When to use

- "Why do we do it this way?", "is this really required?", "what would this cost if we started from scratch?"
- A strategy or design copied from an incumbent ("like Uber for X") that nobody has checked.
- Cost, architecture or process choices that exist only because they always have.

Skip: quick convention-following checklists with no wish to revisit assumptions, or purely social coordination with nothing to model.

## Before you start

1. State in one block: **Reconstruction target** (belief, cost, design or strategy to ground) and **Pass** (Surface, Question, Bedrock, Rebuild, Implications).
2. **Gather first.** Read the code, contracts, specs or data that show what is actually required (a regulation, an SLA, a measured limit) before tagging anything fundamental. Ask up to 3 questions only for immutable constraints that tools cannot answer.
3. **Light path.** Small ask: 3 assumptions, 3 bedrock items, a 3-step rebuild, 2 implications.

## Steps

### 1. Surface
State the conventional answer or the analogy people rely on. List loaded words and hidden comparisons.

### 2. Question
For each major assumption: **Assumption:** ... - **Why believed?** (authority, analogy, experience) - **What if false?**

### 3. Bedrock
List truths that survive scrutiny: physics, logic, arithmetic, legal musts, documented needs of real users. Tag each `[FUNDAMENTAL]` or `[ASSUMPTION]`.

Aim for three or more honest bedrock items. If fewer exist, say why in one line.

### 4. Rebuild
Derive conclusions in numbered steps using only `[FUNDAMENTAL]` items. "Industry standard" is not a premise unless translated into a fundamental (for example "buyers require SLA X because regulation Y"). A new premise goes into Bedrock first, with a tag.

### 5. Implications
- **So what:** what changes versus the conventional path.
- **Cost of being wrong** if a tagged assumption fails.
- A short **vs convention** contrast when it helps the decision.

If bedrock is too thin to rebuild, write **insufficient grounding** and list the evidence that would fix it.

## Pitfalls

- Calling a preference or a habit "fundamental".
- Rebuilding from first principles and arriving exactly at the old answer. That is fine if each step is defended; say so.
- Faux profundity. Keep every step short and checkable.
- Ignoring switching cost. A better design from scratch may not beat the current one after migration.

Worked example: [references/example.md](references/example.md).

## Checklist

- [ ] Target and Pass stated
- [ ] Surface names the convention or analogy
- [ ] Question ties each assumption to why it is held
- [ ] Bedrock tagged `[FUNDAMENTAL]` or `[ASSUMPTION]`
- [ ] Rebuild uses only fundamentals
- [ ] Implications name what changes and the cost of being wrong
