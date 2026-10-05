# Example: Fermi Estimation (light path)

Illustrative case. All inputs are invented for the example.

**User:** "We're adding a 'recent activity' feed that writes one row per user action. Roughly how much storage per year, and will one database handle it?"

**Quantity:** storage added per year by the feed, in GB, plus peak writes per second. **Purpose:** decide whether the current database is enough. **Needed accuracy:** within a factor of 3.
**Pass:** Decompose, Estimate, Combine, Cross-check, Sensitivity.

**Decompose**
- Storage per year = active users x actions per user per day x 365 x bytes per row.

| Factor | Low | High | Basis |
|--------|-----|------|-------|
| Active users | 20,000 | 60,000 | `[ESTIMATED]` user's current count and growth |
| Actions per user per day | 10 | 40 | `[ESTIMATED]` guess; check product analytics |
| Bytes per row (with index) | 200 | 500 | `[ESTIMATED]` typical small row |

**Combine**
- Low: 20,000 x 10 x 365 x 200 B = 14.6 GB per year.
- High: 60,000 x 40 x 365 x 500 B = 438 GB per year.
- Geometric midpoint: about 80 GB per year. Order of magnitude: tens to hundreds of GB.
- Peak writes: average is users x actions / 86,400 s, about 2-28 per second; assume peak is 10x average, so roughly 20-280 per second.

**Cross-check**
- A similar existing table of 1 million rows takes about 300 MB in the user's database (`[ESTIMATED]`, check). Rows per year, low to high: 73 million to 876 million, which is about 22 GB to 260 GB. Close to the first result.

**Sensitivity**
- Actions per user per day moves the answer most (4x range). Measure it from product analytics for two weeks.
- Verdict: storage is not a problem for one database for several years at the low end; at the high end plan retention or partitioning. Peak writes up to a few hundred per second are usually fine, but verify against the database's measured limit.
