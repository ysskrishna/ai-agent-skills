# Example: Analytical Thinking (light path)

Illustrative case. All details are invented.

**User:** "Weekly signups from our pricing page dropped last month. What should we look at?"

**Analytical question:** which factor best explains the drop in weekly signups from the pricing page last month?
**Pass:** Frame, Decompose, Hypotheses, Evidence, Synthesis.

**Frame**
- Type: explain. Unit: weekly signups attributed to the pricing page. Baseline: the previous four weeks.

**Decompose**
- Signups = visitors x conversion rate.
  - Visitors: traffic by channel (search, paid, referral); page load issues.
  - Conversion: page changes, price changes, form errors, tracking changes.

**Hypotheses**
- H1: traffic fell (one channel). Expect visitors down with stable conversion. Falsified if visitors are flat.
- H2: conversion fell after a page or price change. Expect a step change on a known date. Falsified if conversion is flat.
- H3: tracking broke. Expect a drop in recorded events but not in billing signups. Falsified if billing signups fell too.

**Evidence**
- Not yet gathered. Thought experiment (no data): ask the user for visitors, conversion and billing signups by week for 8 weeks, and the deploy log.
- Reading guide: H1 shows in visitors by channel. H2 lines up with a deploy or price date. H3 shows when billing and analytics disagree.

**Synthesis**
1. Answer: not determinable without data; the three checks above separate the causes in under an hour.
2. Key uncertainty: whether billing signups also dropped (separates a real drop from a tracking fault).
3. Next step: pull 8 weeks of visitors, conversion and billing signups; compare against the deploy log.
