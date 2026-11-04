# Review checklist: 2026-11-04-car-root-bug-chain

- [ ] Facts from the article: signature check rejected the modified update image; SHEX takes one token, no arguments; writable mounts noexec; LOG path traversal wrote to /proc/sys/kernel/core_pattern; dbus-monitor aborted and the kernel ran payload.sh as root; offset 180 changed to 120 minutes; replacement SD card about 60 EUR.
- [ ] Framing: "Plan A / Plan B / what works" are the author's own attempts, in his order. The "two harmless-looking bugs" line is my read: the article calls them dead ends on their own, not harmless.
- [ ] linkedin.txt "My rule: score a bug by what it can combine with. A log command that writes anywhere is low severity only until it reaches a file the kernel reads." Your rule? Keep, edit or cut.
- [ ] linkedin.txt hook is a question (Wednesday rotation) on the elimination formula: "Signed updates won't stop this root. Neither will noexec. Will your triage?" Both defenses did block his direct attempts; they didn't stop the chain.
- [ ] linkedin.txt opens with "#10 on HackerNews this week" (870 points, 329 comments; posted 2026-11-02).
- [ ] Image is the author's own photo from the article (credited in sources.md). Quick look before posting.
- [ ] x_extra.txt post 1 is a myth call: "a crash bug is just a crash" is false because the PHP2Shell crash bug (reported 2024) became RCE within two weeks of Calif's AI-assisted audit, per IEEE Spectrum. Agree?
- [ ] x_extra.txt post 2 is a myth call: "paying for Gemini keeps your chats out of training" is false per Google's help pages quoted in the thread (personal accounts, Keep Activity on; reviewed chats kept up to three years). Agree?
