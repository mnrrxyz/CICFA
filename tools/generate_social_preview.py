#!/usr/bin/env python3
"""
generate_social_preview.py
CICFA — Generates a 1280x640 social preview image for GitHub / social sharing.
Output: social_preview.png
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# ── Canvas ────────────────────────────────────────────────────
W, H = 1280, 640
BG        = (5, 5, 5)
GREEN     = (0, 255, 65)
GREEN_DIM = (0, 140, 35)
GREEN_DK  = (0, 40, 10)
RED       = (255, 45, 45)
RED_DK    = (80, 0, 0)
WHITE     = (210, 210, 210)

img  = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

# ── Fonts ─────────────────────────────────────────────────────
MONACO = '/System/Library/Fonts/Monaco.ttf'
MENLO  = '/System/Library/Fonts/Menlo.ttc'

f_giant  = ImageFont.truetype(MONACO, 148)   # CICFA letters
f_large  = ImageFont.truetype(MENLO,  22)
f_med    = ImageFont.truetype(MENLO,  16)
f_small  = ImageFont.truetype(MENLO,  13)
f_tiny   = ImageFont.truetype(MENLO,  11)

# ── CRT scanlines ─────────────────────────────────────────────
for y in range(0, H, 3):
    draw.line([(0, y), (W, y)], fill=(0, 0, 0), width=1)

# ── Vignette ─────────────────────────────────────────────────
for i in range(80):
    darkness = max(0, 80 - i) * 2
    c = (darkness // 6, 0, 0)
    draw.rectangle([i, i, W - i, H - i], outline=c)

# ── Giant CICFA text (left) ───────────────────────────────────
# Ghost / shadow layer
draw.text((46, 62), "CICFA", font=f_giant, fill=(0, 60, 15))
draw.text((44, 60), "CICFA", font=f_giant, fill=(0, 110, 28))
# Main
draw.text((42, 58), "CICFA", font=f_giant, fill=GREEN)

# ── Grid overlay on text area ─────────────────────────────────
for x in range(0, 680, 40):
    draw.line([(x, 58), (x, 220)], fill=(0, 30, 8), width=1)
for y in range(58, 222, 20):
    draw.line([(0, y), (680, y)], fill=(0, 30, 8), width=1)

# Redraw text on top of grid
draw.text((42, 58), "CICFA", font=f_giant, fill=GREEN)

# ── Left: subtitle block ──────────────────────────────────────
y_sub = 240
draw.text((48, y_sub),
    "Cultural Infrastructure Critical Failure Attack",
    font=f_med, fill=GREEN_DIM)
y_sub += 26
draw.text((48, y_sub),
    "DWG-CICFA-01   vB.01   STATUS: ACTIVE",
    font=f_small, fill=(0, 90, 22))
y_sub += 30

draw.line([(48, y_sub), (620, y_sub)], fill=(0, 60, 15), width=1)
y_sub += 20

left_lines = [
    (GREEN_DIM, "> Making institutions experience the aesthetic,"),
    (GREEN_DIM, "  symbolic, and procedural logic of cyber-attacks."),
    ((0, 70, 18), ""),
    ((0, 70, 18), "> This is not an attack."),
    (GREEN,      "  This is an attack."),
]
for color, text in left_lines:
    draw.text((48, y_sub), text, font=f_small, fill=color)
    y_sub += 22

# ── Vertical divider ──────────────────────────────────────────
div_x = 700
draw.line([(div_x, 30), (div_x, H - 60)], fill=(30, 0, 0), width=1)
for y in range(36, H - 60, 8):
    draw.point((div_x, y), fill=(60, 0, 0))

# ── Right: operation block ────────────────────────────────────
x_r = div_x + 40
y_r = 42

draw.text((x_r, y_r), "> OPERATION 001", font=f_large, fill=RED)
y_r += 32
draw.line([(x_r, y_r), (W - 40, y_r)], fill=RED_DK, width=1)
y_r += 18

fields = [
    ("CODENAME", "MOMA.SYM",                 WHITE),
    ("TARGET  ", "MoMA, New York City",       WHITE),
    ("VECTOR  ", "Symbolic [A] + White Hat [B]", WHITE),
    ("STATUS  ", ">>>>>>>>>>>>>>  OPEN",      GREEN),
    ("DEADLINE", "TBD",                       (0, 90, 22)),
    ("REWARD  ", "Attribution + Exhibition",  WHITE),
]
for label, value, col in fields:
    draw.text((x_r,       y_r), label, font=f_small, fill=(0, 100, 25))
    draw.text((x_r + 120, y_r), value, font=f_small, fill=col)
    y_r += 26

y_r += 10
draw.line([(x_r, y_r), (W - 40, y_r)], fill=RED_DK, width=1)
y_r += 18

regs = [
    ("[A]", "Symbolic / Conceptual"),
    ("[B]", "Technical / White Hat (responsible disclosure)"),
]
for tag, desc in regs:
    draw.text((x_r,      y_r), tag,  font=f_small, fill=RED)
    draw.text((x_r + 46, y_r), desc, font=f_small, fill=GREEN_DIM)
    y_r += 24

y_r += 10
draw.text((x_r, y_r),
    "A real CVE filed as a ransom note is both.",
    font=f_tiny, fill=(0, 70, 18))

y_r += 30
draw.line([(x_r, y_r), (W - 40, y_r)], fill=RED_DK, width=1)
y_r += 18

ethical = [
    "The work is about violence, not violent.",
    "It stages symbolic systems, not real-world harm.",
    "It exposes fragility as aesthetic condition.",
]
for line in ethical:
    draw.text((x_r, y_r), line, font=f_tiny, fill=(80, 0, 0))
    y_r += 18

# ── Bottom bar ────────────────────────────────────────────────
bar_y = H - 50
draw.rectangle([(0, bar_y), (W, H)], fill=(8, 0, 0))
draw.line([(0, bar_y), (W, bar_y)], fill=RED_DK, width=1)

draw.text((48, bar_y + 14),
    "github.com/DEEP-WEB-GALLERY/CICFA",
    font=f_small, fill=(120, 0, 0))

draw.text((W - 300, bar_y + 14),
    "deep-web-gallery.github.io/CICFA",
    font=f_small, fill=(80, 0, 0))

# ── Border ────────────────────────────────────────────────────
draw.rectangle([(1, 1), (W - 2, H - 2)], outline=RED_DK, width=1)

# ── Save ──────────────────────────────────────────────────────
out = Path(__file__).parent.parent / "social_preview.png"
img.save(out, "PNG", optimize=True)
print(f"[OK] Social preview saved: {out}")
