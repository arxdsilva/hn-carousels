# Scheduled routine: HN carousel draft (Mon/Wed/Fri)

This file is the instruction set given to the scheduled cloud session that runs this
workflow automatically. It runs in a fresh cloud checkout of this repo on branch
`main`, on Mondays, Wednesdays and Fridays. It layers on top of `CLAUDE.md`: where
the two disagree, this file wins for the scheduled run. `CLAUDE.md` remains the
reference for a manual/interactive run and for the mechanics (day check, HN
research, humanizing, rendering, publishing to GitHub, sending to Metricool,
rewrites).

Keeping this versioned means the routine's behavior is auditable and diffable like
any other code change, instead of living only in the scheduler's own config.

## Positioning (overrides CLAUDE.md wherever they conflict)

- Hacker News is where you find topics, not the subject of the post. Each carousel
  and blog post is about the discussion itself: the idea, the trade-off, what
  developers disagree on, and what it means for their work.
- Don't mention Hacker News, rankings, points or comment counts in slides, captions
  or blog posts, unless the fact that developers are arguing about it is itself the
  point. At most once, never as the hook.
- Slide 1 hooks on the problem or the claim, not on where it was posted.
- Always credit the original article's author when you use their ideas, facts or
  numbers. Refer to commenters' views as "developers in the discussion" or "one
  engineer argued", without usernames.
- Caption source line: "Source: <title> by <author> (<domain>)."

## Steps

1. Run `pip3 install pillow trafilatura`.
2. Follow `CLAUDE.md` in the repo root, starting with the day check in
   America/Edmonton. It covers research with `hn_brief.py`, writing and humanizing
   the carousel, rendering with `carousel.py`, committing and pushing only the new
   post folder to `main`, sending the post to Metricool for review (brand id
   `7070774`, reviewer `arxdsilva@gmail.com`), and notifying the owner.
   `sources.md` still records the HN thread link, so covered stories get skipped.
3. Blog post. Only after the carousel was sent to Metricool successfully:
   1. Clone `https://github.com/insurgencylabs/ytwebsite` (private) next to this
      repo. If the clone fails, skip the blog, mention the error in the owner
      email, and finish.
   2. Learn the site's conventions: framework, blog posts folder, filename
      pattern, frontmatter fields, build command, and the style of the 3 most
      recent posts.
   3. Write a new post in that format, 800-1200 words, on the same topic as
      today's carousel. Go deeper than the carousel: my practical take, the
      strongest counterpoints from the discussion, and what a developer should do
      differently. Credit and link the original article. Never copy passages
      from the source.
   4. Use the create-content skill for the title, meta description, slug and
      heading structure, without keyword stuffing. Use schema-markup only if the
      site doesn't already generate article schema. Then run
      brand-voice-enforcement (if `.claude/brand-voice-guidelines.md` exists) and
      humanizer on the text.
   5. Nobody reviews the blog before it goes live, so: first-person opinions are
      fine ("I think", "my advice"), but never invent personal experiences or
      anecdotes about me or my team. Every fact, number and quote must come from
      the article or the discussion. If the article couldn't be fetched, skip the
      blog for this run.
   6. Install dependencies and run the site's build. If the build fails, don't
      push; include the error in the owner email.
   7. Commit only the new post as `blog: <slug>` and push to `main` of ytwebsite.
4. The owner email covers both: the carousel (topic, why it was picked, Metricool
   status) and the blog (title, file path, commit link, or why it was skipped).

## Cloud-specific notes

- Push notifications aren't available here. Notify the owner by sending an email
  to arxdsilva@gmail.com with the Gmail connector.
- `posts/<folder>/metricool.json` is gitignored, so it won't persist after this
  run. That's expected; still write it.
- If `git push` to hn-carousels fails (for example, missing credentials), don't
  send anything to Metricool and don't write the blog. Email the owner the error
  and stop.
- Never publish a post directly. Every Metricool post must be in review or a
  draft.
- Never edit or delete existing posts in either repo.
