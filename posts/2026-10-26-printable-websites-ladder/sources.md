Structure: ladder
Angle: How to make a web page print well: good: do nothing and let Ctrl-P print the screen layout, better: a short @media print block (hide nav, 12pt text, black links), best: add page-break rules and render PDFs from the same page in a headless browser.

- HN thread: https://news.ycombinator.com/item?id=50241664 (81 points, 71 comments, rank #8 on the 2026-10-26 front page).
- Article: [Websites Should Be Printable](https://brennenputh.me/blog/printable-websites/) by Brennen Puth (brennenputh.me), 2026-10-24.
- Levels 1 and 2 come from the article (Puth's Ctrl-P test and his print CSS snippet: noPrint/onlyPrint classes, 12pt body text, black links; code blocks still breaking across pages).
- Level 3 combines thread points (one developer: printable pages head off "download a PDF" requests and let you print any page in a headless browser; another: printing drops background colors and images by default; another listed missing pieces like keeping elements from breaking up) with general CSS knowledge (break-inside: avoid, print-color-adjust).
- Counterpoints (thread): print support ranks below on-screen UX and accessibility for one developer; others called printing a waste of paper; one argued the web was meant for navigable documents, not print.
- Slide 1: no usable image. fetch_image.py returned a page screenshot of a different post by the author, so slide 1 uses a panel.
