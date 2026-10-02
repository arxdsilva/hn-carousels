# Review checklist — 2026-10-02-git-sha256-migration (Type C: Hot take)

## Stance
- [ ] **Stance (slide 1 / caption / linkedin.txt): "Scott Chacon says Git's SHA-256 migration is a costly mistake. I think he's half right."** Right that trust was never about the hash and real attacks don't need to crack it; wrong to call the migration purely unnecessary, since compliance rules (FIPS 140-2) force it at some firms regardless of any exploit. Confirm you agree with this stance, or tell me which way to flip it (fully agree / fully disagree with Chacon) and I'll rebuild the carousel around that instead.

## Claims about the owner
- [ ] Slide 7 / linkedin.txt: "My rule: map your real attack path first." — stated as the owner's own rule, not an invented anecdote, but confirm he's comfortable publishing it as his stance.

## Numbers and facts to double-check
- [ ] Scott Chacon identified as GitHub's co-founder and the author of Pro Git — confirmed by the article's own byline (blog.gitbutler.com).
- [ ] "GitHub still has no public SHA-256 support" (slide 5) — true per the HN thread as of this writing (SHA-256 support is in closed beta); could go stale if GitHub ships it.
- [ ] FIPS 140-2 banning SHA-1 (slide 4) — sourced from a commenter's claim in the thread, not the article itself; worth a sanity check before this goes out if it needs to be airtight.
- [ ] Slide 6 panel quote ("A practical proof of concept.") — a shortened, close paraphrase of commenter kpcyrd's line that SHAttered "was specifically a pratical proof of concept," not a word-for-word quote. Flagging since it's presented in quotation marks.

## Image
- [ ] Slide 1's image (`assets/article.jpg`) is the article's own hero illustration, pulled via `fetch_image.py`'s `og:image` fetch, also reused on `linkedin.png`. It's the article's own promotional art, not something we have separate rights to.
