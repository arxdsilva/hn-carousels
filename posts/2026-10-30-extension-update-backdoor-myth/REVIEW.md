# Review checklist: 2026-10-30-extension-update-backdoor-myth

- [ ] Myth call: "the fixed update removes the backdoor" is false, because 2.1.313 wrote an attacker SSH key (svc-telemetry) to ~/.ssh/authorized_keys plus LaunchAgent / scheduled-task persistence, and Kevin Beaumont says he confirmed the replacement versions don't remove them. Cursor also says uninstalling may not be enough. Agree, or flip it? Strongest counter: Cursor says the SSH-enable step failed without admin rights on most macOS and Windows hosts, and the attacker server is offline.
- [ ] Your rule (opinion, no experience claimed): slide 2 "My rule: a bad extension means checking the whole machine."; linkedin.txt rule line. OK to state as yours?
- [ ] Attribution is contested: Beaumont says "Anthropic got compromised" and the build was on Anthropic's verified account; Cursor says the version "was not developed by Anthropic". The post avoids saying who was breached. Keep it that way until Anthropic publishes something.
- [ ] "5,000": Cursor says "at most 5,000 users were affected" (Cursor marketplace). Beaumont says the VS Code build was hit too, so the true total may differ. Used in linkedin.png / linkedin.txt hook as "5,000".
- [ ] Version numbers 2.1.313 (bad) and 2.1.314 (fixed) are from Phorion, Cursor and Beaumont.
- [ ] "ran as soon as the file loaded, before the extension activated" is from Phorion.
- [ ] Incident is under 24 hours old. Re-check for an Anthropic statement before approving; it may change the framing.
- [ ] linkedin.txt opens with "#2 on HackerNews this week" (rank #2 at 07:05 MDT on 2026-10-30).
- [ ] x_extra.txt: Mistral license quote is from a thread comment quoting the license; Raymond Chen fix (pushd/popd) is from his post.
