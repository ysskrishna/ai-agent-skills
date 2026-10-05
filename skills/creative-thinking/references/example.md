# Example: Creative Thinking (light path)

Illustrative case. All details are invented.

**User:** "We need a name and a first-week activation idea for a CLI tool that explains failing CI logs in plain English."

**Brief:** name plus week-one activation for a developer CLI; audience is working developers; tone is calm and practical; avoid names that sound like another CI vendor.
**Pass:** Prime, Diverge, Connect, Harvest.

**Prime**
- Delight: a developer reads the explanation and fixes the build in under a minute.
- Must not: send logs off the machine without consent.

**Diverge** (triggers: analogy, constraint flip)
1. `F` "Logbook": a notebook metaphor, one entry per failure.
2. `N` "Tl;dr CI": says what it does.
3. `N` Run it on the last failing build automatically, no setup.
4. `W` The tool replies in the voice of an on-call senior engineer.
5. `F` A weekly digest of your three most common failure causes.
6. `N` Analogy (doctor's triage): print "severity, likely cause, next check" first.

**Connect**
- 3 + 6 -> first run shows triage for the latest failed build with zero configuration.
- 5 + 1 -> the "logbook" keeps a local history and produces the weekly digest.

**Harvest**
1. Top picks: (a) "Logbook" with zero-config first run (matches the calm tone); (b) triage output format (fast to scan); (c) weekly digest (gives a reason to come back).
2. Next step: paste five real failing logs into a prototype and time how long a teammate takes to act on the output.
3. Parking lot: on-call voice (fun but risks tone drift); name "Tl;dr CI" (clear but feels jokey).
