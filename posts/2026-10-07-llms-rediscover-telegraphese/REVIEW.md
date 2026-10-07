# Review checklist — 2026-10-07-llms-rediscover-telegraphese (Type A: Rediscovered)

## Claims about the owner
- [ ] Slide 7 / linkedin.txt: "My rule: compress for the model, not the person." — stated as the owner's own rule, not an invented anecdote, but confirm he's comfortable publishing it as his stance.

## Numbers and facts to double-check
- [ ] "Cuts output tokens by up to 49%" (slide 1) — the article's own top figure (GLM-5.3-Flash's writer savings, "48.4% savings with the lowercase instruction"); 49% is the qwen3.8-27b writer figure in the article's table. Worth confirming you want the max across models rather than the author's own headline number (40.4-48.9% range).
- [ ] "$10 a word" / "1866" (slide 3 panel) — from the article: "$100 for ten words" on the first transatlantic cable, "$10 a word, ten-word minimum, roughly $2,600 in today's money." Sourced to the article, not independently verified against a primary telegraph-history source.
- [ ] "Output tokens cost three to five times more than input tokens" (slide 7) — the article's own claim ("Output tokens cost 3-5x input tokens... at any major API"), not independently checked against current API pricing pages.
- [ ] Slide 6 panel quote ("Just AI slop dressed up as caveman-speak.") — a paraphrase of commenter jubilanti's line ("Just another AI slop version of the old 'caveman' dialect."), not a word-for-word quote. Flagging since it's presented in quotation marks.

## Image
- [ ] No image: `fetch_image.py` returned `NO_IMAGE_FOUND` for the article URL. All slides use text, bullets or a panel instead. `linkedin.png` uses the routine's default dark-panel style with no photo.
