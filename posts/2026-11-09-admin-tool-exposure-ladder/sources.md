# Sources

- **Structure:** ladder (Monday default)
- **Angle:** good: WAF rules blocking the admin paths, better: real auth on every admin endpoint with no secrets in shipped JavaScript, best: admin tools reachable only through a VPN or identity-aware proxy (public app APIs still need auth).
- **HN thread:** https://news.ycombinator.com/item?id=50419215 (443 points, 208 comments, #9 on the front page, 2026-11-09 07:05 America/Edmonton)
- **Article:** [Unlocking any car from X brand in most of the world](https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/) by Shubham Shah ("Shubs", shubs.io), 2026-11-07, research done with Sam Curry.
- **Image:** the article's own screenshot of the exposed "TEST HARNESS" admin login page (shubs.io/content/images/2026/11/CleanShot-2026-07-24-at-09.35.19@2x.png), cropped for slide 1 and the LinkedIn card. The author's own work.

## Facts used
- Chain (Australia): Plate -> VIN -> Subscriber GUID -> OpenIDM admin credentials in a JS vendor bundle -> path traversal to bypass the WAF -> MFA bypass via ROPC flow -> minting a consumer app token -> remote command API (Shah).
- admintool.<redacted>-telematics.com.au served a login page titled TEST HARNESS; many of its APIs needed only the hardcoded API keys in its JS bundle (Shah).
- The OpenIDM admin credentials were meant for staging but worked in production (Shah).
- Heavy WAF rules blocked /openidm/; /static%2f..%2fopenidm/ wasn't covered, found after GPT 5.6 Sol Ultra spent about six hours on the OpenIDM source (Shah).
- The author asks why the OpenIDM instances were exposed externally at all; the mobile app called some OpenIDM endpoints (e.g. pinService), which is why some had to stay reachable (Shah).
- Combined with Sam Curry's write-up: remote commands for the automaker's vehicles in Australia, the US and Canada.

## Thread points used
- Pair the phone with the car and have the car accept only commands signed by the phone's key, so the maker's servers can't command the car from an account alone (top-level comment): X counterpoint.
- Several top comments question whether cars should be remotely controllable over the internet at all.
