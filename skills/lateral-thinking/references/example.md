# Example: Lateral Thinking (light path)

Illustrative case. All details are invented.

**User:** "Our onboarding checklist has 12 steps and users drop off around step 5. We keep shortening copy and moving steps around. Nothing sticks."

**Stuck point:** the assumption that onboarding is a sequence users must complete before value.
**Pass:** Provocation, Extract principle, Concept fan, Candidates.

**Provocation**
> **Po:** users never see the checklist. - **Movement idea:** the product could do the setup for them, so the checklist is not their job.

**Extract principle**
- Setup should happen as a by-product of using the product, not as a gate in front of it.

**Concept fan**
- Direction: remove setup from the user's path.
  - Concept: infer settings from existing data. Ideas: import from the tool they already use; prefill from the signup email domain.
  - Concept: do setup lazily when first needed. Ideas: ask for the integration key only when the user clicks "send test event".
- Direction: make the remaining setup feel like progress.
  - Concept: show value first. Idea: open with a working demo project already populated.

**Candidates**
- `near-term` Ask for each setting at the moment it is first needed.
- `near-term` Open with a prefilled demo project.
- `stretch` Import settings from the user's current tool.
- `experimental` One-sentence setup: the user types what they want and the product configures itself.
