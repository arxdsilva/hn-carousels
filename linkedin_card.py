#!/usr/bin/env python3
"""
Single-image LinkedIn quote card. Reuses carousel.py's panel renderer
(same dark gradient, gold serif big line, optional small caption) at
1080x1080 instead of a full carousel slide, since a LinkedIn post
needs one image with very little text on it.

Usage: python3 linkedin_card.py "Big line" "optional small caption" out.png
Pass "" for the second argument to omit the small caption.
"""
import sys
from PIL import Image
from carousel import draw_panel, M

W = H = 1080


def main(big, small, out_path):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw_panel(img, (M, M, W - M, H - M), {"big": big, "small": small or None})
    img.save(out_path, optimize=True)
    print(out_path)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
