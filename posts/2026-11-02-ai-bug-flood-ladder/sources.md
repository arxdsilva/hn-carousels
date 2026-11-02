# Sources

- **Structure:** ladder (Monday default)
- **Angle:** good: triage AI-found bug reports by severity with a cut-off, better: pause feature work until the backlog shrinks, best: run the same bug hunt on every PR before merge, with a human reviewing the fixes.
- **HN thread:** https://news.ycombinator.com/item?id=50312408 (588 points, 361 comments, #2 on the front page, 2026-11-02 07:20 America/Edmonton)
- **Article:** [Postgres 19 is late, and it's AI's fault](http://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html) by Robert Haas (rhaas.blogspot.com), originally published at https://neon.com/blog/postgres-19-is-late-and-its-ais-fault
- **Image:** Neon's header image for the same article (og:image of the neon.com version), cropped to a 1080x460 strip.

## Facts used
- Back-patched commits to the release branch: 724 (REL_18_STABLE, Apr 8 to Sep 25, 2025) vs 1169 (REL_19_STABLE, same window, 2026), "more than 60%" (Haas).
- Three features reverted between Aug 27 and Sep 15: UPDATE/DELETE FOR PORTION OF, SQL/PGQ, ALTER TABLE MERGE/SPLIT PARTITION (Haas).
- LLM-drafted fixes "aren't always correct or compliant with PostgreSQL standards" and still need human review (Haas).

## Thread points used
- Triage by priority with a cut-off, leaving niche bugs ignored (top-level comment).
- One company put a full halt on feature work because of the volume of urgent security tasks (reply in thread).
- Warnings treated as errors and strict compiler settings while fixing thousands of bugs on a 1.5M-line codebase (top comment).
- Discovery isn't the bottleneck anymore; verification is (top-level comment): used as the X counterpoint.
