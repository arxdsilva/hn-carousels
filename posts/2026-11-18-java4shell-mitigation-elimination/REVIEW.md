# Review before posting

- [ ] Image: Calif's own artwork for the write-up (pixel-art Spock with "All your Base64 are belong to us", by Michal Zalewski). Credited in caption.txt and linkedin.txt. The crop keeps the caption band and a hand; it's a Star Trek likeness, so decide if you're fine reusing it.
- [ ] Slide 2 and every file say -XX:-UseBASE64Intrinsics works as the bridge until patching. That's Calif's own recommendation; "it also starts fine on ARM" comes from one developer in the thread and HotSpot's flag being platform independent. Double-check before posting.
- [ ] "Oracle shipped the patch on Nov 17" (Calif: OpenJDK advisory + Oracle patch, 1:00pm PT Nov 17, 2026). Your distro (Temurin, Corretto...) may lag; the thread said Temurin hadn't shipped yet.
- [ ] "You pay with slower Base64" in linkedin.txt is general knowledge (it disables hardware-accelerated Base64), not a measured number.
- [ ] "My rule" in linkedin.txt (patch Java clients too, because of the TLS client-side exploit Calif describes) is written in your voice. Confirm it's yours.
- [ ] linkedin.txt says "#3 on HackerNews this week" (rank at 07:02 Wednesday). Adjust if it moved.
- [ ] x_extra.txt #1: myth call "GEO won't win back the clicks AI Overviews take", based on Revscope's numbers (0.62 to 0.37 clicks per search in Agarwal and Sen's experiment; AI assistants 0.3% of traffic in March). Agree with the stance?
- [ ] x_extra.txt credits Revscope and Cloudflare as organizations; neither article shows a byline in the extract.
