# Review checklist: 2026-10-21-neural-networks-already-clean

- [ ] Slide 1 hook says "90% of neurons in a 32B model have one main job". The essay's figure is "roughly 90% of neuron poles" in a preliminary Qwen3-32B audit, and the author says it depends on thresholds and some samples are small. Is "neurons" an acceptable simplification of "neuron poles"? Slide 1 does say "preliminary audit".
- [ ] Numbers to double-check against the essay: ~90% one main job, ~7% two related jobs, ~2-4% not yet understood (Qwen3-32B); 99-100% of the last layer of a retrained InceptionV1 variant easily interpretable (x.txt only).
- [ ] Slide 2 bullet "the cat-and-car neuron detected a shape": the brief says cat and car neurons were really shape detectors. Confirm that wording matches the essay.
- [ ] Slide 2 opinion "A model you can read is a model you can debug." and linkedin.txt "My rule: if I can't read a system, I can't debug it, and models shouldn't get a pass." These are stated as your opinion, not experience. OK to post in your voice?
- [ ] x.txt part 5: first-person opinion ("I care because a model I can read is one I can debug") plus the open-weights argument, which comes from a commenter in the thread. OK in your voice?
- [ ] The slide 1 image is Goodfire's own og:image, cropped (bottom edge of the left city trimmed slightly). Quick look that the crop reads well.
- [ ] linkedin.txt source line contains the domain "already-clean.goodfire.com", same format as earlier posts. LinkedIn may auto-link it; drop the domain if you want zero links.
- [ ] x_extra.txt post 1 is a myth call: "Myth: flat design won because it's easier to use." Evidence is developers in the DEsk discussion (discoverability lessons from 90s/00s user testing), with the counterpoint that skeuomorphism faded for a reason. Agree, or flip it?
- [ ] x_extra.txt post 2 (Krea 3): "4x faster than Nano Banana Pro" is from the title; "10x faster, 3x cheaper than GPT Image 2" is from the page's headline. The page's animated per-image price and seconds didn't scrape cleanly, so they're left out. Confirm the 10x/3x claim on krea.ai/krea-3.

## Rewrite (2026-10-20): new "Presenting solutions" rules

Only linkedin.txt changed (numbered steps). Slides, caption, x.txt and the Metricool draft are unchanged.

- [ ] Steps carry the reason for each fix, not a cost: the essay doesn't give per-step costs, so none are invented. The overall limit ("preliminary audit") sits in the opening line.
- [ ] Step 3 (better metrics) is new to linkedin.txt, from the essay: tools rewarded explanations that simulate activations over ones that are right.
