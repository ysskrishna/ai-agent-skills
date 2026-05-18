# AI Agent Skills

A curated collection of agent skills, compatible with Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more.

## Installation

### Via Claude Code Plugin Marketplace

```bash
# Add the marketplace
/plugin marketplace add ysskrishna/ai-agent-skills

# Install plugin(s) from the catalog
/plugin install six-thinking-hats@ai-agent-skills
/plugin install critical-thinking@ai-agent-skills
/plugin install systems-thinking@ai-agent-skills
/plugin install creative-thinking@ai-agent-skills
/plugin install strategic-thinking@ai-agent-skills
/plugin install analytical-thinking@ai-agent-skills
/plugin install lateral-thinking@ai-agent-skills
/plugin install design-thinking@ai-agent-skills
/plugin install first-principles-thinking@ai-agent-skills
/plugin install ethical-thinking@ai-agent-skills
```

### Via skills.sh

Install via [skills.sh](https://skills.sh):

```bash
# Install all skills from this repo
npx skills add ysskrishna/ai-agent-skills

# Or install individual skills
npx skills add ysskrishna/ai-agent-skills/six-thinking-hats
npx skills add ysskrishna/ai-agent-skills/critical-thinking
npx skills add ysskrishna/ai-agent-skills/systems-thinking
npx skills add ysskrishna/ai-agent-skills/creative-thinking
npx skills add ysskrishna/ai-agent-skills/strategic-thinking
npx skills add ysskrishna/ai-agent-skills/analytical-thinking
npx skills add ysskrishna/ai-agent-skills/lateral-thinking
npx skills add ysskrishna/ai-agent-skills/design-thinking
npx skills add ysskrishna/ai-agent-skills/first-principles-thinking
npx skills add ysskrishna/ai-agent-skills/ethical-thinking
```

## Skills

| Name | Description |
|------|-------------|
| [`six-thinking-hats`](skills/six-thinking-hats/SKILL.md) | Applies Edward de Bono's Six Thinking Hats as a sequential thinking-partner process. Selects hat-set modes (Full, Creative, Risk, Decision, Custom) and depth levels (Quick, Standard, Deep Dive) to match user intent. Use when the user asks for multi-angle reasoning, decision support, brainstorming with tradeoffs, or explicitly asks for Six Thinking Hats. Do not use for simple factual questions, execution-only coding tasks, or narrow single-lens requests that do not need multi-hat structure. |
| [`critical-thinking`](skills/critical-thinking/SKILL.md) | Structured critical inquiry: clarify claims, surface assumptions, weigh evidence, test logic, and stress-test conclusions. Use when the user asks for critical thinking, rigorous evaluation of an argument, a belief audit, decision quality review, or explicit devil's-advocate analysis without needing a full multi-framework workshop. |
| [`systems-thinking`](skills/systems-thinking/SKILL.md) | Map interdependencies, feedback loops, delays, stocks and flows, and leverage points before recommending action. Use when the user asks for systems thinking, holistic analysis, unintended consequences, root causes beyond single blame, or "how does this connect to that?" across teams, products, or policies. |
| [`creative-thinking`](skills/creative-thinking/SKILL.md) | Facilitate divergent ideation: fluency, flexible perspectives, novel combinations, and elaboration — with optional light convergence. Use when the user asks for creative thinking, fresh ideas, "blue sky" options, creative reframes, or more variety before committing — not when they only want critique or a single correct answer. |
| [`strategic-thinking`](skills/strategic-thinking/SKILL.md) | Connect intent, context, capabilities, and options into a coherent strategy with tradeoffs, risks, and a sequenced path. Use when the user asks for strategic thinking, competitive positioning, roadmap logic, "where to play / how to win", portfolio prioritization, or narrative that links goals to constraints and bets. |
| [`analytical-thinking`](skills/analytical-thinking/SKILL.md) | Decompose problems, define metrics and hypotheses, structure evidence, and synthesize findings with explicit uncertainty. Use when the user asks for analytical thinking, structured breakdowns, quant reasoning framing, root-cause trees, or decision tables — not pure brainstorming or ethics-first deliberation alone. |
| [`lateral-thinking`](skills/lateral-thinking/SKILL.md) | Disrupt fixed patterns with provocations, concept fans, challenge questions, and deliberate reframes to escape local optima. Use when the user asks for lateral thinking, de Bono-style provocation, "unstick" ideation, pattern break, or surprising angles — especially after conventional brainstorming stalls. |
| [`design-thinking`](skills/design-thinking/SKILL.md) | Human-centered design flow: empathize with needs, frame the problem, ideate, prototype intent, and define learning tests. Use when the user asks for design thinking, HCD, problem reframing from user evidence, service or UX concept sprints, or "how might we" exploration before build — not for pure code review without a user problem. |
| [`first-principles-thinking`](skills/first-principles-thinking/SKILL.md) | Strip analogies and convention to surface fundamental truths, then rebuild a reasoning chain and implications. Use when the user asks for first principles, "reason from scratch", challenge industry defaults, physics-of-business style breakdowns, or to sanity-check whether copying incumbents makes sense. |
| [`ethical-thinking`](skills/ethical-thinking/SKILL.md) | Map stakeholders, values, harms and benefits, power asymmetries, and fair process to clarify ethical tradeoffs and recommendations. Use when the user asks for ethical thinking, moral review of a plan, AI or data ethics, fairness, stakeholder harm scans, or "should we" questions beyond pure legality. |

## Changelog

See [CHANGELOG](https://github.com/ysskrishna/ai-agent-skills/blob/main/CHANGELOG.md) for release history.

## Support

If you find this library helpful:

- ⭐ Star the repository
- 🐛 Report issues
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](https://github.com/ysskrishna/ai-agent-skills/blob/main/LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://github.com/ysskrishna/ai-agent-skills/issues">Report Issues</a>
</p>
