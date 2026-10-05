# Example: Design Thinking (light path)

Illustrative case. All details are invented.

**User:** "We want to add a 'team dashboard' to our expense app because managers asked for it. Help me think it through before we build."

**Design challenge:** team managers who approve expenses; unclear what they need from a dashboard.
**Pass:** Empathize, Define, Ideate, Prototype, Test plan.

**Empathize**
- Who: team managers who approve expenses (stated by the user). Their other duties and tools are `[INFERRED]`.
- Pain (stated): they "asked for a dashboard". The underlying job is `[INFERRED]`: know quickly which claims need attention.
- Context: no interview notes were supplied, so nothing more is claimed.

**Define**
- Insight: managers ask for a dashboard, but the likely need is "tell me what needs my approval and what looks wrong".
- POV: **Team managers** need **to see only the claims that need action** because **reviewing every claim wastes their limited time**.
- HMW: How might we surface unusual claims without a full report? How might we let managers approve in bulk with confidence?

**Ideate** (hypotheses)
- Weekly digest of claims that need action (`desirable`, `feasible`).
- Dashboard with spend by category (`feasible`, desirability unproven).
- Flag claims above a manager-set threshold (`desirable`, `feasible`, `viable`).

**Prototype**
- Email mockup of the weekly digest. **Purpose:** do managers act on a digest without opening the app? **Fidelity:** static sketch.
- Paper layout of the dashboard. **Purpose:** which numbers do managers point at first? **Fidelity:** sketch only.

**Test plan**
- Learning goal: the digest is the wrong direction if managers still ask for a dashboard after seeing it.
- Participants: 5 managers to be decided with the user.
- Signals: do they act on a claim from the digest within the session; which number they point to on the paper layout.
- Next iteration: if managers split, test a digest with a link to a small spend view.
