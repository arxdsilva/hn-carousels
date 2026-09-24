#!/usr/bin/env python3
"""
Tweet-style Instagram carousel renderer.
Usage:  python3 carousel.py posts/<date-slug>/spec.json posts/<date-slug>/
Requires: pip install pillow
Spec format (JSON):
{
  "profile": {"name": "Your Name", "handle": "@yourhandle",
              "avatar": "assets/avatar.png", "verified": false},
  "slides": [
    {"text": "Paragraph one with **bold words**.\n\nParagraph two.",
     "panel": {"big": "Big serif line", "small": "optional caption"}}   # panel optional
  ]
}
Max 10 slides (Instagram carousel limit). Output: 1080x1350 PNGs (4:5).
"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
M = 84                      # side margin
HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")
F_REG = f"{FONT_DIR}/Poppins-Regular.ttf"
F_BOLD = f"{FONT_DIR}/Poppins-Bold.ttf"
F_SERIF = f"{FONT_DIR}/Lora-Variable.ttf"

INK = (20, 20, 22)
GREY = (96, 100, 108)
BLUE = (29, 155, 240)
RING = (72, 170, 140)
PANEL_TOP = (14, 30, 24)
PANEL_BOT = (8, 16, 13)
GOLD = (212, 184, 128)
CREAM = (238, 232, 218)


def font(path, size):
    return ImageFont.truetype(path, size)


def parse_runs(paragraph):
    """Split '**bold** text' into [(word, is_bold), ...]."""
    words = []
    for i, chunk in enumerate(re.split(r"\*\*", paragraph)):
        bold = i % 2 == 1
        for w in chunk.split():
            words.append((w, bold))
    return words


def layout_text(text, size, max_w):
    reg, bold = font(F_REG, size), font(F_BOLD, size)
    space = reg.getlength(" ")
    lines = []  # list of (list[(word,bold,x)], is_para_end)
    for para in text.split("\n\n"):
        for raw_line in para.split("\n"):
            cur, x = [], 0
            for w, b in parse_runs(raw_line):
                wl = (bold if b else reg).getlength(w)
                if cur and x + wl > max_w:
                    lines.append((cur, False))
                    cur, x = [], 0
                cur.append((w, b, x))
                x += wl + space
            lines.append((cur, False))
        lines[-1] = (lines[-1][0], True)
    return lines, reg, bold


def measure(lines, size):
    lh = int(size * 1.42)
    gap = int(size * 0.85)
    return sum(lh + (gap if end else 0) for _, end in lines) - gap


def draw_avatar(img, profile, x, y, d):
    ring = 6
    draw = ImageDraw.Draw(img)
    draw.ellipse([x, y, x + d, y + d], fill=RING)
    inner = d - 2 * ring - 6
    ix, iy = x + ring + 3, y + ring + 3
    draw.ellipse([x + ring, y + ring, x + d - ring, y + d - ring], fill=(255, 255, 255))
    mask = Image.new("L", (inner, inner), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, inner, inner], fill=255)
    path = profile.get("avatar")
    if path and not os.path.isabs(path):
        path = os.path.join(HERE, path)  # relative paths resolve from this folder
    if path and os.path.exists(path):
        ph = Image.open(path).convert("RGB")
        s = min(ph.size)
        ph = ph.crop(((ph.width - s) // 2, (ph.height - s) // 2, (ph.width + s) // 2, (ph.height + s) // 2))
        ph = ph.resize((inner, inner), Image.LANCZOS)
        img.paste(ph, (ix, iy), mask)
    else:
        tile = Image.new("RGB", (inner, inner), (32, 44, 40))
        td = ImageDraw.Draw(tile)
        initials = "".join(p[0] for p in profile.get("name", "?").split()[:2]).upper()
        f = font(F_BOLD, int(inner * 0.36))
        tw = f.getlength(initials)
        td.text(((inner - tw) / 2, inner * 0.28), initials, font=f, fill=CREAM)
        img.paste(tile, (ix, iy), mask)


def draw_badge(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE)
    draw.line([(cx - r * 0.45, cy + r * 0.02), (cx - r * 0.1, cy + r * 0.38), (cx + r * 0.5, cy - r * 0.35)],
              fill=(255, 255, 255), width=max(3, int(r * 0.24)), joint="curve")


def draw_header(img, profile):
    draw = ImageDraw.Draw(img)
    d = 150
    draw_avatar(img, profile, M, 78, d)
    nf, hf = font(F_BOLD, 44), font(F_REG, 38)
    tx = M + d + 34
    name = profile.get("name", "Your Name")
    draw.text((tx, 92), name, font=nf, fill=INK)
    if profile.get("verified"):
        draw_badge(draw, tx + nf.getlength(name) + 32, 92 + 30, 21)
    draw.text((tx, 152), profile.get("handle", "@yourhandle"), font=hf, fill=GREY)
    return 78 + d + 56  # y where body starts


def fit_serif(text, max_w, max_h, start):
    size = start
    while size > 30:
        f = font(F_SERIF, size)
        try:
            f.set_variation_by_axes([600])
        except Exception:
            pass
        words, lines, cur = text.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if f.getlength(t) <= max_w:
                cur = t
            else:
                lines.append(cur); cur = w
        lines.append(cur)
        lh = int(size * 1.08)
        if len(lines) * lh <= max_h and max(f.getlength(l) for l in lines) <= max_w:
            return f, lines, lh
        size -= 4
    return f, lines, int(size * 1.08)


def draw_panel(img, box, panel):
    x0, y0, x1, y1 = box
    pw, ph = x1 - x0, y1 - y0
    grad = Image.new("RGB", (pw, ph))
    gd = ImageDraw.Draw(grad)
    for i in range(ph):
        t = i / ph
        gd.line([(0, i), (pw, i)], fill=tuple(int(a + (b - a) * t) for a, b in zip(PANEL_TOP, PANEL_BOT)))
    # soft light arc in the corner, like a lit surface
    gd.arc([pw * 0.55, ph * 0.72, pw * 1.6, ph * 2.2], 180, 270, fill=(40, 58, 50), width=2)
    img.paste(grad, (x0, y0))
    draw = ImageDraw.Draw(img)
    pad = 56
    small = panel.get("small")
    small_h = 70 if small else 0
    f, lines, lh = fit_serif(panel["big"], pw - 2 * pad, ph - 2 * pad - small_h, 150)
    block = len(lines) * lh + small_h
    y = y0 + (ph - block) / 2 - lh * 0.08
    for l in lines:
        draw.text((x0 + (pw - f.getlength(l)) / 2, y), l, font=f, fill=GOLD)
        y += lh
    if small:
        sf = font(F_REG, 38)
        draw.text((x0 + (pw - sf.getlength(small)) / 2, y + 14), small, font=sf, fill=CREAM)


BODY_TOP = 78 + 150 + 56
PANEL_H = 390


def fitted_size(slide):
    panel = slide.get("panel")
    bottom = H - 70 - (PANEL_H + 44 if panel else 0)
    size = 54
    while size > 32:
        lines, _, _ = layout_text(slide["text"], size, W - 2 * M)
        if measure(lines, size) <= bottom - BODY_TOP:
            break
        size -= 2
    return size


def render_slide(profile, slide, size):
    img = Image.new("RGB", (W, H), (255, 255, 255))
    body_top = draw_header(img, profile)
    panel = slide.get("panel")
    panel_h = PANEL_H if panel else 0
    lines, reg, bold = layout_text(slide["text"], size, W - 2 * M)
    draw = ImageDraw.Draw(img)
    lh, gap = int(size * 1.42), int(size * 0.85)
    y = body_top
    for words, end in lines:
        for w, b, x in words:
            draw.text((M + x, y), w, font=bold if b else reg, fill=INK)
        y += lh + (gap if end else 0)
    if panel:
        draw_panel(img, (M, H - 70 - panel_h, W - M, H - 70), panel)
    return img


def main(spec_path, out_dir):
    spec = json.load(open(spec_path))
    slides = spec["slides"][:10]
    os.makedirs(out_dir, exist_ok=True)
    size = min(fitted_size(s) for s in slides)  # same type size on every slide
    for i, s in enumerate(slides, 1):
        p = os.path.join(out_dir, f"slide_{i:02d}.png")
        render_slide(spec["profile"], s, size).save(p, optimize=True)
        print(p)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
