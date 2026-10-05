# Example: SWOT Analysis (light path)

Illustrative case. All details are invented.

**User:** "We are a 5-person team with a feature-flag service. Should we add an enterprise plan with SSO next year? Do a SWOT."

**Subject:** our feature-flag service. **Scope and horizon:** next 12 months. **Decision:** whether to build an enterprise plan with SSO.
**Pass:** Gather, SWOT, Prioritize, TOWS, Next steps.

**SWOT** (sources: user statements; competitor pricing pages to be checked)

| | Helpful | Harmful |
|---|---------|---------|
| **Internal** | **S1** Setup takes minutes `[user stated]`. **S2** Small team ships weekly `[user stated]`. | **W1** No audit log or role model `[user stated]`. **W2** Two engineers handle support `[user stated]`. |
| **External** | **O1** Several customers asked about SSO `[user stated]`. **O2** Larger vendors' enterprise tiers are priced high `[assumed, check pages]`. | **T1** Big vendors bundle flags into their platforms `[assumed]`. **T2** Security reviews can take months and slow sales `[assumed]`. |

**Prioritize**
- Kept: S1, W1, O1, T2. Dropped S2 and W2 for this decision (they affect pace, not whether to go).

**TOWS**
- **SO:** use fast setup (S1) to offer a guided SSO setup for the customers asking (O1).
- **WO:** build roles and an audit log (W1) first, since SSO buyers expect them (O1).
- **ST:** use fast setup (S1) as the pitch against bundled platforms (T1).
- **WT:** limit exposure to long security reviews (T2) by starting with customers who already trust the team.

**Next steps**
1. Interview the customers who asked about SSO to learn what they will pay (owner: founder, 2 weeks).
2. Check competitor enterprise pricing pages to verify O2.
3. Test first: that those customers need roles and audit logs, not only SSO.
