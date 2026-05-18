---
name: ethical-thinking
description: >
  Use this skill when the user asks for ethical thinking or wants a structured
  pass on values and harms—mapping stakeholders, tradeoffs, power asymmetries,
  harms and benefits, consent, justice, and fair process for a plan or product.
  Use for moral review, fairness or AI-ethics style questions, stakeholder harm
  scans, or should-we questions beyond pure legality, including indirect asks.
  Skip when they want legal advice as such, only neutral facts with no
  normative review requested, or implementation-only work with no values lens
  asked for.
license: MIT
metadata:
  author: ysskrishna
  version: "2026.5.17"
---

# Ethical Thinking

Ethics is about **conflicts between legitimate goods**. End with transparent tradeoffs, not false certainty.

---

## When to Use

Use for actions affecting welfare, dignity, consent, autonomy, justice, or collective risk. Not a substitute for legal advice; flag **legal review needed** when law may bind.

---

## Setup (run before starting)

In one short block:

1. **Ethical focal action** — what is being considered?
2. **Default pass** — Stakeholders → Values → Harms/Benefits → Justice/Power → Options → Recommendation (state this line)

Up to 3 questions on affected parties and red lines; proceed with `[UNKNOWN]` for missing stakeholder detail.

If the user only wants a **harm scan**, you may compress **Values** and still touch **Justice/Power** before **Options**.

---

## The Lenses

### Stakeholders

Who is **affected** (direct / indirect / future / non-human if ecologically relevant)? **Vulnerability** — dependence, cognitive load, marginalization — tag `higher` / `medium` / `lower` with justification from context (not stereotypes).

### Values

Which **values** are in play (autonomy, beneficence, non-maleficence, justice, dignity, solidarity, etc.)? Map **value tension** pairs: **A vs B** — why both matter here.

### Harms / Benefits

Concrete **harms** and **benefits** with likelihood **Low/Med/High** and **reversibility** where applicable. Distinguish **predicted** vs **observed** (if user gave history).

### Justice / Power

Distribution of **burdens and boons**. **Power asymmetry** — who can say no, who bears error cost? Note **procedural** fairness (voice, consent, appeal).

### Options

2+ ethically distinct paths (including **do not proceed** if plausible). For each:

> **Option:** … — **Value fit:** … — **Residual harm:** … — **Safeguards:** …

### Recommendation

State a **preferred** option if the analysis supports one, or **conditional** guidance. Include **dissenting consideration** — strongest reason against your recommendation. Add **monitoring** — what to watch if you proceed.

---

## Execution Rules

1. Do not **demonize** actors; focus on structures, incentives, and foreseeable effects.
2. If values irreconcilably clash, say so — recommend **process** (deliberation, oversight) not fake unanimity.
3. Never invent sensitive personal attributes about real people; stick to user-supplied facts.

---

## Checklist (verify before responding)

- [ ] Setup: focal action + default pass (note if harm-scan style compression)
- [ ] Stakeholders include indirect/future if relevant
- [ ] At least one explicit **value tension** pair
- [ ] Harms/benefits have likelihood; options have safeguards
- [ ] Justice/power addresses distribution and voice/consent
- [ ] Recommendation names residual harm and dissenting consideration
