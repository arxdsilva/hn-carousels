# Review before posting

- [ ] Numbers from Rida F'kih's article: 60 Hz default cap; MessageChannel loop locked to vsync = 80 reads/s; free-running loop = 50,000 reads/s with 80 distinct values; empty rAF loop = ~90 reads/s; hidden smooth-scroller pushes ProMotion to 120 Hz; OffscreenCanvas (transferControlToOffscreen) renders at 120 FPS. Quick check against the article.
- [ ] Slide 1 says "from 60 to 120 FPS". Strictly, input reaches 120 Hz and canvas rendering reaches 120 FPS; the plain DOM still updates at 60. Fine as a headline?
- [ ] Battery counterpoint (slide 2, x.txt) paraphrases one developer in the thread: native iOS turns on 120 Hz only for large transitions, the web has no switch, so it would be 120 Hz all the time.
- [ ] "My rule" in linkedin.txt (spend 120 Hz only during gestures; measure on a real iPhone with the Timelines tab in Safari's Web Inspector) is written in your voice. Safari Web Inspector is general knowledge, not from the article. Confirm it's yours.
- [ ] linkedin.txt says "#10 on HackerNews this week" (rank at 07:02 Wednesday). Adjust if it moved.
- [ ] LinkedIn hook is a flat Proof result, not the Wednesday question style: the previous run (also a Wednesday) opened with a question, and ROUTINE.md says not to repeat the preceding run's style.
- [ ] Image: the article's own social card from rida.dev (the author's work), cropped for slide 1, full on linkedin.png. It repeats the article title.
- [ ] x_extra.txt #1: myth call "a sandboxed agent can't talk to another agent" is false, based on Deshpande's 1,221/1,221 rounds over a shared vLLM server. The thread's top critic says it needs pre-shared protocols and stack knowledge. Agree with the stance?
- [ ] x_extra.txt #2: Bonsai numbers (5.9 GB, SWE-bench Verified 75.6 vs 60.8 vs Qwen3.8 27B 80.6) are PrismML's own; "5 of 8, 29% faster" is one developer's self-made benchmark from the thread.
