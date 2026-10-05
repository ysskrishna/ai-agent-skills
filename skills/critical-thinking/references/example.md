# Example: Critical Thinking (light path)

Illustrative case. All details are invented.

**User:** "Our checkout conversion went up after we switched to a single-page checkout, so we should convert every flow to single-page. Sanity check?"

**Focus:** "The single-page checkout caused the conversion increase, so all flows should switch."
**Pass:** Clarify, Information, Assumptions, Reasoning, Alternatives, Conclusion.

**Clarify**
- Factual claim: the change caused the increase. Normative claim: every flow should switch.

**Information**
- `[CITED]` User states conversion rose after the switch. Basis is the user's report; no figures or dates given.
- `[MISSING]` Traffic mix, test design, and time window before and after.

**Assumptions**
- **Assumption:** nothing else changed in the same period. **If false:** the lift may belong to a promotion or traffic shift.
- **Assumption:** checkout flows are alike. **If false:** a flow with many fields or add-ons may behave differently.
- **Value premise:** conversion is the metric that matters. **If rejected:** refund rate or support load may change the answer.

**Reasoning**
- Leap: "after" is treated as "because of" (correlation vs causation).
- Leap: one flow's result is applied to all flows (hasty generalization).
- Bias to consider: confirmation (the team chose the redesign).

**Alternatives**
- Seasonal or campaign traffic raised conversion.
- Single-page helps mobile users only.

**Conclusion**
1. Judgment: the claim is plausible but not shown. The case for "all flows" is weak because the evidence is one report with `[MISSING]` design details.
2. Would change the judgment: an A/B test or matched before/after with the same traffic mix; results by device and flow type.
