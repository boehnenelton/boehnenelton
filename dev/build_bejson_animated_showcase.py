#!/usr/bin/env python3
"""
Script:        build_bejson_animated_showcase.py
Description:   Demonstrates how BEJSON 104a schema tables compile directly into
               deterministic vector graphics and renders animated SVG and GIF showcases.
Author:        Elton Boehnen · boehnenelton2024@gmail.com · boehnenelton2024.pages.dev · github.com/boehnenelton
Version:       1.0.0
"""

import json
import math
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

REPO_ROOT = Path("/storage/emulated/0/Admin/Dev/Repos/boehnenelton")
ASSETS_DIR = REPO_ROOT / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Authoritative BEJSON 104a Graphic Primitives Schema & Table
# ---------------------------------------------------------------------------

BEJSON_GRAPHIC_DATA = {
    "Format": "BEJSON",
    "Format_Version": "104a",
    "Format_Creator": "Elton Boehnen",
    "Schema_Name": "cubic_graphic_primitives",
    "Schema_Version": "1.0.0",
    "Description": "BEJSON 104a tabular vector graphic schema defining the canonical 3D isometric open branding cube and stage coordinates.",
    "Records_Type": [
        "CubicGraphicPrimitive"
    ],
    "Fields": [
        {"name": "element_id", "type": "string"},
        {"name": "primitive_type", "type": "string"},
        {"name": "points_or_coords", "type": "string"},
        {"name": "fill_color", "type": "string"},
        {"name": "stroke_color", "type": "string"},
        {"name": "stroke_width", "type": "number"},
        {"name": "animation_mode", "type": "string"},
        {"name": "semantic_label", "type": "string"}
    ],
    "Values": [
        ["elem_01_substrate", "rect", "0,0,1280,640", "#0A0A0C", "none", 0.0, "static", "Canvas Obsidian Substrate"],
        ["elem_02_frame", "rect", "48,48,1184,544", "none", "#1A1A22", 1.5, "static", "Structural Inset Boundary Frame"],
        ["elem_03_notch", "rect", "48,270,4,100", "#DE2626", "none", 0.0, "static", "Left Boundary Accent Notch"],
        ["elem_04_divider", "line", "364,256,364,404", "none", "#DE2626", 3.0, "pulse_alpha", "Primary Red Focal Divider"],
        ["elem_05_floating_cap", "polygon", "0,-48,56,-18,0,12,-56,-18", "#FFFFFF", "#FFFFFF", 1.5, "harmonic_float", "104a Hovering Diamond Cap"],
        ["elem_06_left_facet", "polygon", "-56,-18,0,12,0,72,-56,42", "#181820", "#FFFFFF", 1.5, "static", "Left Obsidian Shading Facet"],
        ["elem_07_right_facet", "polygon", "0,12,56,-18,56,42,0,72", "#DE2626", "#FFFFFF", 1.5, "static", "Right Signature Red Facet"]
    ]
}


def build_animated_svg() -> str:
    """Generates pure SVG with embedded CSS keyframe animations for GitHub inline display."""
    return """<svg width="1280" height="640" viewBox="0 0 1280 640" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes floatCap {
        0%, 100% {
          transform: translateY(0px);
        }
        50% {
          transform: translateY(-22px);
        }
      }
      @keyframes pulseBeam {
        0%, 100% {
          opacity: 0.75;
          stroke-width: 3px;
        }
        50% {
          opacity: 1.0;
          stroke-width: 3.5px;
        }
      }
      @keyframes scanTick {
        0%, 100% {
          stroke: #333340;
        }
        50% {
          stroke: #DE2626;
        }
      }
      .anim-cap {
        animation: floatCap 2.8s ease-in-out infinite;
      }
      .anim-divider {
        animation: pulseBeam 2.0s ease-in-out infinite;
      }
      .anim-tick {
        animation: scanTick 3.5s ease-in-out infinite;
      }
    </style>
  </defs>

  <!-- Pitch Black Substrate -->
  <rect width="1280" height="640" fill="#0A0A0C" />

  <!-- Outer Structural Boundary Inset -->
  <rect x="48" y="48" width="1184" height="544" rx="0" fill="none" stroke="#1A1A22" stroke-width="1.5" />

  <!-- Corner Precision Ticks (Zero Curvature) -->
  <path class="anim-tick" d="M 48 76 L 48 48 L 76 48" fill="none" stroke-width="2" />
  <path class="anim-tick" d="M 1204 48 L 1232 48 L 1232 76" fill="none" stroke-width="2" />
  <path class="anim-tick" d="M 48 564 L 48 592 L 76 592" fill="none" stroke-width="2" />
  <path class="anim-tick" d="M 1204 592 L 1232 592 L 1232 564" fill="none" stroke-width="2" />

  <!-- Vertical Red Accent Marker -->
  <rect x="48" y="270" width="4" height="100" rx="0" fill="#DE2626" />

  <!-- Center Brand Lockup with Animated Floating Top Diamond Cap -->
  <g transform="translate(260, 320)">
    <!-- Base Cube Geometry -->
    <g transform="translate(0, 0)">
      <!-- Left Face (Obsidian Dark) -->
      <polygon points="-56,-18 0,12 0,72 -56,42" fill="#181820" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <!-- Right Face (Elton Boehnen Signature Red #DE2626) -->
      <polygon points="0,12 56,-18 56,42 0,72" fill="#DE2626" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <!-- Inner Base Floor -->
      <polygon points="0,12 -40,-9 0,-30 40,-9" fill="#0F0F14" stroke="#22222E" stroke-width="1" />

      <!-- Floating Diamond Cap (Harmonic Oscillation) -->
      <g class="anim-cap">
        <polygon points="0,-48 56,-18 0,12 -56,-18" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
        <polygon points="0,-36 40,-15 0,6 -40,-15" fill="#0A0A0C" />
      </g>
    </g>

    <!-- Pulsing Vertical Divider Line -->
    <line class="anim-divider" x1="104" y1="-64" x2="104" y2="84" stroke="#DE2626" stroke-linecap="square" />

    <!-- Pure Purpose Typography -->
    <text x="144" y="16" fill="#FFFFFF" font-size="62" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" letter-spacing="1.5">boehnenelton</text>
    <text x="146" y="52" fill="#888896" font-size="14" font-family="monospace" font-weight="600" letter-spacing="3">SCHEMA-DRIVEN VECTOR ENGINE // BEJSON 104a</text>
  </g>
</svg>"""


def generate_frame_svg(frame_idx: int, total_frames: int) -> str:
    """Generates an explicit SVG frame at a given timeline interpolation step for GIF rendering."""
    progress = frame_idx / float(total_frames)
    # Sine wave harmonic oscillation for vertical float (-22px at peak)
    y_float = -22.0 * math.sin(progress * 2.0 * math.pi)
    # Divider pulse alpha between 0.75 and 1.0
    alpha = 0.85 + 0.15 * math.cos(progress * 2.0 * math.pi)
    # Stroke width between 3.0 and 3.5
    stroke_w = 3.0 + 0.5 * math.sin(progress * 2.0 * math.pi)

    return f"""<svg width="1280" height="640" viewBox="0 0 1280 640" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="640" fill="#0A0A0C" />
  <rect x="48" y="48" width="1184" height="544" rx="0" fill="none" stroke="#1A1A22" stroke-width="1.5" />

  <!-- Corner Ticks -->
  <path d="M 48 76 L 48 48 L 76 48" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 48 L 1232 48 L 1232 76" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 48 564 L 48 592 L 76 592" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 592 L 1232 592 L 1232 564" fill="none" stroke="#333340" stroke-width="2" />

  <rect x="48" y="270" width="4" height="100" rx="0" fill="#DE2626" />

  <g transform="translate(260, 320)">
    <!-- Base Cube Geometry -->
    <g transform="translate(0, 0)">
      <polygon points="-56,-18 0,12 0,72 -56,42" fill="#181820" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,12 56,-18 56,42 0,72" fill="#DE2626" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,12 -40,-9 0,-30 40,-9" fill="#0F0F14" stroke="#22222E" stroke-width="1" />

      <!-- Floating Top Diamond Cap -->
      <g transform="translate(0, {y_float:.2f})">
        <polygon points="0,-48 56,-18 0,12 -56,-18" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
        <polygon points="0,-36 40,-15 0,6 -40,-15" fill="#0A0A0C" />
      </g>
    </g>

    <!-- Pulsing Vertical Divider -->
    <line x1="104" y1="-64" x2="104" y2="84" stroke="#DE2626" stroke-width="{stroke_w:.2f}" opacity="{alpha:.2f}" />

    <!-- Typography -->
    <text x="144" y="16" fill="#FFFFFF" font-size="62" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" letter-spacing="1.5">boehnenelton</text>
    <text x="146" y="52" fill="#888896" font-size="14" font-family="monospace" font-weight="600" letter-spacing="3">SCHEMA-DRIVEN VECTOR ENGINE // BEJSON 104a</text>
  </g>
</svg>"""


def main():
    # 1. Write the BEJSON 104a schema table
    schema_path = ASSETS_DIR / "cubic_schema.104a.bejson"
    schema_path.write_text(json.dumps(BEJSON_GRAPHIC_DATA, indent=2), encoding="utf-8")
    print(f"[+] Wrote BEJSON schema table: {schema_path}")

    # 2. Write the animated SVG
    anim_svg_path = ASSETS_DIR / "boehnenelton_cubic_engine.svg"
    anim_svg_path.write_text(build_animated_svg(), encoding="utf-8")
    print(f"[+] Wrote animated vector SVG: {anim_svg_path}")

    # 3. Render 24 discrete frames for smooth looping GIF (1280x640 scaled to crisp 840x420 for optimal web gif performance)
    print("[+] Compiling animated GIF frames via native Chromium...")
    frames = []
    total_frames = 24
    temp_dir = REPO_ROOT / "dev" / "temp_frames"
    temp_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/data/data/com.termux/files/usr/bin/chromium",
            args=["--no-sandbox", "--disable-gpu"]
        )
        page = browser.new_page(viewport={"width": 1280, "height": 640})

        for i in range(total_frames):
            frame_svg = generate_frame_svg(i, total_frames)
            frame_svg_file = temp_dir / f"frame_{i:02d}.svg"
            frame_png_file = temp_dir / f"frame_{i:02d}.png"
            frame_svg_file.write_text(frame_svg, encoding="utf-8")

            page.goto(f"file://{frame_svg_file.resolve()}")
            page.screenshot(path=str(frame_png_file))

            # Open with Pillow and resize to crisp 840x420 for fast loading
            img = Image.open(frame_png_file).resize((840, 420), Image.Resampling.LANCZOS)
            frames.append(img.convert("P", palette=Image.Palette.ADAPTIVE))

        browser.close()

    # 4. Save animated GIF
    gif_path = ASSETS_DIR / "boehnenelton_cubic_engine.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=70,  # ~14 fps, 1.68s loop
        loop=0,
        optimize=True
    )
    print(f"[+] Rendered animated GIF: {gif_path} ({gif_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
