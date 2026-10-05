# Example: Ethical Thinking (light path)

Illustrative case. All details are invented.

**User:** "We want to use customers' support chat transcripts to train an internal model that drafts replies. Is that okay?"

**Focal action:** train an internal reply-drafting model on past customer support transcripts.
**Pass:** Stakeholders, Values, Harms and Benefits, Justice and Power, Options, Recommendation.

**Stakeholders**
- Direct: customers whose chats are used; support agents whose replies become training data.
- Indirect: future customers who receive model-drafted replies.
- Vulnerable: customers who shared health or financial details in chat, because they wrote under the assumption that a person would read it.

**Values**
- **Autonomy vs efficiency:** customers did not choose this use; faster replies help everyone.
- **Privacy vs quality:** more complete transcripts give a better model but carry more personal data.

**Harms and Benefits**
- Harm: the model repeats personal details in another customer's reply. Plausible if transcripts are not scrubbed. Hard to undo once trained.
- Benefit: faster and more consistent replies. Plausible; benefits depend on review by agents.
- Predicted only; no incident history was provided.

**Justice and Power**
- Customers carry the privacy risk; the company gets the benefit. Customers cannot say no after the fact.
- Agents' work becomes training data without a stated say. Check what their contract and policy allow.

**Options**
> **Option:** do not proceed - **Value fit:** respects autonomy - **Residual harm:** slower replies - **Safeguards:** none needed.
> **Option:** proceed with redaction and opt-out - **Value fit:** balances both - **Residual harm:** redaction misses - **Safeguards:** automated plus sampled manual checks, opt-out honored, retention limit, owner named.

**Recommendation**
- Conditional: proceed only with redaction, an opt-out and a named owner. Legal review needed on consent wording and data rules.
- Strongest reason against: transcripts may hold sensitive details that redaction cannot reliably find.
- Monitor: leaks found in drafts, opt-out rate, and agent feedback.
