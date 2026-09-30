# Review checklist — 2026-09-30-what-your-ai-agent-can-see

No claims about the owner's own experience are made in this post.

## Facts to double-check (sourced from HN comments, article was unfetchable — HTTP 403)

- [ ] Slide 2/panel 4: the claim that OpenAI's Dots sandbox presented an OpenAI-issued TLS certificate for gmail.com (MITM) comes from one commenter's (chen_dev) own test, quoted verbatim in the thread. Not independently verified against OpenAI's documentation, since the article itself couldn't be fetched.
- [ ] Slide 3: "most browsers on Linux don't pin certificates" is a commenter's (mintflow) claim, not independently verified.
- [ ] Slide 5: paraphrase of a commenter's (jjcm) argument that domain-specific always-on agents avoid context overload and create a "barrier of trust" — check the paraphrase is fair to the original.
- [ ] Slide 6: paraphrase of a commenter's (mike_hearn) description of running his own agents ("Codexes") in dedicated Unix accounts wired to a Maildir mailbox — check "mailbox" fairly represents "Maildir."
- [ ] Slide 7: paraphrase of a commenter's (abeppu) observation that community consensus on agent trust has shifted in recent months.

## Slides to sanity-check before approving

- [ ] Slide 4 (MITM panel): confirm the tone reads as informative, not alarmist, given we can't verify OpenAI's official explanation for the interception.
- [ ] Overall: this post is built entirely from thread commentary since openai.com/index/introducing-dots/ returned HTTP 403 on every fetch attempt. Worth a manual read of the article if it becomes reachable before this goes live.
