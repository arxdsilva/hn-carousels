# HN carousel workflow

This folder produces Instagram carousels for @arxdsilva, plus LinkedIn assets for the same post: a senior/staff software engineer giving practical takes on what's hot on Hacker News. Audience: working software developers. Language: English. Timezone: America/Edmonton.

Nothing here is ever published without the owner's approval. Each scheduled run writes a draft to `posts/`, pushes it to the public GitHub repo (https://github.com/arxdsilva/hn-carousels, branch `main`) so Metricool can read the slides, and sends it to Metricool for review. The owner approves or rejects it in the Metricool UI, and can ask for a rewrite later (see "Rewrite a post").

Posting days are Monday, Wednesday and Friday. A run may happen on the posting day itself or the day before (Sunday, Tuesday, Thursday) so the owner has time to review. Folder names always use the **posting** date, not the run date.

## The core rule: the post is the lesson, not the news

The engineering accounts that grow fastest on LinkedIn (ByteByteGo, Nikki Siapno, Neo Kim, Raul Junco) almost never post news. Their best posts are lessons people save: "How X works", "X vs Y", or a new event tied to an old engineering problem. Roundups and link-heavy posts are their weakest performers. Opinions on industry news win on comments.

So the HN story is the **trigger and the evidence**, never the headline. Every post is one of three types, and the type decides the hook, the slide structure and the ending.

## The three post types

### Type A: Rediscovered ("X just rediscovered Y")

A new event, tool or incident from HN, connected to an old, well-known engineering problem. Reference: Raul Junco, "AI agents just rediscovered the dual-write problem."

- **Fits:** postmortems, outages, "how we built X" write-ups, migrations, a new tool that hits a classic limit (consistency, caching, retries, queues, N+1, clock skew, backpressure, cache invalidation, idempotency).
- **Hook formula (slide 1, paragraph 1):** `**[New thing] just rediscovered [old problem].**` or `**[Company] hit the oldest bug in [area].**`
- **Slide structure:**
  1. Hook + one-line what happened + HN signal.
  2. What happened, in plain terms (from the article only).
  3. Name the old problem and say where it has shown up before.
  4. Why it happens (the mechanism, one idea per slide; 1–2 slides).
  5. The known fixes or patterns (bullets work well here).
  6. Counterpoint from the thread.
  7. The rule to take away, in bold.
  8. Closing question + save.

### Type B: Explainer ("How X works" / "X vs Y")

When the HN story is about a technology, explain the technology itself. The story is the reason to explain it today. Reference: Alex Xu ("How SSH Works", "MCP vs Function calling"), Nikki Siapno ("Docker vs Kubernetes"), Neo Kim ("If you want to get good at X, learn these N concepts").

- **Fits:** a new release or protocol, a deep-dive article, a technology the thread is confused or arguing about, a "why is X fast/slow" post.
- **Hook formula:** a plain title, no clever wording. One of: `**How [X] works**`, `**[X] vs [Y]**`, `**[N] things to know before you use [X]**`, `**If you want to get good at [X], learn these [N] ideas**`. Paragraph 2 says in one sentence why it matters right now (the HN story).
- **Slide structure:**
  1. Title hook + why now + HN signal.
  2. The one-sentence definition.
  3. How it works, step by step (2–4 slides; bullets for steps, image or panel for the key moment).
  4. For "X vs Y": a side-by-side comparison slide using bullets, then "when to pick which".
  5. The common mistake or misconception (counterpoint from the thread goes here).
  6. Cheat-sheet summary slide: 3–4 bullets someone would screenshot.
  7. Closing question + save.

### Type C: Hot take (an opinion on what HN is arguing about)

When the thread is a debate, take a clear side. Reference: Gergely Orosz on DHH and hand-written code (121 comments), John Crickett on reviewing agent code (76 comments). This type is built for comments, which decide reach in the first hour.

- **Fits:** threads where comments are split, career and practice debates, "AI will replace X" claims, controversial engineering opinions, big-name statements.
- **Hook formula:** `**[Person/company] says [claim]. [I think they're right / half right / wrong].**` or `**Unpopular opinion: [claim].**` The stance must be one sentence.
- **Slide structure** (shorter: 6–8 slides):
  1. Hook with the stance + HN signal.
  2. The claim, fairly stated and attributed.
  3. Where it's right.
  4. Where it breaks (the take; 1–2 slides).
  5. The strongest opposing comment from the thread, quoted and attributed.
  6. What to actually do on Monday.
  7. A question that asks people to pick a side + save.
- **The stance is a draft.** Always add it to `REVIEW.md` as a checkbox ("Stance: I think X. Do you agree?") so the owner confirms or flips it before it goes out.

## Picking the type for the day

Each posting day has a default type, so the feed gets a mix every week:

| Posting day | Default type |
|---|---|
| Monday | B (Explainer) — a save-worthy post to start the week |
| Wednesday | A (Rediscovered) |
| Friday | C (Hot take) — debates do better heading into the weekend |

1. Use the day's default type if any story in the top 10 fits it well.
2. If none fits, use the type that fits the best story, but never the same type as the previous post (check `type` in the newest `posts/*/spec.json`). If the newest post has no `type` field (it predates this rule), there's no type to avoid — pick freely.
3. Record the type in `spec.json` as a top-level `"type": "A" | "B" | "C"` field and in `sources.md`.

## When a scheduled run starts

1. **Day check.** Get today's date in America/Edmonton and work out the posting date:
   - Monday, Wednesday or Friday: the posting date is today.
   - Sunday, Tuesday or Thursday: the posting date is tomorrow.
   - Saturday: say so and stop without creating anything.
2. **Don't duplicate.** If a folder for the posting date already exists in `posts/`, stop.

## Steps

1. **Read the front page.** Run `python3 hn_brief.py top`. It lists the top 10 stories with rank, id, points and comment counts, and leaves out any story already linked in a `posts/*/sources.md`.
2. **Pick the type and the story together.** Start from the day's default type (see "Picking the type for the day"). Among the top 10, choose the story that best fits that type and that a working developer can act on or form an opinion about: engineering practice, tools, careers, security incidents, AI in development, architecture, performance. Skip politics, non-tech stories, and plain product launches unless there's a clear practical angle. Break ties by comment count. Before writing, state the angle in one line: for A, "[new thing] rediscovered [old problem]"; for B, the exact title; for C, the one-sentence stance. If you can't write that line, the story doesn't fit the type; try another story or type.
3. **Research it.** Run `python3 hn_brief.py story <id>` for the article text and the top comments with their first reply. Note the strongest counterpoints from commenters. For type C, also note the strongest comment on each side. Fetch the article URL directly only if the script prints `ARTICLE: could not fetch`.
4. **Write the carousel** as `posts/YYYY-MM-DD-short-slug/spec.json` (YYYY-MM-DD is the posting date), using `posts/2026-09-23-dont-read-what-you-didnt-write/spec.json` for the `profile` block (keep it exactly as in that file), the slide structure for the chosen type above, and the examples below for the slide text format. Add the top-level `"type"` field.
   - 6 to 10 slides (type C: 6 to 8). Slide 1 is the hook, written with the type's hook formula. **It's the highest-leverage slide** — most people decide whether to keep swiping right there — so make it hit hardest: the bold title, claim or stance as paragraph 1, every paragraph a single short sentence, paired with an image. The HN signal (rank, comments) goes in slide 1 as a short supporting line, never as the hook itself. The hook names the lesson or the stance, not the news event.
   - The last slide asks one specific question and asks people to save the post. Match the question to the type: A, "Where have you hit [old problem]?"; B, "What would you add?" or "Which do you use, X or Y?"; C, a question that asks them to pick a side.
   - One idea per slide. Each slide's `text` is **2 or 3 short, direct paragraphs**, separated by a blank line (`\n\n` in the JSON string). Keep every paragraph to **one short sentence, roughly 8 to 20 words**. No compound sentences, no padding, no throat-clearing — if a paragraph needs "and" or a comma to hold two ideas, split it or cut one.
   - Add an `"image"` to most slides (a photo from the article, or clearly related to the topic — see "Getting an image" below), whether the slide has 2 or 3 paragraphs; this is the default, reference-matched format. Use a `"bullets"` list of 2 to 4 short, direct points instead of an image only on a slide where there's no good image, and on the type B steps, comparison and cheat-sheet slides and the type A fixes slide, where bullets are the point. Don't add both `image` and `bullets` to the same slide.
   - Bold (`**like this**`) can be used more than once per slide where it helps a reader scan, not capped at one. It can wrap a short phrase inside a paragraph, or the whole paragraph when the paragraph itself is the punchline (e.g. a bold hook as paragraph 1, or a bold one-line takeaway as the last paragraph).
   - A `panel` (the dark number/quote callout) is still available for variety, at most 3 slides, if you want a big stat or line to stand on its own instead of an image; keep panel text very short (a title, a number with a caption, or a short line). It works well for the type C opposing-comment slide and the type A "old problem" name. A slide takes at most one of `panel`, `bullets`, `image`.
   - Facts, numbers and quotes come only from the article or the thread, attributed to their author. Never invent a statistic, source, or detail. For type A, any claim about where the old problem showed up before must be general engineering knowledge or come from the thread; never invent a specific incident.
   - The take is practical: what this means for the reader's work, what to do differently. Include at least one counterpoint from the thread when there's a real one.
   - First-person claims about the owner's own experience ("in my team we...") must not be invented. Keep the voice first person, but any sentence that states something about his personal experience goes on the REVIEW.md checklist, and so does the stance in a type C post.

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
5. **Humanize.** Run the humanizer skill (`.claude/skills/humanizer`) in embedded mode over all slide text and the caption. Apply the edits to `spec.json`. Keep the type's hook formula intact; the humanizer can change wording, not the shape of the title.
6. **Render.** Run `python3 carousel.py posts/<folder>/spec.json posts/<folder>/`. Open the PNGs and check that no text overflows and each slide reads well. Fix and re-render if needed.
7. **Write the other files** in the same folder:
   - `caption.txt`: one hook line, two short paragraphs with the practical take, the question, a source credit line ("Source: <title> by <author> (<domain>), via Hacker News."), then 3 to 5 hashtags. No em dashes.
   - `sources.md`: the post type (A, B or C) and the one-line angle from step 2; HN thread link (`https://news.ycombinator.com/item?id=<id>`, which `hn_brief.py top` uses to skip covered stories) with points, comments and rank; article link.
   - `REVIEW.md`: checkboxes for every claim about the owner, the stance (type C), every number to double-check, and any slide you're unsure about.
8. **Write the LinkedIn assets**, every run, in the same folder. These are manual-post assets for the owner, not something this workflow publishes itself; there's no LinkedIn API integration here.
   - `linkedin.pdf` (types A and B): the rendered slides combined into one PDF, in order, for a LinkedIn document (carousel) post: `python3 -c "import glob,sys;from PIL import Image;f=sorted(glob.glob(sys.argv[1]+'/slide_*.png'));i=[Image.open(x).convert('RGB') for x in f];i[0].save(sys.argv[1]+'/linkedin.pdf',save_all=True,append_images=i[1:])" posts/<folder>`. Open it and check the page count matches the slides. Type C posts skip the PDF; on LinkedIn they go out as text plus the quote card.
   - `linkedin.png`: one 1080x1080 quote card, not a slide, with no profile header and no paragraph body text. One short line, roughly 10 words or fewer, plus an optional one-line caption. For types A and B this is the backup single-image version of the post, so the owner can test the PDF against the single image; for type C it's the only image. When the carousel has a real photo (its `image` slide, not an illustration you generated), reuse that same image file here too: `linkedin_card.py "Big line" "optional small caption" posts/<folder>/linkedin.png posts/<folder>/assets/<name>.jpg` renders the bold hook line on white at the top and the photo full-bleed beneath it, matching the Instagram slide-1 look. With no 4th argument it falls back to the original dark-gradient gold-serif panel style (`carousel.py`'s `draw_panel`). Open the PNG and confirm nothing overflows before committing.
   - `linkedin.txt`, written for the type:
     - **First line:** a title in the type's hook formula, the same line as `linkedin.png`. It's all most people see before "…more", so it must stand alone.
     - **Body, type A:** one sentence on what happened (with the HN ranking), one naming the old problem, then 3 to 5 numbered lines of what to do about it.
     - **Body, type B:** one sentence on why now (with the HN ranking), then 4 to 7 numbered points, each as `N Term` on one line and `↳ one-line explanation` on the next.
     - **Body, type C:** the stance, the claim being answered (attributed), where it's right, where it breaks, in 4 to 6 short lines. No list.
     - **Ending, all types:** the type's closing question on its own line; then "Repost if this helps someone on your team."; then "Follow Arthur Silva for practical takes on what engineers are talking about."; then the same source line format as `caption.txt`; then at most 3 hashtags. No emoji anywhere in `linkedin.txt`.
     - **No links anywhere in `linkedin.txt`.** Links in the post body cut reach. If the owner wants the article link, it goes in a comment after the first hour (mention this in the notification).
     - Separate each part with a blank line. Run the humanizer over it.
   - The hook (on all LinkedIn files) must differ from that day's Instagram slide 1 and caption hook, and from the immediately preceding post's LinkedIn hook, while still following the type's hook formula. See `ROUTINE.md` for the scheduled routine's specific hook-rotation and voice rules; follow those when running under that routine, and use your own judgment otherwise. Where they conflict with this file's type formulas, the type formulas win.

8b. **Write the X assets**

These are manual-post assets for the owner. There's no X API integration here; nothing is published.

Why X is different. On X, multi-page carousels don't exist and reposted LinkedIn content performs poorly. What gets bookmarked on X is long text that states a principle or lesson, a single explainer diagram with a plain title, and first-hand "I tried it" notes. News on X is mostly covered by quoting the source's own post and adding a short take. Replies drive same-day reach; bookmarks drive lasting reach.

`x.txt` is the X version of the day's post, written for its type (A, B or C from `spec.json`).

Format of the file:

```
TYPE: A|B|C
QUOTE TARGET: <who to quote, e.g. "the article author's or company's own post announcing this, if one exists; otherwise post standalone">
IMAGES: <slide filenames to attach, in order, or "none">

<post part 1>
---
<post part 2>
---
<post part 3, etc.>

REPLY:
<the reply the owner posts under it>
```

- **Parts.** Write the post as 1 to 6 parts separated by a line containing only `---`. Every part must be 280 characters or fewer, and part 1 must stand alone as a complete post. The owner can paste the parts as one long post or as a thread.
- **First line.** The first line of part 1 is the hook and follows the type's hook formula from "The three post types". On X it should be blunter and shorter than on LinkedIn.
- **Type A (Rediscovered), 3 to 6 parts.** Open with the parallel, for example `The last time [X] happened was [era/system]. We're about to relearn the same lesson.` or `[New thing] just rediscovered [old problem].` Then what happened (from the article), the old problem and why it happens, the fix or rule in one bold-free plain sentence, and one counterpoint from the thread. `IMAGES:` slide 1.
- **Type B (Explainer), 1 to 3 parts.** Part 1 is just the title (`How X works`, `X vs Y`) plus one line on why it matters now. The images do the explaining. `IMAGES:` up to 4 slides: the cheat-sheet slide first, then the 1 to 3 slides that best show how it works. Optional part 2: the numbered points in `N Term: one-line explanation` form, kept under 280 characters.
- **Type C (Hot take), 1 to 2 parts.** Open with `Hot take:` or the stance itself in one sentence. Then where the claim is right, where it breaks, and a closing question that asks people to pick a side. Keep the whole thing short; this type is built for replies. `IMAGES:` none, or slide 1 if there's no quote target.
- **Voice.** First person, plain, direct. No hashtags, no emojis, no "🧵", no "A thread:". No em dashes. The same rule as everywhere else applies: never invent the owner's personal experience. Any first-person experience claim or stance goes on `REVIEW.md`.
- **Sources.** Name the article's author and site in the body when you cite something ("per <author> at <site>"). Facts, numbers and quotes come only from the article or the HN thread.
- **`REPLY:`** One line with the article link, plus a short pointer like "Full breakdown in the carousel on Instagram/LinkedIn (@arxdsilva)." Links go in the reply, never in the post parts.
- **Quote target.** Describe who to quote (the author, the company, or the project's official account). Don't guess a handle or URL. The owner finds and quotes the post if it exists.
- Run the humanizer over every part and the reply.

`x_extra.txt` covers the volume gap: X rewards posting much more often than three times a week.

- Write 2 extra standalone posts about 2 other stories from the same `hn_brief.py top` list (not the main story). Pick stories a working developer would have an opinion on.
- For each, run `python3 hn_brief.py story <id>` and base the post only on the article and thread.
- Each post is one part, 280 characters or fewer, written as type A or C (the best fit), with a `REPLY:` line holding the article link. Separate the two posts with a line containing only `===`, and put `TYPE:` and `QUOTE TARGET:` lines above each.
- Run the humanizer over both.
- Record both stories in `x_sources.md` (HN thread link, points, comments, rank, article link), not in `sources.md`, so they stay eligible as future main posts.

Before committing, check every part in both files is 280 characters or fewer (count with `python3 -c "import sys;[print(len(p.strip()),p.strip()[:40]) for p in open(sys.argv[1]).read().split('---')]" posts/<folder>/x.txt` and fix any that are over).
9. **Commit and push.** Follow "Publish to GitHub" below with the commit message `post: <folder>`.
10. **Send to Metricool for review.** Follow "Send to Metricool" below, scheduled for 11:00 AM on the posting date. If that time has already passed, use the next Monday, Wednesday or Friday at 11:00 AM.
11. **Notify the owner.** Send a push notification saying the post is waiting for approval in Metricool, with the posting date and time, the post type and its one-line angle, the story title, the Metricool planner link, the number of open items in `REVIEW.md` (calling out the stance for type C), the raw GitHub URLs to `linkedin.pdf` (types A and B) and `linkedin.png`, the full text of `linkedin.txt` inline so it can be copied straight into a manual LinkedIn post, and a reminder to reply to comments in the first hour and to add the article link as a comment only after that hour. Also include the full text of `x.txt` and `x_extra.txt`, the raw GitHub URLs of the images listed under `IMAGES:` in `x.txt`, and the `QUOTE TARGET:` line, so the owner can post to X by hand. If push notifications aren't available, send an email to arxdsilva@gmail.com with the same content instead.
12. **Finish** with a short summary: which story and type, why it was chosen over the others, what needs review, and the Metricool planner link.

## Publish to GitHub

1. Delete any `slide_NN.png` left over from an earlier render with more slides.
2. Stage only the post folder (`git add posts/<folder>/`), including `REVIEW.md`, `linkedin.png`, `linkedin.txt`, `x.txt`, `x_extra.txt`, `x_sources.md` and (types A and B) `linkedin.pdf`, which stay in the repo as a record. `metricool.json` is gitignored and stays local. Commit with the given message and run `git push origin main`. Never commit anything outside that folder, and never amend, force-push, or skip hooks. If the push fails, report the error and stop.
3. Take the commit SHA (`git rev-parse HEAD`) and build the slide URLs in order: `https://raw.githubusercontent.com/arxdsilva/hn-carousels/<sha>/posts/<folder>/slide_NN.png`, plus the LinkedIn file URLs the same way: `.../posts/<folder>/linkedin.png` and `.../posts/<folder>/linkedin.pdf`. Use the SHA, not `main`, so a rewrite never serves Metricool (or the owner) a cached older image. Also build the raw URLs for the slides listed under `IMAGES:` in `x.txt` the same way; they're already part of the slide list above, so there's nothing new to upload.
4. Check that each URL, including the LinkedIn files, returns HTTP 200 (`curl -sI`). A fresh push can take a minute to show up, so retry a few times before reporting a URL as unreachable and stopping.

## Send to Metricool

Post as an Instagram carousel: brand id `7070774`, timezone America/Edmonton, `media` set to the slide URLs in order, `text` set to the contents of `caption.txt`, and `instagramData.isAiGenerated` set to false.

1. Create it with `createScheduledPostForReview`, reviewer `arxdsilva@gmail.com`, approval system `all`. It publishes only after the owner approves it in the Metricool UI.
2. If that fails because the plan has no review flow, create it with `createScheduledPost` and `draft: true` instead, so it sits in the planner until the owner schedules it by hand. Never create a post that isn't a draft or in review.
3. Save the returned `id`, `uuid`, publish date and planner link to `posts/<folder>/metricool.json`.

## Rewrite a post

Run this only when the owner asks, for example "rewrite posts/<folder>: <what to change>" or "rewrite the latest post". "Latest" means the newest folder in `posts/` by date. The owner may also ask to change the type ("make it a hot take"); then rebuild the slides with that type's structure and hook formula and update the `type` field and `sources.md`.

1. **Edit.** Apply the owner's feedback to `spec.json` and `caption.txt`, following the same slide rules and the post's type as in the scheduled run. Run the humanizer over any text you changed. Update `REVIEW.md` for any new claim, number or stance.
2. **Re-render** with `carousel.py` and check the PNGs as in the scheduled run.
3. **Update the LinkedIn assets** if the rewrite changes the type, topic, claim, or hook, or changes any slide (types A and B: rebuild `linkedin.pdf` from the new slides): edit `linkedin.txt` and re-render `linkedin.png` with `linkedin_card.py`, following the same rules as step 8 of the scheduled run. If the rewrite only fixes a typo or small wording in the caption and the hook still holds, leave them as they are. If the rewrite changes the type, topic, claim or hook, also rewrite `x.txt` following step 8b.
4. **Commit and push.** Follow "Publish to GitHub" with the commit message `post: <folder> (rewrite)`.
5. **Update Metricool.** Read `posts/<folder>/metricool.json` (or find the post with `getScheduledPosts` by date if the file is missing). Update the post with `updateScheduledPost` using the new slide URLs and caption, keeping every other field as it was. If it was in review, send it back with `sendScheduledPostForReview` using the same reviewer and approval system. Save the new `id` to `metricool.json`.
6. **Notify** the owner as in the scheduled run, saying the rewrite is waiting for approval. If the LinkedIn assets changed, include the refreshed `linkedin.pdf` / `linkedin.png` URLs and `linkedin.txt` text so the owner can re-post manually.

## Never
- Never open news.ycombinator.com pages directly. Use `hn_brief.py`.
- Never publish directly. Every Metricool post is either in review or a draft until the owner approves it in the Metricool UI.
- Never delete a Metricool post, and never change the publish date unless the owner asks.
- Never commit or push anything outside the post folder being published.
- Never delete or edit earlier folders in `posts/` unless the owner asks for a rewrite of that folder.
- Never commit or push a post folder without its `linkedin.png` and `linkedin.txt` (and `linkedin.pdf` for types A and B), unless the owner explicitly says to skip LinkedIn for that post.
- Never write a roundup ("5 things on HN this week") or a post whose hook is just the news headline. One story, one lesson or stance.
- Never put a link in `linkedin.txt`.
- Never put an emoji in `linkedin.txt`.
- Never commit or push a post folder without its `x.txt`, unless the owner explicitly says to skip X for that post.
- Never cross-post the Instagram/LinkedIn carousel to X as-is. X gets its own text written for the platform.
- Never add stories used in `x_extra.txt` to `sources.md`. They go in `x_sources.md` so they stay available as future main posts.
