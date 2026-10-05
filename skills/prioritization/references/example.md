# Example: Prioritization (light path)

Illustrative case. All numbers are invented for the example.

**User:** "We have six improvement ideas for our invoicing app and one engineer for the next six weeks (about 1.5 person-months). What should we do first?"

**Goal:** reduce churn among small-business customers this quarter. **Capacity:** about 1.5 person-months. **Items:** 6.
**Pass:** Pick method, Score, Rank, Cut line, Sanity check.

**Method:** RICE, because the user can estimate reach and effort.

| Item | Reach (users/quarter) | Impact | Confidence | Effort (person-months) | RICE |
|------|----------------------|--------|-----------|------------------------|------|
| A. Fix PDF export bug | 800 | 1 | 100% | 0.25 | 3,200 |
| B. Recurring invoices | 500 | 2 | 80% | 1.0 | 800 |
| C. Bulk import | 300 | 1 | 80% | 0.5 | 480 |
| D. Dark mode | 1,000 | 0.25 | 80% | 0.5 | 400 |
| E. Payment reminders | 600 | 2 | 50% | 0.75 | 800 |
| F. Accounting integration | 400 | 3 | 50% | 2.0 | 300 |

Basis: reach from the user's estimates; impact and confidence are `[ESTIMATED]`; effort from the engineer.

**Rank:** A (3,200), then B and E (tied at 800), C (480), D (400), F (300). Tie-break B vs E: E has lower confidence (50%), so confirm demand with five customers before committing; B first.

**Cut line:** A (0.25) + B (1.0) = 1.25 person-months, leaving 0.25 spare. Not this quarter: C, D, E, F.

**Sanity check**
- F feels strategic to the user but scores last because of 2.0 months of effort and low confidence. If F is a strategic bet, make it a separate decision, not a ranking.
- Impact and confidence are guesses; re-score A, B and E after five customer calls.
