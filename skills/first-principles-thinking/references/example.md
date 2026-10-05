# Example: First Principles Thinking (light path)

Illustrative case. All details are invented.

**User:** "Every competitor offers a 99.99% uptime SLA, so we need one too, which means a multi-region setup. Is that actually necessary?"

**Reconstruction target:** the belief that we must offer 99.99% uptime and run multi-region.
**Pass:** Surface, Question, Bedrock, Rebuild, Implications.

**Surface**
- Convention: "competitors offer 99.99%, so customers expect it."
- Hidden comparison: our customers equal the competitors' customers.

**Question**
- **Assumption:** customers will not buy without 99.99%. **Why believed?** analogy to competitors. **What if false?** we avoid a costly architecture.
- **Assumption:** 99.99% requires multi-region. **Why believed?** common advice. **What if false?** one region with good failover may be enough.

**Bedrock**
- `[FUNDAMENTAL]` 99.99% allows about 52 minutes of downtime per year (arithmetic).
- `[FUNDAMENTAL]` Our contracts with two customers mention availability (user supplied).
- `[ASSUMPTION]` Other prospects need the same SLA.
- `[ASSUMPTION]` Our past outages would have been prevented by a second region.

**Rebuild**
1. Two known contracts set the actual requirement; read what level they state.
2. The cause of past outages decides whether a second region helps, so check the incident history.
3. Only if both point to multi-region is multi-region justified.

**Implications**
- So what: decide the SLA from contracts and outage causes, not from competitors' marketing pages.
- Cost of being wrong: if prospects do need 99.99% and we do not offer it, we lose some deals; if we over-build, we carry multi-region cost and complexity for little benefit.
- vs convention: convention starts from the architecture; this starts from the requirement.
