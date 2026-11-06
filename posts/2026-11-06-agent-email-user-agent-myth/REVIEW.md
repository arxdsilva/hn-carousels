# Review checklist: 2026-11-06-agent-email-user-agent-myth

- [ ] Myth call: "your coding agent only sends what you typed" is false, because Claude Code put the signed-in account email in the model's context and subagents sent it in User-Agent headers (a Claude Code team member confirmed the context part in the HN thread). Agree, or flip it? Strongest counter: it isn't a default header; it mostly happened when sites like the SEC require a contact email in the User-Agent.
- [ ] Your rule (opinion, no experience claimed): "anything in the agent's context is something it can send" (slide 2, linkedin.txt, which adds "so check what leaves your machine"). OK to state as yours?
- [ ] This is the second Claude Code story in a week (after 2026-10-30). Fine, or prefer a different story?
- [ ] "53": one user on the GitHub issue said they found 53 tool calls with their email in a User-Agent, mostly subagents running curl -A. Used on slide 1 panel, linkedin.png, linkedin.txt, x.txt.
- [ ] "name, team and repo": from one HN commenter's server logs (e.g. "Claude Code agent run by <name>, <company> platform team").
- [ ] Fix status: Claude Code team member said the email is being removed from context in the next release (early next week); a contributor said built-in mod cc-plugin-privacy blocks it from 2.1.317. Re-check before approving; it may have shipped.
- [ ] SEC claim: an HN commenter showed the SEC API rejects requests without an email in the User-Agent.
- [ ] Article was fetched via a summarizing fetch (github.com 403'd the scripts); issue author "taylor-edwards", opened Nov 5 2026.
- [ ] linkedin.txt opens with "#3 on HackerNews this week" (rank #3 at ~07:00 MST on 2026-11-06).
- [ ] x_extra.txt: sshole details (257 to 1024 char passwords, Alpine cloud images, OpenSSH 10.6p2 fix) are from sshhole.com; Paint version numbers from the CVE thread comments (cve.org page needs JS, not verified directly), and "Windows Update showed nothing" is one commenter's report.
