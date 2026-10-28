# Review checklist: 2026-10-28-emudhra-macos-git

- [ ] Facts from the article: Apple notified 2026-10-17; as of 2026-10-28 the git, curl and python3 shipped with macOS still trust the compromised certs; macOS 27.2 (released 2026-10-26) didn't fix it and undid the manual workaround; Safari and apps on Apple's networking framework are protected; "eight" intermediates comes from the main incident page.
- [ ] "Ten days" (slide 1 panel, linkedin.txt, x.txt) counts 17 to 28 October, matching the article's title.
- [ ] Plan C ("remove them by hand, then rerun the git check after every update") is the article's advice, framed by me as the plan that works. It's a mitigation until Apple ships the fix, not a cure.
- [ ] linkedin.txt "My rule: put that check in the post-update checklist for every Mac, macOS CI runners included, and use SSH remotes for git where you can." Your rule? Keep, edit or cut. The SSH host-key caveat is from the thread.
- [ ] linkedin.txt opens with "#1 on HackerNews today" (260 points, 111 comments at 13:30 UTC).
- [ ] The article's site is a Mozilla-affiliated author's page; one commenter called its tone toward Apple unfair. The post takes the article's side on the facts.
- [ ] x_extra.txt post 1: 361 of 365 changes reproduced exactly; Munich study 24% vs 87% (one model). Check the numbers.
- [ ] x_extra.txt post 2 is a myth call: "printing untrusted output in a terminal is harmless" is false because Ghostty 1.4 fixed several bugs triggered by just displaying malicious output. Agree?
