Structure: myth
Angle: Myth: a CVSS 9.8 means you patch tonight. Wrong because the score assumes a remote, no-login attacker; OpenSSL's EVP_EncodeBlock() overflow needs ~1.6 GB base64-encoded in one call and only affects OpenSSL 4.0/4.1, so exposure decides the date.

- HN thread: https://news.ycombinator.com/item?id=50569226 (296 points, 230 comments, rank #4 on the 2026-11-20 front page).
- Article: [OpenSSL PR #33652: Buffer overflow in EVP_EncodeBlock() (CVE-2026-121481)](https://github.com/openssl/openssl/pull/33652) by the OpenSSL project (github.com). Page returned 403 to the scripts.
- Assessment linked in the thread: https://tldrcve.com/openssl-encodeblock/ (CISA 9.8 vs Ubuntu Medium, affected versions, ~1.6 GB threshold).
- No image: the PR page couldn't be fetched (403), so slide 1 uses a panel.
