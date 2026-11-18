# Sources

- **Structure:** elimination (Wednesday default: Proof or Elimination; the two previous posts were myth and ladder)
- **Angle:** a buffering proxy fails (Calif's Elasticsearch chain runs from one complete request, and WebSocket frames skip the buffer), -XX:UseAVX=2 fails across a mixed fleet (OpenJDK on ARM doesn't recognize it and won't start), patching plus -XX:-UseBASE64Intrinsics until the patch lands works.
- **HN thread:** https://news.ycombinator.com/item?id=50538240 (1012 points, 264 comments, #3 on the front page, 2026-11-18 07:02 America/Edmonton)
- **Article:** [Java4Shell: Write once, RCE everywhere](https://calif.io/java4shell/) by Quang Luong and Calif (calif.io), CVE-2026-114938
- **Image:** the article's own artwork ("All your Base64 are belong to us", pixel art by Michal Zalewski, credited in the write-up), cropped to the caption band for slide 1 (`assets/java4shell-wide.jpg`) and the LinkedIn card (`assets/java4shell-card.jpg`). Original: `assets/java4shell.jpg`.

## Facts used (Calif)
- Memory corruption in HotSpot's x86-64 AVX-512 VBMI Base64 intrinsic. 64 "A" + "=" (128 A's on older 17) gives a negative output length; the 65-char input allocates 50 bytes and a 64-byte write lands 62 bytes past it. CVSS 4.0 9.2.
- Pre-auth RCE in default configs: Keycloak, Jira, Confluence, Artifactory, Jenkins, PingFederate. Post-auth: Kafka, Solr, Elasticsearch, Gerrit, Spinnaker. Client-side exploit (samczsun): a Java program opening TLS to a malicious server.
- Limitations: a proxy that buffers bodies (nginx default) removes the release timing some grooming profiles need; "Request buffering is not a general mitigation": the Elasticsearch chain runs from one complete request; WebSocket frames pass through. No universal payload; each target needs a profile.
- Affected: OpenJDK 17.0.6+, all major distros; needs AVX-512 VBMI (Ice Lake+, Zen 4+). ARM64 not affected. CPU check: avx512f, avx512bw, avx512vbmi, bmi2 in /proc/cpuinfo.
- Recommendations: OpenJDK advisory and Oracle patch at 1:00pm PT Nov 17, 2026; update immediately. Mitigation flags: -XX:-UseBASE64Intrinsics, or -XX:UseAVX=2 on x86-64 only ("OpenJDK on ARM doesn't recognize it and will fail to start").

## Thread points used
- -XX:-UseBASE64Intrinsics recommended over UseAVX=2, which fails on systems without AVX2 (one developer).
- Temurin hadn't shipped a patch yet; Adoptium aims for 2 days after tags (two developers).
- Exploit is sensitive to RTT and jitter; reply: a semi-working Keycloak heap leak with live tokens is still dangerous (used as X counterpoint).
