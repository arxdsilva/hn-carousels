# Review checklist: 2026-11-13-dependency-cooldown-myth

- [ ] Myth call: "updating to the newest dependency version right away is safest" is false, because malicious versions are usually caught within hours or days (Rust Release Team), so a short cooldown waits out the riskiest window. Agree, or flip it? Strongest counter: the Rust team itself says cooldowns are no complete defense, and `cargo install` ignores the setting (a commenter asked why; a Cargo maintainer said it was for usability and consistency with the MSRV-aware resolver).
- [ ] Your rule (opinion, no experience claimed): "let new versions age a few days before they reach your build" (slide 2), plus "keep the override for urgent fixes" (linkedin.txt). OK as yours?
- [ ] "3 days": the value in the article's example `.cargo/config.toml` (`global-min-publish-age = "3 days"`), not a recommendation from the Rust team. Used on slide 1 panel, caption question.
- [ ] "3 hours": from the article's sample `cargo update` output ("cc v1.18.0, published 3 hours ago"). Used in the caption hook, linkedin.txt and linkedin.png.
- [ ] Tool names (general knowledge, not from the article): Renovate's `minimumReleaseAge` and Dependabot's `cooldown` setting, in linkedin.txt. Confirm both still exist under those names.
- [ ] Override: article shows `CARGO_RESOLVER_INCOMPATIBLE_PUBLISH_AGE=allow cargo update clap --precise 4.6.9` (slide 2 "one env var").
- [ ] linkedin.txt opens with "#5 on HackerNews this week" (rank #5 at ~07:40 MST on 2026-11-13).
- [ ] x_extra.txt: the outage timing (investigating 09:58 UTC, resolved 11:58 UTC) is from the status page; the zigzag repo page returned 403 to the scripts, so that post rests on the title and the thread only.
