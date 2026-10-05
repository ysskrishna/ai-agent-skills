---
name: ethical-thinking
description: >
  Use for ethical thinking, or when a plan could harm or unfairly burden people: "should we do this?", "is this fair?", "privacy or bias risk", "who gets hurt?". Maps stakeholders, harms, power and consent. Skip for legal advice, neutral fact lookups and implementation-only work.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.10.5"
---

# Ethical Thinking

Ethics is about **conflicts between legitimate goods**. End with transparent tradeoffs, not false certainty.

## When to use

- A product, policy or data decision that could affect people: privacy, fairness, consent, manipulation, safety.
- "Should we?" questions that go beyond "can we" or "is it legal".
- AI and data ethics reviews, stakeholder harm scans, moral review of a plan.

Skip: legal advice as such, neutral fact-finding with no values review requested, implementation-only work.

## Before you start

1. State in one block: **Focal action** (what is being considered) and **Pass** (Stakeholders, Values, Harms and Benefits, Justice and Power, Options, Recommendation).
2. **Gather first.** Read the design doc, data fields, policy text or code to learn who and what is actually affected before assuming. Ask up to 3 questions only for affected parties or red lines that tools cannot answer.
3. **Light path.** Small ask: 2-3 lines per lens, 2 options. For a pure harm scan you may compress Values, but still cover Justice and Power before Options.

## Lenses

### 1. Stakeholders
Who is affected: direct, indirect, future, non-human where ecology matters. For vulnerable groups, describe dependence, cognitive load or marginalization in plain words and one sentence on why that raises caution. Justify from the context; never stereotype.

### 2. Values
Which values are in play (autonomy, beneficence, non-maleficence, justice, dignity, solidarity, others)? Name at least one **value tension**: **A vs B**, and why both matter here.

### 3. Harms and Benefits
Concrete harms and benefits. For each: how plausible, under what conditions, and how reversible. Separate **predicted** from **observed** when the user supplies history.

### 4. Justice and Power
Who carries the burdens and who gets the benefits? Who can say no, and who bears the cost of errors? Check procedural fairness: voice, consent, appeal.

### 5. Options
Two or more ethically distinct paths, including "do not proceed" when plausible:

> **Option:** ... - **Value fit:** ... - **Residual harm:** ... - **Safeguards:** ...

### 6. Recommendation
A preferred option if the analysis supports one, or conditional guidance. Include the **strongest reason against** your recommendation and **what to monitor** if the plan proceeds.

## Rules

1. Do not demonize actors; focus on structures, incentives and foreseeable effects.
2. If values truly clash, say so and recommend a process (deliberation, oversight) instead of fake unanimity.
3. Never invent sensitive personal facts about real people; use only what the user gave.
4. Not legal advice. Where law may bind, write "legal review needed" and do not predict legal outcomes.

## Pitfalls

- A stakeholder list that stops at "users". Include the people who bear the cost without using the product.
- Harm stated with no plausibility or conditions, which reads as either alarmist or empty.
- A Recommendation with no dissent. If you cannot name the strongest objection, the analysis is unfinished.
- Safeguards that are only intentions ("we will be careful"). Name an owner or a mechanism.

Worked example: [references/example.md](references/example.md).

## Checklist

- [ ] Focal action and Pass stated
- [ ] Stakeholders include indirect or future parties when relevant
- [ ] At least one explicit value tension
- [ ] Harms and benefits give plausibility; options list safeguards
- [ ] Justice and Power covers distribution, voice and consent
- [ ] Recommendation names residual harm and the strongest dissent
