# Sources

- **Structure:** ladder (Monday default)
- **Angle:** good: a public shortener like Bitly (the vendor controls the destination forever), better: short links on a domain you own (a stale CNAME to a lapsed domain can still be taken), best: plain redirects hosted on your main site and kept in your repo (only as safe as your domain renewal).
- **HN thread:** https://news.ycombinator.com/item?id=50511395 (319 points, 161 comments, #9 on the front page, 2026-11-16 07:03 America/Edmonton)
- **Article:** [Old Bitly links hijacked in Burger King, McDonald's and Trump tweets](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/) by the Ransomnews Research Team (ransomnews.com), 2026-11-15.
- **Image:** the article's own header graphic ("A 2011 Burger King tweet now links to a list of Nazi camps."), Ransomnews's own work. Cropped for slide 1; uncropped on the LinkedIn card.

## Facts used
- A Bitly link in a 24 July 2011 Burger King tweet (bit.ly/19BFiM) was created again on 15 Nov 2026 05:32 UTC and pointed at Wikipedia's list of Nazi concentration camps; a 7 June 2011 McDonald's link (bit.ly/mLWJO0) was created again 18 minutes earlier and pointed at the 9/11 article (Ransomnews).
- Nobody posted from either company's account; the links changed hands on Bitly's side (Ransomnews).
- Of 97 Bitly links in Trump tweets 2009 to 2013, 56 were created after the tweets they sit in (49 recreated to the expected destination, 7 elsewhere), plus one blocked (Ransomnews).
- Bitly's help pages say back-halves cannot be reused; Bitly confirmed the issue on X on 15 Nov, suspended the accounts involved and is disabling the affected links (Ransomnews).

## Thread points used
- Two developers described old CNAME records pointing at domains that were let go and later bought by spammers or malware operators (Better level's limit).
- Run shorteners on your own domain; QR code services should generate a direct URL to something you own (Best level / rule).
- Counterpoint: whether you trust the company making the link or the shortener is a stability bet either way; Bitly has outlived many startups that used it.
