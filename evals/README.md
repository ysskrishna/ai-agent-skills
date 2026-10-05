# Trigger eval queries

One file per skill: `evals/<skill-name>.json`. Each file is an array of `{ "query": "...", "should_trigger": true|false }`.

- `should_trigger: true`: realistic prompts where the skill should load. Most do not name the method.
- `should_trigger: false`: near-misses that share keywords or topics but need a different approach (often a sibling skill or plain execution).

Rules for adding queries:

- Write them like real chat messages: casual, some typos, some context.
- Keep 8 positives and 8 negatives per skill. Make at least half of the negatives close to a sibling skill's territory.
- Keep these files outside `skills/` so they are not shipped with installs.

How to use them: `validate-skills.sh` checks that each file exists and has the right shape. Running them against an agent is manual and optional (paste a prompt, see which skill loads). The method is described at <https://agentskills.io/skill-creation/optimizing-descriptions>.
