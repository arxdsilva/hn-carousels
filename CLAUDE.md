# HN carousel workflow

> **This file is the current version of these instructions.** The scheduled routine's stored prompt may still embed an older copy (post types A/B/C, "Rediscovered / Explainer / Hot take", 6 to 10 slides). If the prompt that started a run disagrees with this file or `ROUTINE.md`, follow this file and `ROUTINE.md`: five structures, exactly 2 slides.

This folder produces Instagram carousels for @arxdsilva, plus LinkedIn assets for the same post: a senior/staff software engineer giving practical takes on what's hot on Hacker News. Audience: working software developers. Language: English. Timezone: America/Edmonton.

Nothing here is ever published without the owner's approval. Each scheduled run writes a draft to `posts/`, pushes it to the public GitHub repo (https://github.com/arxdsilva/hn-carousels, branch `main`) so Metricool can read the slides, and sends it to Metricool for review. The owner approves or rejects it in the Metricool UI, and can ask for a rewrite later (see "Rewrite a post").

Posting days are Monday, Wednesday and Friday. A run may happen on the posting day itself or the day before (Sunday, Tuesday, Thursday) so the owner has time to review. Folder names always use the **posting** date, not the run date.

## The core rule: the post is the lesson, not the news

The engineering accounts that grow fastest on LinkedIn (ByteByteGo, Nikki Siapno, Neo Kim, Raul Junco) almost never post news. Their best posts are lessons people save: "How X works", "X vs Y", or a new event tied to an old engineering problem. Roundups and link-heavy posts are their weakest performers. Opinions on industry news win on comments.

So the HN story is the **trigger and the evidence**, never the headline. Every post is built on one of five structures, and the structure decides the hook, the slide layout and the ending. The same five structures shape the companion blog post on ytwebsite (its `.claude/CLAUDE.md` §3), so a story keeps one structure on every platform.

## The five structures

Each structure is a short argument in beats. Slide 1 carries the opening beat; slide 2 carries the rest, as bullets.

### 1. Proof: result > what they did > step by step

Lead with an outcome someone can measure, then show how it was reached.

- **Fits:** postmortems with a measured fix, "how we built X" write-ups, migrations, performance work with numbers, a release with a working demo.
- **Hook formula:** `**[Who] [got result, with a number].**` Example: `**Anthropic went from 2,500 to 30,000 merges a day.**` Paragraph 2 says in one sentence what they did.
- **Slides:**
  1. The result and what they did, paired with an image when one exists.
  2. The steps, in order, as 3–4 bullets, each one concrete; then the closing question + save.
- **Closing question:** "Which step would you skip?" or "What would you try first?"
- **"What I did"** means the article's author or company unless the owner supplied the experience. Never invent first-person steps; any first-person line goes on `REVIEW.md`.

### 2. Elimination: not plan A > not plan B > plan C works

The obvious fixes fail, for reasons the reader can see, and one approach holds.

- **Fits:** write-ups where the team tried the standard playbook first (shallow clones, then mirrors, then a rewrite), debugging stories, tool comparisons with a winner.
- **Hook formula:** `**[Plan A] won't fix [problem]. Neither will [plan B].**`
- **Slides:**
  1. The hook and the problem in one line, paired with an image when one exists.
  2. Three bullets: why A fails, why B fails, why C works, each with its reason from the article or thread; then the closing question + save.
- **Closing question:** "Which did you try first?"
- Every failed plan needs a reason from the article or thread. Never invent an attempt the source doesn't describe.

### 3. Myth: common myth > it's not true because

Name a belief the reader probably holds, then take it apart with evidence.

- **Fits:** threads correcting a popular belief, headlines that got the cause wrong ("an AI agent deleted it"), misconceptions about a technology ("deleting cookies stops tracking"), big-name claims the thread disputes.
- **Hook formula:** `**Myth: [common belief].**` Paragraph 2 gives the one-line reason it's wrong.
- **Slides:**
  1. The myth and the short reason, paired with an image when one exists.
  2. Bullets: the evidence it's false (from the article or thread), what's actually true, the strongest opposing comment; then a question that asks people to pick a side + save.
- **Closing question:** a pick-a-side question ("Myth or fair warning?").
- **The myth call is a stance and a draft.** Always add it to `REVIEW.md` as a checkbox ("Myth call: X is false because Y. Agree?") so the owner confirms or flips it before it goes out. Use this structure for posts built for comments.

### 4. Ladder: better > even better > best

Three ways to do the same job, each one better than the last, with what each costs.

- **Fits:** how-tos, explainers of a technology, a new tool that improves on an older one, techniques with clear tradeoffs (retry with backoff, then an idempotency key, then a key plus a ledger constraint).
- **Hook formula:** `**How to [do X]: good, better, best.**` or `**[N] ways to [do X], from good to best.**` Paragraph 2 says in one sentence why it matters right now (the HN story).
- **Slides:**
  1. The hook and the why-now, paired with an image when one exists (a panel if not).
  2. Three bullets, one per rung ("Good: ...", "Better: ...", "Best: ..."), each naming what it buys and what it costs; then the closing question + save.
- **Closing question:** "Which rung are you on?"

### 5. Precondition: nothing will work > unless you do XYZ > what to do

The usual fixes all fail until one basic thing is in place.

- **Fits:** incidents whose root cause is a missing basic (untested backups, no observability, no ownership), adoption failures ("we bought the tool and nothing changed"), AI and tooling stories where the process was the real gap.
- **Hook formula:** `**No [tool or fix] will save you until you [XYZ].**`
- **Slides:**
  1. The hook and what happened in one line, paired with an image when one exists.
  2. Bullets: why the usual fixes fail without XYZ, what XYZ is, the concrete steps to put it in place; then the closing question + save.
- **Closing question:** "Where are you missing [XYZ]?"

### Writing structures 2 and 3

Elimination and Myth are built on "not this". State each beat as its own plain claim with its reason ("Mirrors only bought time: they got harder to run as merges kept climbing."). Don't compress a beat into the "it's not X, it's Y" sentence tic; the humanizer flags that, and it must keep the beats themselves.

## Presenting solutions

Whenever a post hands the reader fixes (the Ladder rungs, the Proof steps, the plan that works in Elimination, what to do in Precondition), each one must be something they could do today. The owner's hand edit of the 2026-10-19 LinkedIn post is the reference:

```
3 ways to stop ad spyware. Your browser extension is the weakest.

#10 on HackerNews last week: spyware reaching devices once a targeted ad rendered.

To protect your devices:
1. Good: an ad blocker in every browser, but it never sees the ads inside apps.

2. Better: turn off the mobile ad ID, through MDM on work phones, which Citizen Lab says directly blocks the vendor's current method.

3. Best: block ads at the gateway, or on the router at home.

My rule: block ads where the traffic leaves the network, so nobody's safety depends on an extension they remembered to install (a DNS filter on the router, like Pi-hole, AdGuard Home or NextDNS).

Which level is your team at?
```

- **Number the fixes.** One fix per numbered item, in order, never run together in a paragraph. Open the list with a short line saying who it protects or what it's for ("To protect your devices:").
- **Each item is the fix plus its limit.** What to do, then in the same sentence what it misses or costs ("but it never sees the ads inside apps").
- **Name the tool.** When a fix is a category ("a DNS filter on the router"), name 2 or 3 real, widely used tools for it (Pi-hole, AdGuard Home or NextDNS). Tool names are general knowledge, not from the article, so list them on `REVIEW.md`. Never name a product you aren't sure exists and does that job.
- **Check the fix does what you claim.** Before writing "covers every device" or "nobody depends on X", check the obvious exceptions: devices off that network, ways around it, what it can't see. Narrow the claim or name the exception rather than overclaim.
- **Keep the setup line short.** The line before the list says what happened in the reader's terms ("spyware reaching devices once a targeted ad rendered"). Credit the source where its fact is used and in the source line; don't stack names into the setup.
- **Reader words, not our words.** "Level", "option" or "step" in reader-facing text, never "rung" or "beat". The structure names are for us.

Myth posts have no fix list and stay in prose.

## Picking the structure for the day

Each posting day has a default, so the feed gets a mix every week:

| Posting day | Default structure |
|---|---|
| Monday | 4 Ladder: a save-worthy post to start the week |
| Wednesday | 1 Proof or 2 Elimination, whichever the best story supports |
| Friday | 3 Myth: debates do better heading into the weekend |

5 Precondition has no day; use it when the story's root cause is a missing basic.

1. Use the day's default if any story in the top 10 fits it well.
2. Otherwise use the structure that fits the best story, but never the same structure as either of the two previous posts (check `structure` in the two newest `posts/*/spec.json`). Posts from before this rule have a `type` field (`A`, `B`, `C`) or nothing; they don't count, so there's nothing to avoid from them.
3. Record it in `spec.json` as a top-level `"structure": "proof" | "elimination" | "myth" | "ladder" | "precondition"` field and in `sources.md`.

## When a scheduled run starts

1. **Day check.** Get today's date in America/Edmonton and work out the posting date:
   - Monday, Wednesday or Friday: the posting date is today.
   - Sunday, Tuesday or Thursday: the posting date is tomorrow.
   - Saturday: say so and stop without creating anything.
2. **Don't duplicate.** If a folder for the posting date already exists in `posts/`, stop.

## Steps

1. **Read the front page.** Run `python3 hn_brief.py top`. It lists the top 10 stories with rank, id, points and comment counts, and leaves out any story already linked in a `posts/*/sources.md`.
2. **Pick the structure and the story together.** Start from the day's default (see "Picking the structure for the day"). Among the top 10, choose the story that best fits that structure and that a working developer can act on or form an opinion about: engineering practice, tools, careers, security incidents, AI in development, architecture, performance. Skip politics, non-tech stories, and plain product launches unless there's a clear practical angle. Break ties by comment count. Before writing, state the angle in one line, in the structure's shape: Proof, "[who] got [result] by [what they did]"; Elimination, "[A] fails, [B] fails, [C] works"; Myth, "Myth: [belief]. Wrong because [reason]"; Ladder, "good: [A], better: [B], best: [C]"; Precondition, "nothing works until [XYZ]". If you can't write that line from the article and thread, the story doesn't fit the structure; try another story or structure.
3. **Research it.** Run `python3 hn_brief.py story <id>` for the article text and the top comments with their first reply. Note the strongest counterpoints from commenters. For Myth, also note the strongest comment on each side. For Elimination, note the reason each failed plan failed. Fetch the article URL directly only if the script prints `ARTICLE: could not fetch`.
4. **Write the carousel** as `posts/YYYY-MM-DD-short-slug/spec.json` (YYYY-MM-DD is the posting date), using `posts/2026-09-23-dont-read-what-you-didnt-write/spec.json` for the `profile` block (keep it exactly as in that file), the slides for the chosen structure above, and the examples below for the slide text format. Add the top-level `"structure"` field.
   - **Exactly 2 images.** Slide 1 is the hook, written with the structure's hook formula. **It's the highest-leverage slide** — most people decide whether to keep swiping right there — so make it hit hardest: the bold result, claim, myth or title as paragraph 1, every paragraph a single short sentence, paired with an image whenever one is available (see "Getting an image" below — reusing an image from the article is the priority, before falling back to a panel). The HN signal (rank, comments) goes in slide 1 as a short supporting line, never as the hook itself. The hook names the lesson or the stance, not the news event.
   - Slide 2 carries the rest of the structure's beats, compressed: the steps, the failed plans and the one that works, the evidence against the myth, the rungs, or the precondition and what to do. It closes with the structure's closing question and asks people to save the post. Because everything lands on one slide, use `bullets` to carry the density (2 to 4 short, direct points — test render and cut a bullet if it overflows, rather than shrinking text past readability) and keep the `text` paragraphs very short.
   - Each slide's `text` is **1 to 3 short, direct paragraphs**, separated by a blank line (`\n\n` in the JSON string). Keep every paragraph to **one short sentence, roughly 8 to 20 words**. No compound sentences, no padding, no throat-clearing — if a paragraph needs "and" or a comma to hold two ideas, split it or cut one. Slide 2's `text` should usually be on the shorter end of that range, since the bullets do most of the work.
   - Add an `"image"` to slide 1 whenever one is available; this is the default, reference-matched format for the hook slide. Use a `"bullets"` list of 2 to 4 short, direct points on slide 1 only when no image exists; slide 2 is almost always `bullets`. Don't add both `image` and `bullets` to the same slide.
   - Bold (`**like this**`) can be used more than once per slide where it helps a reader scan, not capped at one. It can wrap a short phrase inside a paragraph, or the whole paragraph when the paragraph itself is the punchline (e.g. a bold hook as paragraph 1, or a bold one-line takeaway as the last paragraph).
   - A `panel` (the dark number/quote callout) is the fallback for slide 1 when no image exists, or an alternative to bullets on slide 2 if you want one big stat or line to stand on its own (a Proof result works well); keep panel text very short (a title, a number with a caption, or a short line). A slide takes at most one of `panel`, `bullets`, `image`.
   - Facts, numbers and quotes come only from the article or the thread, attributed to their author. Never invent a statistic, source, or detail. Any claim about where a problem showed up before must be general engineering knowledge or come from the thread; never invent a specific incident.
   - The take is practical: what this means for the reader's work, what to do differently. Include at least one counterpoint from the thread when there's a real one and there's room for it on slide 2.
   - First-person claims about the owner's own experience ("in my team we...") must not be invented. Keep the voice first person, but any sentence that states something about his personal experience goes on the REVIEW.md checklist, and so does the myth call in a Myth post.

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

   **Getting an image.** Reusing an image from the article is the priority — generating or sourcing one from elsewhere is a last resort. Run `python3 fetch_image.py <article_url> posts/<folder>/assets/<name>.jpg`. It tries the article's `og:image`/`twitter:image` meta tags first, then falls back to the first substantial `<img>` in the page body (skipping icons, logos and avatars) when no meta image is set — so it reaches for a diagram, screenshot or illustration the article actually embeds, not just its social-preview image. It prints the saved path on success, or `NO_IMAGE_FOUND` / `FETCH_FAILED` on failure — use `bullets` or a `panel` on slide 1 instead when it fails. Open whatever it saves: an image that doesn't crop well into a 1080×460 full-bleed strip (a tall screenshot, a dense multi-panel comic) usually needs a manual crop first — pick the single most legible, self-contained region (one panel, one row, the key screenshot area) rather than the whole source, save that as the asset, and only then reference it from `spec.json`; letting the renderer center-crop a tall or busy image automatically tends to cut through the content that matters. Image paths in `spec.json` are relative to the repo root, same as `profile.avatar`. An `image` slide renders full-bleed: no side margin, flush to the bottom edge of the slide, like a photo card under the text, not inset like the `panel`/`bullets` box. If the reused image isn't the article author's own work (a comic, a chart from elsewhere, a screenshot of another site), credit its real source and license in `caption.txt`, `linkedin.txt` and `sources.md`, and flag it in `REVIEW.md` for a quick look before posting.
5. **Humanize.** Run the humanizer skill (`.claude/skills/humanizer`) in embedded mode over all slide text and the caption. Apply the edits to `spec.json`. Keep the structure's hook formula and its beats intact; the humanizer can change wording, not the shape of the title or the order of the beats.
6. **Render.** Run `python3 carousel.py posts/<folder>/spec.json posts/<folder>/`. Open the PNGs and check that no text overflows and each slide reads well. Fix and re-render if needed.
7. **Write the other files** in the same folder:
   - `caption.txt`: one hook line, two short paragraphs with the practical take, the question, a source credit line ("Source: <title> by <author> (<domain>), via Hacker News."), then 3 to 5 hashtags. No em dashes.
   - `sources.md`: the post's structure and the one-line angle from step 2; HN thread link (`https://news.ycombinator.com/item?id=<id>`, which `hn_brief.py top` uses to skip covered stories) with points, comments and rank; article link.
   - `REVIEW.md`: checkboxes for every claim about the owner, the myth call (Myth), every number to double-check, and any slide you're unsure about.
8. **Write the LinkedIn assets**, every run, in the same folder. These are manual-post assets for the owner, not something this workflow publishes itself; there's no LinkedIn API integration here.
   - `linkedin.pdf`: the rendered slides combined into one PDF, in order, for a LinkedIn document (carousel) post: `python3 -c "import glob,sys;from PIL import Image;f=sorted(glob.glob(sys.argv[1]+'/slide_*.png'));i=[Image.open(x).convert('RGB') for x in f];i[0].save(sys.argv[1]+'/linkedin.pdf',save_all=True,append_images=i[1:])" posts/<folder>`. Open it and check the page count matches the slides.
   - `linkedin.png`: one 1080x1080 quote card, not a slide, with no profile header and no paragraph body text. One short line, roughly 10 words or fewer, plus an optional one-line caption. It's the backup single-image version of the post, so the owner can test the PDF against the single image; for a Myth post the owner may post it alone with the text. When the carousel has a real photo (its `image` slide, not an illustration you generated), reuse that same image file here too: `linkedin_card.py "Big line" "optional small caption" posts/<folder>/linkedin.png posts/<folder>/assets/<name>.jpg` renders the bold hook line on white at the top and the photo full-bleed beneath it, matching the Instagram slide-1 look. With no 4th argument it falls back to the original dark-gradient gold-serif panel style (`carousel.py`'s `draw_panel`). Open the PNG and confirm nothing overflows before committing.
   - `linkedin.txt`, written for the structure:
     - **First line:** a title in the structure's hook formula, the same line as `linkedin.png`. It's all most people see before "…more", so it must stand alone.
     - **Body, Proof:** one sentence on what happened (with the HN ranking), one with the result and its number, then 3 to 5 numbered steps.
     - **Body, Elimination:** one sentence on why now (with the HN ranking), then the three plans as `N Plan` on one line and `↳ why it fails` (or `↳ why it works`, for the last) on the next.
     - **Body, Myth:** the myth, why it's wrong, the evidence (attributed), what's actually true, in 4 to 6 short lines. No list.
     - **Body, Ladder:** one sentence on what happened (with the HN ranking), then a short line opening the list, then the levels as a numbered list (`1. Good: ...`, `2. Better: ...`, `3. Best: ...`), each the fix plus its limit, then the owner's rule naming the tools. See "Presenting solutions".
     - **Body, Precondition:** one sentence on what happened (with the HN ranking), one naming the precondition, then 3 to 5 numbered lines of what to do.
     - **Ending, every structure:** the structure's closing question on its own line; then "Repost if this helps someone on your team."; then "Follow Arthur Silva for practical takes on what engineers are talking about."; then the same source line format as `caption.txt`; then at most 3 hashtags. No emoji anywhere in `linkedin.txt`.
     - **No links anywhere in `linkedin.txt`.** Links in the post body cut reach. If the owner wants the article link, it goes in a comment after the first hour (mention this in the notification).
     - Separate each part with a blank line. Run the humanizer over it.
   - The hook (on all LinkedIn files) must differ from that day's Instagram slide 1 and caption hook, and from the immediately preceding post's LinkedIn hook, while still following the structure's hook formula. See `ROUTINE.md` for the scheduled routine's specific hook-rotation and voice rules; follow those when running under that routine, and use your own judgment otherwise. Where they conflict with this file's hook formulas, the hook formulas win.

8b. **Write the X assets**

These are manual-post assets for the owner. There's no X API integration here; nothing is published.

Why X is different. On X, multi-page carousels don't exist and reposted LinkedIn content performs poorly. What gets bookmarked on X is long text that states a principle or lesson, a single explainer diagram with a plain title, and first-hand "I tried it" notes. News on X is mostly covered by quoting the source's own post and adding a short take. Replies drive same-day reach; bookmarks drive lasting reach.

`x.txt` is the X version of the day's post, written for its structure (from `spec.json`).

Format of the file:

```
STRUCTURE: proof|elimination|myth|ladder|precondition
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
- **First line.** The first line of part 1 is the hook and follows the structure's hook formula from "The five structures". On X it should be blunter and shorter than on LinkedIn.
- **Proof, 2 to 5 parts.** The result with its number, what they did, the steps (one part or one line each), and one counterpoint from the thread. `IMAGES:` slide 1.
- **Elimination, 3 to 5 parts.** The hook, why plan A fails, why plan B fails, what works and why, and one counterpoint from the thread. `IMAGES:` slide 2, then slide 1.
- **Myth, 1 to 2 parts.** Open with `Myth:` and the belief, then why it's wrong in one or two lines, and a closing question that asks people to pick a side. Keep the whole thing short; this structure is built for replies. `IMAGES:` none, or slide 1 if there's no quote target.
- **Ladder, 1 to 3 parts.** Part 1 is the title plus one line on why it matters now. The images do the explaining. `IMAGES:` both slides, slide 2 (the rungs) first, then slide 1. Optional part 2: the rungs in `Good: X. Better: Y. Best: Z.` form, kept under 280 characters.
- **Precondition, 3 to 5 parts.** The hook, what happened (from the article), why the usual fixes fail without the precondition, what to do in one plain sentence, and one counterpoint from the thread. `IMAGES:` slide 1.
- **Voice.** First person, plain, direct. No hashtags, no emojis, no "🧵", no "A thread:". No em dashes. The same rule as everywhere else applies: never invent the owner's personal experience. Any first-person experience claim or myth call goes on `REVIEW.md`.
- **Sources.** Name the article's author and site in the body when you cite something ("per <author> at <site>"). Facts, numbers and quotes come only from the article or the HN thread.
- **`REPLY:`** One line with the article link, plus a short pointer like "Full breakdown in the carousel on Instagram/LinkedIn (@arxdsilva)." Links go in the reply, never in the post parts.
- **Quote target.** Describe who to quote (the author, the company, or the project's official account). Don't guess a handle or URL. The owner finds and quotes the post if it exists.
- Run the humanizer over every part and the reply.

`x_extra.txt` covers the volume gap: X rewards posting much more often than three times a week.

- Write 2 extra standalone posts about 2 other stories from the same `hn_brief.py top` list (not the main story). Pick stories a working developer would have an opinion on.
- For each, run `python3 hn_brief.py story <id>` and base the post only on the article and thread.
- Each post is one part, 280 characters or fewer, written in whichever structure fits a single part best (usually Myth, Precondition or Proof), with a `REPLY:` line holding the article link. Separate the two posts with a line containing only `===`, and put `STRUCTURE:` and `QUOTE TARGET:` lines above each.
- Run the humanizer over both.
- Record both stories in `x_sources.md` (HN thread link, points, comments, rank, article link), not in `sources.md`, so they stay eligible as future main posts.

Before committing, check every part in both files is 280 characters or fewer (count with `python3 -c "import sys;[print(len(p.strip()),p.strip()[:40]) for p in open(sys.argv[1]).read().split('---')]" posts/<folder>/x.txt` and fix any that are over).
9. **Commit and push.** Follow "Publish to GitHub" below with the commit message `post: <folder>`.
10. **Send to Metricool for review.** Follow "Send to Metricool" below, scheduled for 11:00 AM on the posting date. If that time has already passed, use the next Monday, Wednesday or Friday at 11:00 AM.
11. **Notify the owner.** Send a push notification saying the post is waiting for approval in Metricool, with the posting date and time, the post's structure and its one-line angle, the story title, the Metricool planner link, the number of open items in `REVIEW.md` (calling out the myth call for a Myth post), the raw GitHub URLs to `linkedin.pdf` and `linkedin.png`, the full text of `linkedin.txt` inline so it can be copied straight into a manual LinkedIn post, and a reminder to reply to comments in the first hour and to add the article link as a comment only after that hour. Also include the full text of `x.txt` and `x_extra.txt`, the raw GitHub URLs of the images listed under `IMAGES:` in `x.txt`, and the `QUOTE TARGET:` line, so the owner can post to X by hand. If push notifications aren't available, send an email to arxdsilva@gmail.com with the same content instead.
12. **Finish** with a short summary: which story and structure, why it was chosen over the others, what needs review, and the Metricool planner link.

## Publish to GitHub

1. Delete any `slide_NN.png` left over from an earlier render with more slides.
2. Stage only the post folder (`git add posts/<folder>/`), including `REVIEW.md`, `linkedin.png`, `linkedin.txt`, `linkedin.pdf`, `x.txt`, `x_extra.txt` and `x_sources.md`, which stay in the repo as a record. `metricool.json` is gitignored and stays local. Commit with the given message and run `git push origin main`. Never commit anything outside that folder, and never amend, force-push, or skip hooks. If the push fails, report the error and stop.
3. Take the commit SHA (`git rev-parse HEAD`) and build the slide URLs in order: `https://raw.githubusercontent.com/arxdsilva/hn-carousels/<sha>/posts/<folder>/slide_NN.png`, plus the LinkedIn file URLs the same way: `.../posts/<folder>/linkedin.png` and `.../posts/<folder>/linkedin.pdf`. Use the SHA, not `main`, so a rewrite never serves Metricool (or the owner) a cached older image. Also build the raw URLs for the slides listed under `IMAGES:` in `x.txt` the same way; they're already part of the slide list above, so there's nothing new to upload.
4. Check that each URL, including the LinkedIn files, returns HTTP 200 (`curl -sI`). A fresh push can take a minute to show up, so retry a few times before reporting a URL as unreachable and stopping.

## Send to Metricool

Post as an Instagram carousel: brand id `7070774`, timezone America/Edmonton, `media` set to the slide URLs in order, `text` set to the contents of `caption.txt`, and `instagramData.isAiGenerated` set to false.

1. Create it with `createScheduledPostForReview`, reviewer `arxdsilva@gmail.com`, approval system `all`. It publishes only after the owner approves it in the Metricool UI.
2. If that fails because the plan has no review flow, create it with `createScheduledPost` and `draft: true` instead, so it sits in the planner until the owner schedules it by hand. Never create a post that isn't a draft or in review.
3. Save the returned `id`, `uuid`, publish date and planner link to `posts/<folder>/metricool.json`.

## Rewrite a post

Run this only when the owner asks, for example "rewrite posts/<folder>: <what to change>" or "rewrite the latest post". "Latest" means the newest folder in `posts/` by date. The owner may also ask to change the structure ("make it a myth post"); then rebuild the slides with that structure's beats and hook formula and update the `structure` field and `sources.md`. A post from before the five structures (with a `type` field) gets a `structure` field on any rewrite.

1. **Edit.** Apply the owner's feedback to `spec.json` and `caption.txt`, following the same slide rules and the post's structure as in the scheduled run. Run the humanizer over any text you changed. Update `REVIEW.md` for any new claim, number or myth call.
2. **Re-render** with `carousel.py` and check the PNGs as in the scheduled run.
3. **Update the LinkedIn assets** if the rewrite changes the structure, topic, claim, or hook, or changes any slide (rebuild `linkedin.pdf` from the new slides): edit `linkedin.txt` and re-render `linkedin.png` with `linkedin_card.py`, following the same rules as step 8 of the scheduled run. If the rewrite only fixes a typo or small wording in the caption and the hook still holds, leave them as they are. If the rewrite changes the structure, topic, claim or hook, also rewrite `x.txt` following step 8b.
4. **Commit and push.** Follow "Publish to GitHub" with the commit message `post: <folder> (rewrite)`.
5. **Update Metricool.** Read `posts/<folder>/metricool.json` (or find the post with `getScheduledPosts` by date if the file is missing). Update the post with `updateScheduledPost` using the new slide URLs and caption, keeping every other field as it was. If it was in review, send it back with `sendScheduledPostForReview` using the same reviewer and approval system. Save the new `id` to `metricool.json`.
6. **Notify** the owner as in the scheduled run, saying the rewrite is waiting for approval. If the LinkedIn assets changed, include the refreshed `linkedin.pdf` / `linkedin.png` URLs and `linkedin.txt` text so the owner can re-post manually.

## Never
- Never open news.ycombinator.com pages directly. Use `hn_brief.py`.
- Never publish directly. Every Metricool post is either in review or a draft until the owner approves it in the Metricool UI.
- Never delete a Metricool post, and never change the publish date unless the owner asks.
- Never commit or push anything outside the post folder being published.
- Never delete or edit earlier folders in `posts/` unless the owner asks for a rewrite of that folder.
- Never commit or push a post folder without its `linkedin.png`, `linkedin.txt` and `linkedin.pdf`, unless the owner explicitly says to skip LinkedIn for that post.
- Never write a roundup ("5 things on HN this week") or a post whose hook is just the news headline. One story, one structure, one lesson or stance.
- Never put a link in `linkedin.txt`.
- Never put an emoji in `linkedin.txt`.
- Never commit or push a post folder without its `x.txt`, unless the owner explicitly says to skip X for that post.
- Never cross-post the Instagram/LinkedIn carousel to X as-is. X gets its own text written for the platform.
- Never add stories used in `x_extra.txt` to `sources.md`. They go in `x_sources.md` so they stay available as future main posts.
