# HN carousels: setup

## One-time setup
1. Put this folder somewhere permanent on your computer.
2. Install Pillow: `pip3 install pillow`
3. Open Claude Desktop, go to the Code tab, and choose this folder as the project.
4. Create a local scheduled task (Routines page) for this folder, with this prompt:

   Run the HN carousel workflow described in CLAUDE.md.

   Schedule it for Monday, Wednesday and Friday at 7:00 AM. If the scheduler only offers daily, pick daily: the workflow skips other days by itself.

Local tasks run only while Claude Desktop is open and your computer is awake. If a run is missed, it catches up the next time the app opens.

## After each run
1. Open the newest folder in `posts/`.
2. Go through `REVIEW.md` and edit `spec.json` or `caption.txt` so the take is really yours.
3. If you changed `spec.json`, re-render: `python3 carousel.py posts/<folder>/spec.json posts/<folder>/`
4. Upload the slide PNGs in order and paste `caption.txt` in Metricool (Create post) or the Instagram app.
