# Example: Systems Thinking (light path)

Illustrative case. All details are invented.

**User:** "Our on-call engineers are burning out, so we added more alerts to catch problems earlier. Pages went up and so did the burnout. Why?"

**System in focus:** the alerting and on-call process of one engineering team.
**Pass:** Boundary, Structure, Dynamics, Delays, Leverage, Synthesis.

**Boundary**
- In: alerts, pages, on-call engineers, incident backlog. Out: product roadmap.
- Purpose: detect and fix customer-facing problems quickly without exhausting the team.

**Structure**
- Alerts -> Pages: each new alert rule adds pages.
- Pages -> Interrupted engineer time: lowers time for fixing causes.
- Unfixed causes -> Future alerts: the same problem fires again.

**Dynamics**
> **Loop [R]:** more alerts -> more pages -> less time to fix causes -> more repeat alerts - **Mechanism:** interruptions starve the work that would remove the alerts.
> **Loop [B]:** tired engineers -> slower response -> management adds alerts to catch problems "earlier" - **Mechanism:** the fix for slowness feeds loop R.

**Delays**
- Burnout shows up weeks after the alert load rises, so the cause looks unrelated.

**Leverage**
> **Leverage point:** a rule that every page must have an owner and a ticket to remove its cause - **Why it matters:** it changes the information flow so repeat alerts get fixed - **Risk of backfire:** teams delete alerts instead of fixing causes; review deleted alerts monthly.

**Synthesis**
1. Story: alerts were treated as a safety net, but each page took away the time needed to remove the causes, so pages kept growing.
2. Non-obvious: adding detection made the team slower at prevention.
3. Moves: pause new alert rules for one cycle; tag every page by cause; fund time to fix the top three repeat causes.
