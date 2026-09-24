# HN carousels: setup

## One-time setup
1. Put this folder somewhere permanent on your computer.
2. Install Pillow: `pip3 install pillow`. Optionally, `pip3 install trafilatura` for cleaner article text in `hn_brief.py`.
3. Open Claude Desktop, go to the Code tab, and choose this folder as the project.
4. Create a local scheduled task (Routines page) for this folder, with this prompt:

   Run the HN carousel workflow described in CLAUDE.md.

   Schedule it for Monday, Wednesday and Friday at 7:00 AM (America/Edmonton).

Local tasks run only while Claude Desktop is open and your computer is awake. If a run is missed, it catches up the next time the app opens.

## Research

The routine researches through `hn_brief.py`, which uses the official HN API instead of the web pages:

- `python3 hn_brief.py top` lists the top 10 stories and skips any already linked in `posts/*/sources.md`.
- `python3 hn_brief.py story <id>` prints the article text (up to 1,800 words) and the top 12 comments, each with its first reply.

## Publishing

1. **Routine drafts and pushes.** The routine writes a new folder in `posts/`, commits it (`post: <folder>`) and pushes to `main`. Metricool can't read local files or Google Drive, so it pulls the slides from raw GitHub URLs pinned to that commit, such as `https://raw.githubusercontent.com/arxdsilva/hn-carousels/<sha>/posts/<folder>/slide_01.png`. Drafts are public on GitHub from this point, before you've reviewed them.
2. **Sent to Metricool for review.** The routine creates the Instagram carousel for 11:00 AM on the posting date and sends it to review, with you as the reviewer. If your plan doesn't have the review flow, it saves the post as a draft instead. You get a notification with the planner link.
3. **You approve in Metricool.** Check the post against `REVIEW.md`, then approve it (or schedule the draft) in the Metricool UI. Nothing publishes until you do.
4. **Rewrite if needed.** In Claude Code, say "rewrite posts/<folder>: <what to change>". Claude edits and re-renders the post, pushes a new commit, updates the Metricool post and sends it back to review.

The Metricool post ids are saved in `posts/<folder>/metricool.json`, which is gitignored.

The Metricool free plan allows 20 posts a month. Three posts a week comes to about 13, which leaves some room for extra posts.
