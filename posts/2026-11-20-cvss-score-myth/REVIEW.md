# Review checklist: 2026-11-20-cvss-score-myth

- [ ] Myth call: "a CVSS 9.8 means you patch tonight" is false, because the score assumes a remote attacker with no login, while this bug needs ~1.6 GB base64-encoded in one call and only hits OpenSSL 4.0/4.1. Agree, or flip it? Strongest counter: apps bundle their own OpenSSL (tldrcve notes Ubuntu flags Node.js on 22.04), so "my distro is on 3.x" isn't proof you're safe. Other side from the thread: one developer is tired of dropping everything for CVEs that turn out minor; another sees every patched bug as software getting better.
- [ ] Your rule (opinion, no experience claimed): "the score sets the ceiling, and your exposure sets the date" (slide 2, linkedin.txt, x.txt). OK as yours?
- [ ] "1.6 GB": tldrcve says "about 1.6 GB" ((INT_MAX / 4) * 3 bytes); the top HN comment said "~1.5GB" (that's the GiB figure). Used on slide 1 panel, slide 2, caption, linkedin.png/txt, x.txt.
- [ ] "9.8 is CISA's score", "Ubuntu rates it Medium", "only 4.0.0-4.0.3 and 4.1.0": from the tldrcve assessment linked in the thread (tldrcve.com/openssl-encodeblock), not from the PR itself. The PR page returned 403, so I couldn't read it directly. Fix expected in 4.1.1/4.0.4 on 1 Dec 2026 (not used in the post).
- [ ] "Most distros still ship 3.x": from thread comments (4.2 is the first 4.x LTS; Arch/Fedora are on 4.x).
- [ ] Source line credits "the OpenSSL project" for PR #33652; swap in the PR author's name if you prefer.
- [ ] linkedin.txt opens with "#4 on HackerNews this week" (rank #4 at ~07:00 MST on 2026-11-20).
- [ ] x_extra.txt: Frostbite numbers (4.59x perf/W, 25 workloads, in-order dual-issue baseline) are from Architect Labs' post; "humans picked the workloads and built the checker" is one commenter's point. Sokoban: ~430 subagents, 24 world-first solves, frozen verifier are from Andrew Healey's post.
