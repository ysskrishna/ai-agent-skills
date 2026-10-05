# Example: Strategic Thinking (light path)

Illustrative case. All details are invented.

**User:** "We're a 6-person team with a small open-source observability library. Do we monetize with a hosted version, paid support, or stay free and focus on adoption?"

**Strategic question:** how should a 6-person team turn a small open-source library into a sustainable business?
**Pass:** Intent, Landscape, Advantage, Options, Choice, Risks and Cadence.

**Intent**
- Win: reach break-even on team salaries without losing the contributor community. Non-goals: building a general observability platform.

**Landscape**
- Large vendors bundle observability. **Implication:** competing on breadth is unrealistic.
- Users of the library are mostly small teams. **Implication:** they pay for convenience and uptime, rarely for licences.

**Advantage**
- Honest gap: no proven moat yet. Plausible assets are the contributor community and deep knowledge of the library's edge cases.

**Options**
> **Option:** hosted version - **Bet:** teams pay to avoid running it - **Cost:** infra, on-call, security work - **Kill signal:** fewer than a few paying teams after two quarters.
> **Option:** paid support and consulting - **Bet:** companies pay for expertise - **Cost:** founders' time, does not scale - **Kill signal:** support requests do not convert to contracts.
> **Option:** stay free, grow adoption - **Bet:** adoption creates future leverage - **Cost:** runway - **Kill signal:** adoption stalls even with investment.

**Choice**
- Primary: paid support first, to fund runway and learn what users pay for. Defer: hosted version until three customers ask for it. Reject: platform expansion.

**Risks and Cadence**
- Risks: support work crowds out development; one large customer shapes the roadmap; a vendor ships a similar feature. Mitigate with a support cap per week, a roadmap rule that no single customer decides, and a quarterly competitor check.
- Horizons chosen: 90 days and 12 months, because this is a business-plan decision. Review trigger: if support revenue covers less than half of costs after two quarters.
