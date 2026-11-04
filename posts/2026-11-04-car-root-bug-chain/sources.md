Structure: elimination
Angle: Flashing a modified update fails (signature check), the script engine's shell command fails (one token, no arguments, noexec mounts), chaining a log-command path traversal into core_pattern with a binary that crashes on start works.

- HN thread: https://news.ycombinator.com/item?id=50339288 (870 points, 329 comments, rank #10 on the 2026-11-04 front page).
- Article: [Jailbreaking my car's navigation system just so I can change the time](https://blog.nns.ee/2026/11/02/renault-hack/) by Rasmus Moorats (nns.ee), 2026-11-02.
- Facts used: 2014 Renault Latitude, TomTom Carminat LIVE unit on Linux 2.6.28.10; settings menu definition is read from a DRM-checked map SD card (CID-bound signatures); replacement card about 60 EUR shipped to Estonia; modified ttsystem image rejected (appended signature, likely 40 bytes); SHEX launches one whitespace-delimited token; mounts read-only or noexec; LOG command has a ../ path traversal writing printable ASCII as root; final chain writes `|/bin/sh /media/sdcard/payload.sh` to /proc/sys/kernel/core_pattern, then SHEX /bin/dbus-monitor, which SIGABRTs without a system bus; fix was the UTC offset in /mnt/flash/settings.dat, 180 to 120 minutes.
- Counterpoint (thread): one developer said he should have just bought the SD card and trusted the previous owner; the author replied the card had already gone in the trash.
- Image: the article's own photo of the head unit's "Execute master.script?" prompt (blog.nns.ee/img/2026-11-02-renault-hack/execute-script.jpg), cropped to 1279x544. The author's own work.
