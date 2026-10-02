#!/usr/bin/env python3
"""
Fetch an article's og:image (or twitter:image) and save it locally, for the
"image" slide option in carousel.py.

Usage: python3 fetch_image.py <article_url> <out_path.jpg>

Prints the saved path on success, or NO_IMAGE_FOUND / FETCH_FAILED on failure
(the carousel workflow should fall back to bullets on that slide instead).
"""
import re
import sys
import urllib.request

META_RE = re.compile(
    r'<meta[^>]+(?:property|name)=["\'](?:og:image|twitter:image)["\'][^>]+content=["\']([^"\']+)["\']',
    re.IGNORECASE,
)


def main(url, out_path):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (hn-carousels)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", "replace")
    except Exception as e:
        print(f"FETCH_FAILED: {e}")
        return 1

    match = META_RE.search(html)
    if not match:
        print("NO_IMAGE_FOUND")
        return 1
    image_url = match.group(1)

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
