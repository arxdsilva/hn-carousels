# Review checklist

## Claims to verify against source
- [ ] Slide 2 / caption: "built fast with an AI coding assistant" is drawn from a commit message visible in the article text ("🤖 Generated with Claude Code", co-authored by David Collantes) plus two commenters asking "Vibecoded?" / "clearly." The specific tool is named in the commit but the slide keeps it generic ("an AI coding assistant") rather than naming it. Confirm that's the right call.
- [ ] Slide 5: "No answer showed up in the docs" is based on the article text as fetched (truncated at ~1800 words) not covering spam/abuse mitigation, and no reply to commenter xena's question in the top-level thread addressing it. The project's full docs (docs/PROTOCOL.md etc.) weren't checked beyond what the fetch returned — worth a quick look before this goes out in case it's addressed elsewhere.
- [ ] Slide 6: "Every new protocol restarts the hardening clock at zero" is this account's own framing of the reuse-vs-rebuild point raised by commenters rixed and RobotToaster (who suggested building on atproto/ActivityPub/Matrix instead), not a direct quote from the thread.

## Sourcing
- [ ] No personal full name was found for the project's author; the HN/git handle "prologic" (git.mills.io/prologic) is used for the source credit, same pattern as the DAWO post's project-style attribution. Confirm that's acceptable.

## Slides to double check
- [ ] Slide 3: "a poorly specified implementation of half of XMPP" is commenter Conlectus's opinion, presented as one developer's view rather than settled fact — confirm the framing reads clearly as an argument, not a verified claim.
