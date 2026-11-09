#!/usr/bin/env python3
"""
Generate cool cubic banner variants for Elton Boehnen's GitHub profile hub repository.
Produces SVG, PNG (1280x640), and WebP formats across 4 distinct cubic architectural variants.
"""

from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

REPO_ROOT = Path("/storage/emulated/0/Admin/Dev/Repos/boehnenelton")
ASSETS_DIR = REPO_ROOT / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# 1. Variant 1: Canonical 104 Open Cube (Dark)
VARIANT_1_CANONICAL = """<svg width="1280" height="640" viewBox="0 0 1280 640" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="640" fill="#0A0A0C" />
  <rect x="48" y="48" width="1184" height="544" rx="0" fill="none" stroke="#1A1A22" stroke-width="1.5" />
  <path d="M 48 76 L 48 48 L 76 48" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 48 L 1232 48 L 1232 76" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 48 564 L 48 592 L 76 592" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 592 L 1232 592 L 1232 564" fill="none" stroke="#333340" stroke-width="2" />
  <rect x="48" y="270" width="4" height="100" rx="0" fill="#DE2626" />

  <g transform="translate(260, 320)">
    <!-- 3D Open Isometric Cube (Format 104) -->
    <g transform="translate(0, 0)">
      <polygon points="0,-48 56,-18 0,12 -56,-18" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,-36 40,-15 0,6 -40,-15" fill="#0A0A0C" />
      <polygon points="-56,-18 0,12 0,72 -56,42" fill="#181820" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,12 56,-18 56,42 0,72" fill="#DE2626" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
    </g>
    <line x1="104" y1="-64" x2="104" y2="84" stroke="#DE2626" stroke-width="3" />
    <text x="144" y="16" fill="#FFFFFF" font-size="62" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" letter-spacing="1.5">boehnenelton</text>
    <text x="146" y="52" fill="#888896" font-size="14" font-family="monospace" font-weight="600" letter-spacing="3">SYSTEMS ARCHITECT // BEJSON &amp; AUTONOMOUS ENGINES</text>
  </g>
</svg>"""

# 2. Variant 2: Floating Top Dynamic Cube (Format 104a)
VARIANT_2_FLOATING = """<svg width="1280" height="640" viewBox="0 0 1280 640" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="640" fill="#0A0A0C" />
  <rect x="48" y="48" width="1184" height="544" rx="0" fill="none" stroke="#1A1A22" stroke-width="1.5" />
  <path d="M 48 76 L 48 48 L 76 48" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 48 L 1232 48 L 1232 76" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 48 564 L 48 592 L 76 592" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 592 L 1232 592 L 1232 564" fill="none" stroke="#333340" stroke-width="2" />
  <rect x="48" y="270" width="4" height="100" rx="0" fill="#DE2626" />

  <g transform="translate(260, 320)">
    <!-- Floating Top 3D Cube (Format 104a) -->
    <g transform="translate(0, 0)">
      <!-- Hovering Diamond Cap -->
      <polygon points="0,-72 56,-42 0,-12 -56,-42" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,-60 40,-39 0,-18 -40,-39" fill="#0A0A0C" />
      <!-- Lower Body Base -->
      <polygon points="-56,-24 0,6 0,66 -56,36" fill="#181820" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,6 56,-24 56,36 0,66" fill="#DE2626" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,6 -42,-16 0,-38 42,-16" fill="#101016" stroke="#333344" stroke-width="1" />
    </g>
    <line x1="104" y1="-64" x2="104" y2="84" stroke="#DE2626" stroke-width="3" />
    <text x="144" y="16" fill="#FFFFFF" font-size="62" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" letter-spacing="1.5">boehnenelton</text>
    <text x="146" y="52" fill="#888896" font-size="14" font-family="monospace" font-weight="600" letter-spacing="3">FORMAT 104a // HIGH-PERFORMANCE DATA MATRIX</text>
  </g>
</svg>"""

# 3. Variant 3: Stacked Pillar Dual Cube (Format 104db / MFDB)
VARIANT_3_STACKED = """<svg width="1280" height="640" viewBox="0 0 1280 640" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="640" fill="#0A0A0C" />
  <rect x="48" y="48" width="1184" height="544" rx="0" fill="none" stroke="#1A1A22" stroke-width="1.5" />
  <path d="M 48 76 L 48 48 L 76 48" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 48 L 1232 48 L 1232 76" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 48 564 L 48 592 L 76 592" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 1204 592 L 1232 592 L 1232 564" fill="none" stroke="#333340" stroke-width="2" />
  <rect x="48" y="270" width="4" height="100" rx="0" fill="#DE2626" />

  <g transform="translate(260, 320)">
    <!-- Stacked Pillar Dual Cubes (Format 104db / MFDB) -->
    <g transform="translate(0, 0)">
      <!-- Top Cube -->
      <polygon points="0,-72 48,-46 0,-20 -48,-46" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="-48,-46 0,-20 0,22 -48,-4" fill="#20202A" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,-20 48,-46 48,-4 0,22" fill="#DE2626" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <!-- Bottom Cube -->
      <polygon points="-48,2 0,28 0,70 -48,44" fill="#14141C" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,28 48,2 48,44 0,70" fill="#991B1B" stroke="#FFFFFF" stroke-width="1.5" stroke-linejoin="round" />
    </g>
    <line x1="104" y1="-64" x2="104" y2="84" stroke="#DE2626" stroke-width="3" />
    <text x="144" y="16" fill="#FFFFFF" font-size="62" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" letter-spacing="1.5">boehnenelton</text>
    <text x="146" y="52" fill="#888896" font-size="14" font-family="monospace" font-weight="600" letter-spacing="3">MFDB ARCHITECTURE // RELATIONAL PERSISTENCE</text>
  </g>
</svg>"""

# 4. Variant 4: Architectural Minimal Light
VARIANT_4_LIGHT = """<svg width="1280" height="640" viewBox="0 0 1280 640" xmlns="http://www.w3.org/2000/svg">
  <rect width="1280" height="640" fill="#FFFFFF" />
  <rect x="48" y="48" width="1184" height="544" rx="0" fill="none" stroke="#E5E7EB" stroke-width="1.5" />
  <path d="M 48 76 L 48 48 L 76 48" fill="none" stroke="#9CA3AF" stroke-width="2" />
  <path d="M 1204 48 L 1232 48 L 1232 76" fill="none" stroke="#9CA3AF" stroke-width="2" />
  <path d="M 48 564 L 48 592 L 76 592" fill="none" stroke="#9CA3AF" stroke-width="2" />
  <path d="M 1204 592 L 1232 592 L 1232 564" fill="none" stroke="#9CA3AF" stroke-width="2" />
  <rect x="48" y="270" width="4" height="100" rx="0" fill="#DE2626" />

  <g transform="translate(260, 320)">
    <!-- 3D Open Isometric Cube (Light Palette) -->
    <g transform="translate(0, 0)">
      <polygon points="0,-48 56,-18 0,12 -56,-18" fill="#000000" stroke="#000000" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,-36 40,-15 0,6 -40,-15" fill="#FFFFFF" />
      <polygon points="-56,-18 0,12 0,72 -56,42" fill="#E5E7EB" stroke="#000000" stroke-width="1.5" stroke-linejoin="round" />
      <polygon points="0,12 56,-18 56,42 0,72" fill="#DE2626" stroke="#000000" stroke-width="1.5" stroke-linejoin="round" />
    </g>
    <line x1="104" y1="-64" x2="104" y2="84" stroke="#DE2626" stroke-width="3" />
    <text x="144" y="16" fill="#000000" font-size="62" font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" letter-spacing="1.5">boehnenelton</text>
    <text x="146" y="52" fill="#666677" font-size="14" font-family="monospace" font-weight="600" letter-spacing="3">SYSTEMS ARCHITECT // BEJSON &amp; AUTONOMOUS ENGINES</text>
  </g>
</svg>"""

VARIANTS = {
    "boehnenelton_banner_canonical": VARIANT_1_CANONICAL,
    "boehnenelton_banner_floating_cube": VARIANT_2_FLOATING,
    "boehnenelton_banner_stacked_pillar": VARIANT_3_STACKED,
    "boehnenelton_banner_light_minimal": VARIANT_4_LIGHT
}

def main():
    print("Authoring SVG banner files...")
    for name, svg_content in VARIANTS.items():
        svg_file = ASSETS_DIR / f"{name}.svg"
        svg_file.write_text(svg_content, encoding="utf-8")
        print(f"  [+] Wrote {svg_file.name}")

    print("Launching Chromium to render 1280x640 PNGs...")
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/data/data/com.termux/files/usr/bin/chromium",
            args=["--no-sandbox", "--disable-gpu"]
        )
        page = browser.new_page(viewport={"width": 1280, "height": 640})
        for name in VARIANTS.keys():
            svg_file = ASSETS_DIR / f"{name}.svg"
            png_file = ASSETS_DIR / f"{name}.png"
            webp_file = ASSETS_DIR / f"{name}.webp"

            page.goto(f"file://{svg_file.resolve()}")
            page.screenshot(path=str(png_file))
            print(f"  [+] Rendered {png_file.name}")

            # WebP conversion
            img = Image.open(png_file)
            img.save(webp_file, format="WEBP", quality=95)
            print(f"  [+] Converted {webp_file.name}")

        browser.close()

    print("All banner variants generated successfully.")

if __name__ == "__main__":
    main()
