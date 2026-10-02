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
4. **Write the carousel** as `posts/YYYY-MM-DD-short-slug/spec.json` (YYYY-MM-DD is the posting date), using `posts/2026-09-23-dont-read-what-you-didnt-write/spec.json` for the `profile` block (keep it exactly as in that file) and the examples below for the slide text format.
   - 6 to 10 slides. Slide 1 is the hook: why a developer should care, plus the HN signal (rank, comments). **It's the highest-leverage slide** — most people decide whether to keep swiping right there — so make it hit hardest: a bold question or claim as paragraph 1, every paragraph a single short sentence, paired with an image. The last slide asks one specific question that invites people to share experiences, and asks them to save the post.
   - One idea per slide. Each slide's `text` is **2 or 3 short, direct paragraphs**, separated by a blank line (`\n\n` in the JSON string). Keep every paragraph to **one short sentence, roughly 8 to 20 words**. No compound sentences, no padding, no throat-clearing — if a paragraph needs "and" or a comma to hold two ideas, split it or cut one.
   - Add an `"image"` to most slides (a photo from the article, or clearly related to the topic — see "Getting an image" below), whether the slide has 2 or 3 paragraphs; this is the default, reference-matched format. Use a `"bullets"` list of 2 to 4 short, direct points instead of an image only on a slide where there's no good image. Don't add both `image` and `bullets` to the same slide.
   - Bold (`**like this**`) can be used more than once per slide where it helps a reader scan, not capped at one. It can wrap a short phrase inside a paragraph, or the whole paragraph when the paragraph itself is the punchline (e.g. a bold hook question as paragraph 1, or a bold one-line takeaway as the last paragraph).
   - A `panel` (the dark number/quote callout) is still available for variety, at most 3 slides, if you want a big stat or line to stand on its own instead of an image; keep panel text very short (a title, a number with a caption, or a short line). A slide takes at most one of `panel`, `bullets`, `image`.
   - Facts, numbers and quotes come only from the article or the thread, attributed to their author. Never invent a statistic, source, or detail.
   - The take is practical: what this means for the reader's work, what to do differently. Include at least one counterpoint from the thread when there's a real one.
   - First-person claims about the owner's own experience ("in my team we...") must not be invented. Keep the voice first person, but any sentence that states something about his personal experience goes on the REVIEW.md checklist.

   Slide examples:
   ```json
   {"text": "**Short bold hook question?**\n\nOne short sentence here.\n\nOne more short sentence, with **one bold phrase**.",
    "image": "posts/2026-10-02-example/assets/article-photo.jpg"}
   ```
   ```json
   {"text": "One short sentence.\n\nAnother short sentence.",
    "bullets": ["First short, direct point.", "Second short, direct point.", "Third short, direct point."]}
   ```
   ```json
   {"text": "One short sentence.\n\nAnother short sentence.\n\nA closing short sentence."}
   ```

   **Getting an image.** Run `python3 fetch_image.py <article_url> posts/<folder>/assets/<name>.jpg` to pull the article's `og:image`. It prints the saved path on success, or `NO_IMAGE_FOUND` / `FETCH_FAILED` on failure — use `bullets` on that slide instead when it fails. Image paths in `spec.json` are relative to the repo root, same as `profile.avatar`. An `image` slide renders full-bleed: no side margin, flush to the bottom edge of the slide, like a photo card under the text, not inset like the `panel`/`bullets` box.
5. **Humanize.** Run the humanizer skill (`.claude/skills/humanizer`) in embedded mode over all slide text and the caption. Apply the edits to `spec.json`.
6. **Render.** Run `python3 carousel.py posts/<folder>/spec.json posts/<folder>/`. Open the PNGs and check that no text overflows and each slide reads well. Fix and re-render if needed.
7. **Write the other files** in the same folder:
   - `caption.txt`: one hook line, two short paragraphs with the practical take, the question, a source credit line ("Source: <title> by <author> (<domain>), via Hacker News."), then 3 to 5 hashtags. No em dashes.
   - `sources.md`: HN thread link (`https://news.ycombinator.com/item?id=<id>`, which `hn_brief.py top` uses to skip covered stories) with points, comments and rank; article link.
   - `REVIEW.md`: checkboxes for every claim about the owner, every number to double-check, and any slide you're unsure about.
8. **Write the LinkedIn assets**, every run, in the same folder. This is a manual-post asset for the owner, not something this workflow publishes itself; there's no LinkedIn API integration here.
   - `linkedin.png`: one 1080x1080 quote card, not a slide, with no profile header and no paragraph body text. One short line, roughly 10 words or fewer, plus an optional one-line caption. When the carousel has a real photo (its `image` slide, not an illustration you generated), reuse that same image file here too: `linkedin_card.py "Big line" "optional small caption" posts/<folder>/linkedin.png posts/<folder>/assets/<name>.jpg` renders the bold hook line on white at the top and the photo full-bleed beneath it, matching the Instagram slide-1 look. With no 4th argument it falls back to the original dark-gradient gold-serif panel style (`carousel.py`'s `draw_panel`). Open the PNG and confirm nothing overflows before committing.
   - `linkedin.txt`: the same hook line as the image, then two short paragraphs (the HN ranking/recency and the claim in one sentence, then the owner's own take or rule in a sentence or two), a closing question, the same source line format as `caption.txt`, and 3 to 5 hashtags, each part separated by a blank line. Run the humanizer over it.
   - The hook (on both files) must differ from that day's Instagram slide 1 and caption hook, and from the immediately preceding post's LinkedIn hook. See `ROUTINE.md` for the scheduled routine's specific hook-rotation and voice rules; follow those when running under that routine, and use your own judgment otherwise.
9. **Commit and push.** Follow "Publish to GitHub" below with the commit message `post: <folder>`.
10. **Send to Metricool for review.** Follow "Send to Metricool" below, scheduled for 11:00 AM on the posting date. If that time has already passed, use the next Monday, Wednesday or Friday at 11:00 AM.
11. **Notify the owner.** Send a push notification saying the post is waiting for approval in Metricool, with the posting date and time, the story title, the Metricool planner link, the number of open items in `REVIEW.md`, the raw GitHub URL to `linkedin.png`, and the full text of `linkedin.txt` inline so both can be copied straight into a manual LinkedIn post. If push notifications aren't available, send an email to arxdsilva@gmail.com with the same content instead.
12. **Finish** with a short summary: which story, why it was chosen over the others, what needs review, and the Metricool planner link.

## Publish to GitHub

1. Delete any `slide_NN.png` left over from an earlier render with more slides.
2. Stage only the post folder (`git add posts/<folder>/`), including `REVIEW.md`, `linkedin.png` and `linkedin.txt`, which stay in the repo as a record. `metricool.json` is gitignored and stays local. Commit with the given message and run `git push origin main`. Never commit anything outside that folder, and never amend, force-push, or skip hooks. If the push fails, report the error and stop.
3. Take the commit SHA (`git rev-parse HEAD`) and build the slide URLs in order: `https://raw.githubusercontent.com/arxdsilva/hn-carousels/<sha>/posts/<folder>/slide_NN.png`, plus the LinkedIn image URL the same way: `.../posts/<folder>/linkedin.png`. Use the SHA, not `main`, so a rewrite never serves Metricool (or the owner) a cached older image.
4. Check that each URL, including `linkedin.png`, returns HTTP 200 (`curl -sI`). A fresh push can take a minute to show up, so retry a few times before reporting a URL as unreachable and stopping.

## Send to Metricool

Post as an Instagram carousel: brand id `7070774`, timezone America/Edmonton, `media` set to the slide URLs in order, `text` set to the contents of `caption.txt`, and `instagramData.isAiGenerated` set to false.

1. Create it with `createScheduledPostForReview`, reviewer `arxdsilva@gmail.com`, approval system `all`. It publishes only after the owner approves it in the Metricool UI.
2. If that fails because the plan has no review flow, create it with `createScheduledPost` and `draft: true` instead, so it sits in the planner until the owner schedules it by hand. Never create a post that isn't a draft or in review.
3. Save the returned `id`, `uuid`, publish date and planner link to `posts/<folder>/metricool.json`.

## Rewrite a post

Run this only when the owner asks, for example "rewrite posts/<folder>: <what to change>" or "rewrite the latest post". "Latest" means the newest folder in `posts/` by date.

1. **Edit.** Apply the owner's feedback to `spec.json` and `caption.txt`, following the same slide rules as the scheduled run. Run the humanizer over any text you changed. Update `REVIEW.md` for any new claim or number.
2. **Re-render** with `carousel.py` and check the PNGs as in the scheduled run.
3. **Update the LinkedIn assets** if the rewrite changes the topic, claim, or hook: edit `linkedin.txt` and re-render `linkedin.png` with `linkedin_card.py`, following the same rules as step 8 of the scheduled run. If the rewrite only fixes a typo or small wording and the hook still holds, leave them as they are.
4. **Commit and push.** Follow "Publish to GitHub" with the commit message `post: <folder> (rewrite)`.
5. **Update Metricool.** Read `posts/<folder>/metricool.json` (or find the post with `getScheduledPosts` by date if the file is missing). Update the post with `updateScheduledPost` using the new slide URLs and caption, keeping every other field as it was. If it was in review, send it back with `sendScheduledPostForReview` using the same reviewer and approval system. Save the new `id` to `metricool.json`.
6. **Notify** the owner as in the scheduled run, saying the rewrite is waiting for approval. If the LinkedIn assets changed, include the refreshed `linkedin.png` URL and `linkedin.txt` text so the owner can re-post manually.

## Never
- Never open news.ycombinator.com pages directly. Use `hn_brief.py`.
- Never publish directly. Every Metricool post is either in review or a draft until the owner approves it in the Metricool UI.
- Never delete a Metricool post, and never change the publish date unless the owner asks.
- Never commit or push anything outside the post folder being published.
- Never delete or edit earlier folders in `posts/` unless the owner asks for a rewrite of that folder.
- Never commit or push a post folder without its `linkedin.png` and `linkedin.txt`, unless the owner explicitly says to skip LinkedIn for that post.
