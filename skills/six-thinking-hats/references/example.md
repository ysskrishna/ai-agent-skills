# Example: Six Thinking Hats (Decision mode, light path)

Illustrative case. All details are invented.

**User:** "We run one Postgres instance for our SaaS. Should we split the reporting queries onto a read replica now? Use six hats."

**🔵 Blue (open)**
- Focus: should the team add a read replica for reporting queries this quarter?
- Mode: Decision (user needs go / no-go). Order: Blue, White, Black, Yellow, Blue.

**⚪ White**
- `[KNOWN]` Reporting queries run on the same instance as customer traffic (user said so).
- `[UNKNOWN]` Whether reporting queries cause measurable slowdowns for customers.
- `[ASSUMED]` The team has no one on call who has run replication before.

**⚫ Black**
- **Risk:** replica lag makes reports show stale numbers. **Mitigation:** show a "data as of" timestamp on every report.
- **Risk:** a new moving part nobody knows how to operate. **Mitigation:** one runbook and one failover drill before launch.

**🟡 Yellow**
- **Benefit:** heavy reports stop competing with customer requests. **Condition:** the slowdown is actually caused by reporting (see White `[UNKNOWN]`).
- **Benefit:** a path to scale reads later. **Condition:** the app can route read-only queries to a second connection.

**🔵 Blue (close)**
1. Top tension: the benefit depends on an unconfirmed cause (White `[UNKNOWN]`).
2. Recommendation: measure first. If reporting queries explain the slowdowns, go; if not, no-go for now.
3. Next step: check slow-query logs for the last two weeks (owner: backend lead, this week).
