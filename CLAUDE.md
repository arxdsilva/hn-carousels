# HN carousel workflow

This folder produces Instagram carousels for @arxdsilva: a senior/staff software engineer giving practical takes on what's hot on Hacker News. Audience: working software developers. Language: English. Timezone: America/Edmonton.

Nothing here is ever published without the owner's approval. Each scheduled run writes a draft to `posts/`, pushes it to the public GitHub repo (https://github.com/arxdsilva/hn-carousels, branch `main`) so Metricool can read the slides, and sends it to Metricool for review. The owner approves or rejects it in the Metricool UI, and can ask for a rewrite later (see "Rewrite a post").

Posting days are Monday, Wednesday and Friday. A run may happen on the posting day itself or the day before (Sunday, Tuesday, Thursday) so the owner has time to review. Folder names always use the **posting** date, not the run date.

## When a scheduled run starts

1. **Day check.** Get today's date in America/Edmonton and work out the posting date:
   - Monday, Wednesday or Friday: the posting date is today.
   - Sunday, Tuesday or Thursday: the posting date is tomorrow.
   - Saturday: say so and stop without creating anything.
2. **Don't duplicate.** If a folder for the posting date already exists in `posts/`, stop.

## Steps

1. **Read the front page.** Run `python3 hn_brief.py top`. It lists the top 10 stories with rank, id, points and comment counts, and leaves out any story already linked in a `posts/*/sources.md`.
2. **Pick one story.** Choose the most-discussed story in the top 10 that a working developer can act on or form an opinion about in their own job: engineering practice, tools, careers, security incidents, AI in development, architecture, performance. Skip politics, non-tech stories, and plain product launches unless there's a clear practical angle. Break ties by comment count.
3. **Research it.** Run `python3 hn_brief.py story <id>` for the article text and the top comments with their first reply. Note the strongest counterpoints from commenters. Fetch the article URL directly only if the script prints `ARTICLE: could not fetch`.
4. **Write the carousel** as `posts/YYYY-MM-DD-short-slug/spec.json` (YYYY-MM-DD is the posting date), using `posts/2026-09-23-dont-read-what-you-didnt-write/spec.json` as the format and quality reference. Keep the `profile` block exactly as in that file.
   - 6 to 10 slides. Slide 1 is the hook: why a developer should care, plus the HN signal (rank, comments). The last slide asks one specific question that invites people to share experiences, and asks them to save the post.
   - One idea per slide, at most about 55 words. At most one bold phrase per slide (`**like this**`). At most 3 slides with a `panel`; keep panel text very short (a title, a number with a caption, or a short line).
   - Facts, numbers and quotes come only from the article or the thread, attributed to their author. Never invent a statistic, source, or detail.
   - The take is practical: what this means for the reader's work, what to do differently. Include at least one counterpoint from the thread when there's a real one.
   - First-person claims about the owner's own experience ("in my team we...") must not be invented. Keep the voice first person, but any sentence that states something about his personal experience goes on the REVIEW.md checklist.
5. **Humanize.** Run the humanizer skill (`.claude/skills/humanizer`) in embedded mode over all slide text and the caption. Apply the edits to `spec.json`.
6. **Render.** Run `python3 carousel.py posts/<folder>/spec.json posts/<folder>/`. Open the PNGs and check that no text overflows and each slide reads well. Fix and re-render if needed.
7. **Write the other files** in the same folder:
   - `caption.txt`: one hook line, two short paragraphs with the practical take, the question, a source credit line ("Source: <title> by <author> (<domain>), via Hacker News."), then 3 to 5 hashtags. No em dashes.
   - `sources.md`: HN thread link (`https://news.ycombinator.com/item?id=<id>`, which `hn_brief.py top` uses to skip covered stories) with points, comments and rank; article link.
   - `REVIEW.md`: checkboxes for every claim about the owner, every number to double-check, and any slide you're unsure about.
8. **Commit and push.** Follow "Publish to GitHub" below with the commit message `post: <folder>`.
9. **Send to Metricool for review.** Follow "Send to Metricool" below, scheduled for 11:00 AM on the posting date. If that time has already passed, use the next Monday, Wednesday or Friday at 11:00 AM.
10. **Notify the owner.** Send a push notification saying the post is waiting for approval in Metricool, with the posting date and time, the story title, the Metricool planner link, and the number of open items in `REVIEW.md`. If push notifications aren't available, send an email to arxdsilva@gmail.com with the same content instead.
11. **Finish** with a short summary: which story, why it was chosen over the others, what needs review, and the Metricool planner link.

## Publish to GitHub

1. Delete any `slide_NN.png` left over from an earlier render with more slides.
2. Stage only the post folder (`git add posts/<folder>/`), including `REVIEW.md`, which stays in the repo as a record. `metricool.json` is gitignored and stays local. Commit with the given message and run `git push origin main`. Never commit anything outside that folder, and never amend, force-push, or skip hooks. If the push fails, report the error and stop.
3. Take the commit SHA (`git rev-parse HEAD`) and build the slide URLs in order: `https://raw.githubusercontent.com/arxdsilva/hn-carousels/<sha>/posts/<folder>/slide_NN.png`. Use the SHA, not `main`, so a rewrite never serves Metricool a cached older image.
4. Check that each URL returns HTTP 200 (`curl -sI`). A fresh push can take a minute to show up, so retry a few times before reporting a URL as unreachable and stopping.

## Send to Metricool

Post as an Instagram carousel: brand id `7070774`, timezone America/Edmonton, `media` set to the slide URLs in order, `text` set to the contents of `caption.txt`, and `instagramData.isAiGenerated` set to false.

1. Create it with `createScheduledPostForReview`, reviewer `arxdsilva@gmail.com`, approval system `all`. It publishes only after the owner approves it in the Metricool UI.
2. If that fails because the plan has no review flow, create it with `createScheduledPost` and `draft: true` instead, so it sits in the planner until the owner schedules it by hand. Never create a post that isn't a draft or in review.
3. Save the returned `id`, `uuid`, publish date and planner link to `posts/<folder>/metricool.json`.

## Rewrite a post

Run this only when the owner asks, for example "rewrite posts/<folder>: <what to change>" or "rewrite the latest post". "Latest" means the newest folder in `posts/` by date.

1. **Edit.** Apply the owner's feedback to `spec.json` and `caption.txt`, following the same slide rules as the scheduled run. Run the humanizer over any text you changed. Update `REVIEW.md` for any new claim or number.
2. **Re-render** with `carousel.py` and check the PNGs as in the scheduled run.
3. **Commit and push.** Follow "Publish to GitHub" with the commit message `post: <folder> (rewrite)`.
4. **Update Metricool.** Read `posts/<folder>/metricool.json` (or find the post with `getScheduledPosts` by date if the file is missing). Update the post with `updateScheduledPost` using the new slide URLs and caption, keeping every other field as it was. If it was in review, send it back with `sendScheduledPostForReview` using the same reviewer and approval system. Save the new `id` to `metricool.json`.
5. **Notify** the owner as in the scheduled run, saying the rewrite is waiting for approval.

## Never
- Never open news.ycombinator.com pages directly. Use `hn_brief.py`.
- Never publish directly. Every Metricool post is either in review or a draft until the owner approves it in the Metricool UI.
- Never delete a Metricool post, and never change the publish date unless the owner asks.
- Never commit or push anything outside the post folder being published.
- Never delete or edit earlier folders in `posts/` unless the owner asks for a rewrite of that folder.
