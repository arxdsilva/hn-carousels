#!/usr/bin/env python3
"""
Single-image LinkedIn quote card, 1080x1080.

Two styles:
- No image path given: the original dark gradient panel with a big
  gold serif line and optional small caption (carousel.py's draw_panel).
- Image path given: matches the new Instagram slide-1 look instead -
  a bold hook line (supports **bold** runs) and optional grey caption
  on white at the top, with the image full-bleed beneath it.

Usage: python3 linkedin_card.py "Big line" "optional small caption" out.png [image_path]
Pass "" for the second argument to omit the small caption.
"""
import sys
from PIL import Image, ImageDraw
from carousel import (
    M, font, F_REG, F_BOLD, INK, GREY,
    layout_text, measure, draw_image, draw_panel,
)

W = H = 1080


def render_panel(big, small, out_path):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw_panel(img, (M, M, W - M, H - M), {"big": big, "small": small or None})
    img.save(out_path, optimize=True)


def render_with_image(hook, caption, image_path, out_path):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    size = 64
    while size > 36:
        lines, _, _ = layout_text(hook, size, W - 2 * M)
        if measure(lines, size) <= 420:
            break
        size -= 2
    lines, reg, bold = layout_text(hook, size, W - 2 * M)
    lh, gap = int(size * 1.32), int(size * 0.8)
    y = 84
    for words, end in lines:
        for w, b, x in words:
            draw.text((M + x, y), w, font=bold if b else reg, fill=INK)
        y += lh + (gap if end else 0)

    if caption:
        cf = font(F_REG, 34)
        draw.text((M, y + 8), caption, font=cf, fill=GREY)
        y += 8 + int(34 * 1.3)

    image_top = max(y + 40, H - 620)  # image takes at least the bottom ~620px
    draw_image(img, (0, image_top, W, H), image_path)
    img.save(out_path, optimize=True)


def main(big, small, out_path, image_path=None):
    if image_path:
        render_with_image(big, small, image_path, out_path)
    else:
        render_panel(big, small, out_path)
    print(out_path)


if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0], args[1], args[2], args[3] if len(args) > 3 else None)
