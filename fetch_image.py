#!/usr/bin/env python3
"""
Fetch an image to reuse from an article and save it locally, for the
"image" slide option in carousel.py.

Tries, in priority order:
1. og:image / twitter:image meta tags.
2. The first substantial <img> in the page body (skips tiny icons, logos,
   avatars, and data: URIs) — this is what to reach for when the article
   itself embeds a diagram, screenshot or illustration but has no social
   preview image set.

Usage: python3 fetch_image.py <article_url> <out_path.jpg>

Prints the saved path on success, or NO_IMAGE_FOUND / FETCH_FAILED on failure
(the carousel workflow should fall back to bullets on that slide instead).
"""
import re
import sys
import urllib.parse
import urllib.request

META_RE = re.compile(
    r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]+content=["\']([^"\']+)["\']',
    re.IGNORECASE,
)
IMG_RE = re.compile(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
SKIP_HINTS = ("icon", "logo", "avatar", "favicon", "sprite", "badge", "button")


def find_body_image(html, base_url):
    for match in IMG_RE.finditer(html):
        src = match.group(1)
        if src.startswith("data:"):
            continue
        low = src.lower()
        if any(hint in low for hint in SKIP_HINTS):
            continue
        return urllib.parse.urljoin(base_url, src)
    return None


def main(url, out_path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (hn-carousels)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"FETCH_FAILED: {e}")
        return 1

    match = META_RE.search(html)
    if match:
        image_url = match.group(1)
    else:
        image_url = find_body_image(html, url)
        if not image_url:
            print("NO_IMAGE_FOUND")
            return 1

    img_req = urllib.request.Request(image_url, headers={"User-Agent": "Mozilla/5.0 (hn-carousels)"})
    try:
        with urllib.request.urlopen(img_req, timeout=20) as r:
            data = r.read()
    except Exception as e:
        print(f"FETCH_FAILED: {e}")
        return 1

    with open(out_path, "wb") as f:
        f.write(data)
    print(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
