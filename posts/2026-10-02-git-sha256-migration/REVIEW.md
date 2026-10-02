# Review checklist — 2026-10-02-git-sha256-migration

## Claims about the owner
- [ ] Slide 7 / linkedin.txt: "My rule: map the real attack path first." — stated as the owner's own rule, not an invented anecdote, but confirm he's comfortable publishing it as his stance.

## Numbers and facts to double-check
- [ ] Scott Chacon identified as "GitHub's co-founder" — confirmed by the article's own byline (blog.gitbutler.com), which also credits him as a GitButler co-founder and author of Pro Git.
- [ ] $40k figure (slide 2 bullets) — Chacon's own rhetorical number in the article for a hypothetical maintainer payoff, not a documented real-world incident.
- [ ] "GitHub still has no public SHA-256 support" (slide 5) — true per the HN thread as of this writing (SHA-256 support is in closed beta); could go stale if GitHub ships it.
- [ ] SHAttered (2017) and SHA-1 is a Shambles (2020) attack names/dates — taken directly from the article, not independently re-verified here.
- [ ] FIPS 140-2 banning SHA-1 (slide 7 panel) — sourced from a commenter's claim in the thread, not the article itself; worth a sanity check before this goes out if it needs to be airtight.

## Slides I'm less sure about
- [ ] Slide 6: paraphrases Git's official hash-function-transition docs via a commenter's summary (GrantMoyer) rather than the docs directly — accurate to the thread, but double-check against git-scm.com/docs/hash-function-transition if precision matters.

## Image
- [ ] Slide 1's image (`assets/article.jpg`) is the article's own hero illustration, pulled from its `og:image` via `fetch_image.py`. It's the article's own promotional art, not a photo we have separate rights to — flagging in case that matters for how this gets posted.
