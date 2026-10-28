Structure: elimination
Angle: Waiting for Apple's macOS update fails (27.2 shipped without the fix), removing the bad roots by hand once fails (27.2 undid it), removing them and rechecking with the one-line git test after every update works.

- HN thread: https://news.ycombinator.com/item?id=50271640 (260 points, 111 comments, rank #1 on the 2026-10-28 front page).
- Article: [Apple's git still trusts the compromised eMudhra certificates](https://emudhra.we-have-a-problem.com/apple.html) by Dennis Jackson (emudhra.we-have-a-problem.com), 2026-10-28. Background: https://emudhra.we-have-a-problem.com/ (eight compromised eMudhra intermediates, blocked on Apple products since 2026-10-22).
- Plans A and B come from the article: Apple notified 2026-10-17; macOS 27.2 (2026-10-26) did not fix it and undid the manual workaround; Apple's guidance says updates may revert the fix. Plan C (repeat the checks and workaround after every update, consider macOS CI runners) is the article's own advice.
- Apple's statement (linked in the thread): https://support.apple.com/en-us/149555. Tools that check /etc/ssl/cert.pem skip Apple's block and revocation checks.
- Counterpoints (thread): one developer said the threat is overblown since an attacker needs a MITM position; a reply said a phish, DNS poisoning or a hacked access point is enough. One suggested moving git remotes to SSH; a reply said SSH only trades CAs for trusting the host key on first use. One replaced /etc/ssl/cert.pem with MacPorts' bundle.
- Slide 1: fetch_image.py returned NO_IMAGE_FOUND, so slide 1 uses a panel and linkedin.png uses the dark panel style.
