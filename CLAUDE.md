# HN carousel workflow

This folder produces Instagram carousels for @arxdsilva: a senior/staff software engineer giving practical takes on what's hot on Hacker News. Audience: working software developers. Language: English. Timezone: America/Edmonton.

Nothing here is ever posted automatically. Each run writes a draft to `posts/` and stops. The owner reviews, edits, and uploads it himself.

## When a scheduled run starts

1. **Day check.** Get today's date in America/Edmonton. If it is not Monday, Wednesday or Friday, say so and stop without creating anything.
2. **Don't duplicate.** If a folder for today's date already exists in `posts/`, stop.

## Steps

1. **Read the front page.** Fetch https://news.ycombinator.com/ and list the top 10 stories with points and comment counts. Read every `posts/*/sources.md` and skip any story already covered.
2. **Pick one story.** Choose the most-discussed story in the top 10 that a working developer can act on or form an opinion about in their own job: engineering practice, tools, careers, security incidents, AI in development, architecture, performance. Skip politics, non-tech stories, and plain product launches unless there's a clear practical angle. Break ties by comment count.
3. **Research it.** Read the full article and the HN comment thread. Note the strongest counterpoints from commenters.
4. **Write the carousel** as `posts/YYYY-MM-DD-short-slug/spec.json`, using `posts/2026-09-23-dont-read-what-you-didnt-write/spec.json` as the format and quality reference. Keep the `profile` block exactly as in that file.
   - 6 to 10 slides. Slide 1 is the hook: why a developer should care, plus the HN signal (rank, comments). The last slide asks one specific question that invites people to share experiences, and asks them to save the post.
   - One idea per slide, at most about 55 words. At most one bold phrase per slide (`**like this**`). At most 3 slides with a `panel`; keep panel text very short (a title, a number with a caption, or a short line).
   - Facts, numbers and quotes come only from the article or the thread, attributed to their author. Never invent a statistic, source, or detail.
   - The take is practical: what this means for the reader's work, what to do differently. Include at least one counterpoint from the thread when there's a real one.
   - First-person claims about the owner's own experience ("in my team we...") must not be invented. Keep the voice first person, but any sentence that states something about his personal experience goes on the REVIEW.md checklist.
5. **Humanize.** Run the humanizer skill (`.claude/skills/humanizer`) in embedded mode over all slide text and the caption. Apply the edits to `spec.json`.
6. **Render.** Run `python3 carousel.py posts/<folder>/spec.json posts/<folder>/`. Open the PNGs and check that no text overflows and each slide reads well. Fix and re-render if needed.
7. **Write the other files** in the same folder:
   - `caption.txt`: one hook line, two short paragraphs with the practical take, the question, a source credit line ("Source: <title> by <author> (<domain>), via Hacker News."), then 3 to 5 hashtags. No em dashes.
   - `sources.md`: HN thread link with points, comments and rank; article link.
   - `REVIEW.md`: checkboxes for every claim about the owner, every number to double-check, and any slide you're unsure about.
8. **Finish** with a short summary: which story, why it was chosen over the others, and what needs review.

## Never
- Never post, schedule, or call any social media tool.
- Never delete or edit earlier folders in `posts/`.
