#!/usr/bin/env python3
"""
Script:        generate_animated_diagram.py
Description:   Synthesizes an animated architectural diagram of the BEJSON & Autonomous
               Ecosystem pipeline adhering to canvas-animation-studio and bejson-diagram-component.
               Produces both an animated vector SVG and an optimized animated GIF.
Author:        Elton Boehnen · boehnenelton2024@gmail.com · boehnenelton2024.pages.dev · github.com/boehnenelton
Version:       1.0.0
"""

import math
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image

REPO_ROOT = Path("/storage/emulated/0/Admin/Dev/Repos/boehnenelton")
ASSETS_DIR = REPO_ROOT / "assets"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)


def build_animated_diagram_svg() -> str:
    """Generates pure SVG with CSS keyframe animations for the architecture pipeline diagram."""
    return """<svg width="960" height="540" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @keyframes pulseFlow {
        0% { stroke-dashoffset: 40; }
        100% { stroke-dashoffset: 0; }
      }
      @keyframes nodeGlow1 {
        0%, 100% { stroke: #DE2626; fill: #14141C; }
        25%, 75% { stroke: #2A2A38; fill: #0E0E14; }
      }
      @keyframes nodeGlow2 {
        0%, 50%, 100% { stroke: #2A2A38; fill: #0E0E14; }
        25% { stroke: #DE2626; fill: #14141C; }
      }
      @keyframes nodeGlow3 {
        0%, 25%, 100% { stroke: #2A2A38; fill: #0E0E14; }
        50% { stroke: #DE2626; fill: #14141C; }
      }
      @keyframes nodeGlow4 {
        0%, 50%, 100% { stroke: #2A2A38; fill: #0E0E14; }
        75% { stroke: #DE2626; fill: #14141C; }
      }
      @keyframes floatCube {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-8px); }
      }
      .flow-connector {
        stroke-dasharray: 8 6;
        animation: pulseFlow 1.4s linear infinite;
      }
      .node-card-1 { animation: nodeGlow1 4.0s ease-in-out infinite; }
      .node-card-2 { animation: nodeGlow2 4.0s ease-in-out infinite; }
      .node-card-3 { animation: nodeGlow3 4.0s ease-in-out infinite; }
      .node-card-4 { animation: nodeGlow4 4.0s ease-in-out infinite; }
      .cube-float { animation: floatCube 2.8s ease-in-out infinite; }
    </style>
  </defs>

  <!-- Obsidian Canvas Substrate -->
  <rect width="960" height="540" fill="#0A0A0C" />

  <!-- Outer Architectural Boundary (Zero Curvature) -->
  <rect x="30" y="30" width="900" height="480" rx="0" fill="none" stroke="#1A1A22" stroke-width="1.5" />

  <!-- Corner Precision Ticks -->
  <path d="M 30 54 L 30 30 L 54 30" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 906 30 L 930 30 L 930 54" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 30 486 L 30 510 L 54 510" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 906 510 L 930 510 L 930 486" fill="none" stroke="#333340" stroke-width="2" />

  <!-- Header Section -->
  <rect x="30" y="30" width="900" height="64" fill="#0E0E14" stroke="#1A1A22" stroke-width="1" />
  <rect x="30" y="30" width="6" height="64" fill="#DE2626" />
  <text x="54" y="60" fill="#FFFFFF" font-size="18" font-family="system-ui, -apple-system, sans-serif" font-weight="800" letter-spacing="1">BEJSON AUTONOMOUS ECOSYSTEM // PIPELINE ARCHITECTURE</text>
  <text x="54" y="80" fill="#888896" font-size="11" font-family="monospace" letter-spacing="2">DETERMINISTIC COMPILATION · RELATIONAL PERSISTENCE · ZERO-SQL</text>

  <!-- Small Subtle Top-Right 3D Isometric Cube -->
  <g class="cube-float" transform="translate(884, 62)">
    <polygon points="0,-18 20,-7 0,4 -20,-7" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="-20,-7 0,4 0,26 -20,15" fill="#181820" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="0,4 20,-7 20,15 0,26" fill="#DE2626" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
  </g>

  <!-- Stage Connectors (Pulsing Directional Flow) -->
  <g stroke="#DE2626" stroke-width="2.5" fill="none">
    <line class="flow-connector" x1="240" y1="270" x2="280" y2="270" />
    <line class="flow-connector" x1="460" y1="270" x2="500" y2="270" />
    <line class="flow-connector" x1="680" y1="270" x2="720" y2="270" />
  </g>
  <!-- Connector Arrowheads -->
  <polygon points="278,266 284,270 278,274" fill="#DE2626" />
  <polygon points="498,266 504,270 498,274" fill="#DE2626" />
  <polygon points="718,266 724,270 718,274" fill="#DE2626" />

  <!-- Node 01: Declarative Schemas -->
  <g transform="translate(60, 130)">
    <rect class="node-card-1" x="0" y="0" width="180" height="280" rx="0" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">01 · SCHEMAS</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">BEJSON 104a / 105</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Fields Ledger</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• UUIDv4 Identity</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• Strict Typing</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• SHA-256 Hashes</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• Schema Guards</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">IMMUTABLE CONTRACT</text>
  </g>

  <!-- Node 02: O(1) Cache Engine -->
  <g transform="translate(280, 130)">
    <rect class="node-card-2" x="0" y="0" width="180" height="280" rx="0" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">02 · RESOLUTION</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">O(1) FIELD MAP</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Name-to-Index</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• Zero String Alloc</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• Array Address</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• Constant Time</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• Microsecond Read</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">HIGH-SPEED ENGINE</text>
  </g>

  <!-- Node 03: Relational MFDB -->
  <g transform="translate(500, 130)">
    <rect class="node-card-3" x="0" y="0" width="180" height="280" rx="0" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">03 · PERSISTENCE</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">MFDB MULTI-FILE</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Manifest Ledgers</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• Entity Cascades</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• Atomic Renames</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• Zero SQL Server</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• 100% File Durability</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">RELATIONAL SUBSTRATE</text>
  </g>

  <!-- Node 04: Subsystem Routers -->
  <g transform="translate(720, 130)">
    <rect class="node-card-4" x="0" y="0" width="180" height="280" rx="0" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">04 · SUBSYSTEMS</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">AUTONOMOUS CLI</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Management Tool</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• Management CMS</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• NewAgent Runner</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• Reminder Tool</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• 57-Col Portrait UI</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">EXECUTION PLATFORMS</text>
  </g>

  <!-- Bottom Telemetry Status Strip -->
  <rect x="30" y="446" width="900" height="64" fill="#0E0E14" stroke="#1A1A22" stroke-width="1" />
  <circle cx="54" cy="478" r="5" fill="#DE2626" />
  <text x="70" y="482" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="700">FLOW STATUS: ACTIVE</text>
  <text x="230" y="482" fill="#888896" font-size="11" font-family="monospace">│  LATENCY: &lt; 0.5ms  │  CONCURRENCY: ISOLATED  │  PERSISTENCE: ATOMIC RENAME</text>
</svg>"""


def generate_frame_svg(frame_idx: int, total_frames: int) -> str:
    """Generates an explicit SVG frame with interpolated data pulse positions for GIF compilation."""
    progress = frame_idx / float(total_frames)

    # 4 stages of active highlight across the loop
    active_node = int(progress * 4) % 4
    colors = ["#2A2A38", "#2A2A38", "#2A2A38", "#2A2A38"]
    colors[active_node] = "#DE2626"
    bg_fills = ["#0E0E14", "#0E0E14", "#0E0E14", "#0E0E14"]
    bg_fills[active_node] = "#161622"

    # Pulse packet position across connectors
    pulse_offset = (progress * 40.0) % 14.0
    cube_float = -8.0 * math.sin(progress * 2.0 * math.pi)

    return f"""<svg width="960" height="540" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#0A0A0C" />
  <rect x="30" y="30" width="900" height="480" rx="0" fill="none" stroke="#1A1A22" stroke-width="1.5" />

  <!-- Corner Ticks -->
  <path d="M 30 54 L 30 30 L 54 30" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 906 30 L 930 30 L 930 54" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 30 486 L 30 510 L 54 510" fill="none" stroke="#333340" stroke-width="2" />
  <path d="M 906 510 L 930 510 L 930 486" fill="none" stroke="#333340" stroke-width="2" />

  <!-- Header Section -->
  <rect x="30" y="30" width="900" height="64" fill="#0E0E14" stroke="#1A1A22" stroke-width="1" />
  <rect x="30" y="30" width="6" height="64" fill="#DE2626" />
  <text x="54" y="60" fill="#FFFFFF" font-size="18" font-family="system-ui, -apple-system, sans-serif" font-weight="800" letter-spacing="1">BEJSON AUTONOMOUS ECOSYSTEM // PIPELINE ARCHITECTURE</text>
  <text x="54" y="80" fill="#888896" font-size="11" font-family="monospace" letter-spacing="2">DETERMINISTIC COMPILATION · RELATIONAL PERSISTENCE · ZERO-SQL</text>

  <!-- 3D Cube Anchor -->
  <g transform="translate(884, {62 + cube_float:.2f})">
    <polygon points="0,-18 20,-7 0,4 -20,-7" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="-20,-7 0,4 0,26 -20,15" fill="#181820" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="0,4 20,-7 20,15 0,26" fill="#DE2626" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
  </g>

  <!-- Stage Connectors -->
  <g stroke="#DE2626" stroke-width="2.5" fill="none" stroke-dasharray="8 6" stroke-dashoffset="{pulse_offset:.2f}">
    <line x1="240" y1="270" x2="280" y2="270" />
    <line x1="460" y1="270" x2="500" y2="270" />
    <line x1="680" y1="270" x2="720" y2="270" />
  </g>
  <polygon points="278,266 284,270 278,274" fill="#DE2626" />
  <polygon points="498,266 504,270 498,274" fill="#DE2626" />
  <polygon points="718,266 724,270 718,274" fill="#DE2626" />

  <!-- Node 01: Declarative Schemas -->
  <g transform="translate(60, 130)">
    <rect x="0" y="0" width="180" height="280" rx="0" fill="{bg_fills[0]}" stroke="{colors[0]}" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">01 · SCHEMAS</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">BEJSON 104a / 105</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Fields Ledger</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• UUIDv4 Identity</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• Strict Typing</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• SHA-256 Hashes</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• Schema Guards</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">IMMUTABLE CONTRACT</text>
  </g>

  <!-- Node 02: O(1) Cache Engine -->
  <g transform="translate(280, 130)">
    <rect x="0" y="0" width="180" height="280" rx="0" fill="{bg_fills[1]}" stroke="{colors[1]}" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">02 · RESOLUTION</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">O(1) FIELD MAP</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Name-to-Index</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• Zero String Alloc</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• Array Address</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• Constant Time</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• Microsecond Read</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">HIGH-SPEED ENGINE</text>
  </g>

  <!-- Node 03: Relational MFDB -->
  <g transform="translate(500, 130)">
    <rect x="0" y="0" width="180" height="280" rx="0" fill="{bg_fills[2]}" stroke="{colors[2]}" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">03 · PERSISTENCE</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">MFDB MULTI-FILE</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Manifest Ledgers</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• Entity Cascades</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• Atomic Renames</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• Zero SQL Server</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• 100% File Durability</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">RELATIONAL SUBSTRATE</text>
  </g>

  <!-- Node 04: Subsystem Routers -->
  <g transform="translate(720, 130)">
    <rect x="0" y="0" width="180" height="280" rx="0" fill="{bg_fills[3]}" stroke="{colors[3]}" stroke-width="1.5" />
    <rect x="0" y="0" width="180" height="40" fill="#181824" stroke="#2A2A38" stroke-width="1" />
    <rect x="0" y="0" width="4" height="40" fill="#DE2626" />
    <text x="14" y="25" fill="#FFFFFF" font-size="13" font-family="system-ui, sans-serif" font-weight="800">04 · SUBSYSTEMS</text>
    <text x="14" y="60" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">AUTONOMOUS CLI</text>
    <line x1="14" y1="72" x2="166" y2="72" stroke="#22222E" stroke-width="1" />
    <text x="14" y="98" fill="#D1D5DB" font-size="11" font-family="monospace">• Management Tool</text>
    <text x="14" y="122" fill="#D1D5DB" font-size="11" font-family="monospace">• Management CMS</text>
    <text x="14" y="146" fill="#D1D5DB" font-size="11" font-family="monospace">• NewAgent Runner</text>
    <text x="14" y="170" fill="#D1D5DB" font-size="11" font-family="monospace">• Reminder Tool</text>
    <text x="14" y="194" fill="#D1D5DB" font-size="11" font-family="monospace">• 57-Col Portrait UI</text>
    <rect x="14" y="224" width="152" height="34" fill="#121218" stroke="#2A2A38" stroke-width="1" />
    <text x="90" y="246" fill="#888896" font-size="10" font-family="monospace" text-anchor="middle">EXECUTION PLATFORMS</text>
  </g>

  <!-- Bottom Telemetry Status Strip -->
  <rect x="30" y="446" width="900" height="64" fill="#0E0E14" stroke="#1A1A22" stroke-width="1" />
  <circle cx="54" cy="478" r="5" fill="#DE2626" />
  <text x="70" y="482" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="700">FLOW STATUS: ACTIVE</text>
  <text x="230" y="482" fill="#888896" font-size="11" font-family="monospace">│  LATENCY: &lt; 0.5ms  │  CONCURRENCY: ISOLATED  │  PERSISTENCE: ATOMIC RENAME</text>
</svg>"""


def main():
    # 1. Write the vector animated SVG
    svg_path = ASSETS_DIR / "bejson_ecosystem_pipeline.svg"
    svg_path.write_text(build_animated_diagram_svg(), encoding="utf-8")
    print(f"[+] Wrote animated diagram SVG: {svg_path}")

    # 2. Render 24 frames for smooth looping animated GIF
    print("[+] Compiling animated diagram GIF frames via native Chromium...")
    temp_dir = REPO_ROOT / "dev" / "temp_diagram_frames"
    temp_dir.mkdir(parents=True, exist_ok=True)
    frames = []
    total_frames = 24

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/data/data/com.termux/files/usr/bin/chromium",
            args=["--no-sandbox", "--disable-gpu"]
        )
        page = browser.new_page(viewport={"width": 960, "height": 540})

        for i in range(total_frames):
            frame_svg = generate_frame_svg(i, total_frames)
            frame_svg_file = temp_dir / f"frame_{i:02d}.svg"
            frame_png_file = temp_dir / f"frame_{i:02d}.png"
            frame_svg_file.write_text(frame_svg, encoding="utf-8")

            page.goto(f"file://{frame_svg_file.resolve()}")
            page.screenshot(path=str(frame_png_file))

            img = Image.open(frame_png_file)
            frames.append(img.convert("P", palette=Image.Palette.ADAPTIVE))

        browser.close()

    # 3. Save animated GIF
    gif_path = ASSETS_DIR / "bejson_ecosystem_pipeline.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=90,  # ~11 fps, ~2.16s loop
        loop=0,
        optimize=True
    )
    print(f"[+] Rendered animated diagram GIF: {gif_path} ({gif_path.stat().st_size // 1024} KB)")

    # Clean up temp frames
    import shutil
    shutil.rmtree(temp_dir, ignore_errors=True)
    print("[+] Cleaned up temporary diagram frames.")


if __name__ == "__main__":
    main()
