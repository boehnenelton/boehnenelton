#!/usr/bin/env python3
"""
Script:        generate_diagram_animations.py
Description:   Synthesizes high-definition, unclipped, 42-frame (3.5-second @ 12 FPS)
               animated vector SVG and optimized GIF diagrams for:
                 1. BEJSON_CMS Flagship Architecture & Publishing Pipeline
                 2. BEJSON Standard Libraries (Foundational 104 vs Integrity 105) & Polyglot Parity
Author:        Elton Boehnen · boehnenelton2024@gmail.com · boehnenelton2024.pages.dev · github.com/boehnenelton
Version:       1.0.0
RELATIONAL_ID: 7f8a9b0c-1d2e-3f4a-5b6c-7d8e9f0a1b2c
"""

import math
import shutil
import subprocess
import logging
from pathlib import Path
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("generate_diagram_animations")

REPO_ROOT = Path("/storage/emulated/0/Admin/Dev/Repos/boehnenelton")
ASSETS_DIR = REPO_ROOT / "assets"
DEV_DIR = REPO_ROOT / "dev"
TEMP_DIR = DEV_DIR / "temp_diagram_anim"


# =============================================================================
# 1. BEJSON_CMS Flagship Architecture Diagram (42 frames @ 12 FPS)
# =============================================================================

def build_cms_frame_svg(frame_idx: int, total_frames: int) -> str:
    progress = frame_idx / float(total_frames)
    active_stage = int(progress * 4) % 4
    pulse_dash = (frame_idx * 4) % 28
    packet_ratio = (frame_idx % (total_frames // 4)) / float(total_frames // 4)
    cube_float = -6.0 * math.sin(progress * 2.0 * math.pi)

    stages = [
        ("STAGE 1 // CLI DISPATCH", "cms-manage.py parses command & routes to 104a.mfdb.bejson master manifest"),
        ("STAGE 2 // PAGE AUTHORING", "Admin (:5000) & PageEditor (:5002) commit two-part page records to pages_db/"),
        ("STAGE 3 // AI SYNTHESIS", "BKS-1 blog engine dispatches CLI_AI & compiles Graphics 105 Asset Triad"),
        ("STAGE 4 // STATIC PUBLISHING", "BEJSON_CMS_Publisher (:5001) compiles static HTML, RSS & synchronizes assets"),
    ]

    # Colors per territory / card based on active stage
    # Territory 0: Web Services & CLI (active on stage 0 & 1)
    # Territory 1: MFDB Storage & Static Build (active on stage 0, 1, 3)
    # Territory 2: AI & Graphics 105 (active on stage 2)
    t0_border = "#DE2626" if active_stage in (0, 1) else "#262636"
    t1_border = "#DE2626" if active_stage in (0, 1, 3) else "#262636"
    t2_border = "#DE2626" if active_stage == 2 else "#262636"

    # Card highlights
    c_cli = "#DE2626" if active_stage == 0 else "#22222E"
    c_admin = "#DE2626" if active_stage == 1 else "#22222E"
    c_editor = "#DE2626" if active_stage == 1 else "#22222E"
    c_mfdb = "#DE2626" if active_stage == 0 else "#22222E"
    c_pages = "#DE2626" if active_stage in (1, 2) else "#22222E"
    c_pub = "#DE2626" if active_stage == 3 else "#22222E"
    c_bks = "#DE2626" if active_stage == 2 else "#22222E"
    c_ai = "#DE2626" if active_stage == 2 else "#22222E"
    c_gfx = "#DE2626" if active_stage == 2 else "#22222E"

    # Packet position interpolation
    pkt_x1 = 286 + int(packet_ratio * (362 - 286))
    pkt_x2 = 608 + int(packet_ratio * (684 - 608))

    return f"""<svg width="960" height="540" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Obsidian Substrate -->
  <rect width="960" height="540" fill="#0A0A0C" />
  <rect x="24" y="20" width="912" height="500" rx="0" fill="none" stroke="#1A1A24" stroke-width="1.5" />

  <!-- Corner Precision Ticks -->
  <path d="M 24 44 L 24 20 L 48 20" fill="none" stroke="#333342" stroke-width="2" />
  <path d="M 912 20 L 936 20 L 936 44" fill="none" stroke="#333342" stroke-width="2" />
  <path d="M 24 496 L 24 520 L 48 520" fill="none" stroke="#333342" stroke-width="2" />
  <path d="M 912 520 L 936 520 L 936 496" fill="none" stroke="#333342" stroke-width="2" />

  <!-- Header Strip -->
  <rect x="24" y="20" width="912" height="60" fill="#0E0E14" stroke="#1A1A24" stroke-width="1" />
  <rect x="24" y="20" width="6" height="60" fill="#DE2626" />
  <text x="46" y="47" fill="#FFFFFF" font-size="16" font-family="system-ui, -apple-system, sans-serif" font-weight="800" letter-spacing="0.8">BEJSON_CMS // FOUR-SERVICE TOPOLOGY &amp; PUBLISHING PIPELINE</text>
  <text x="46" y="67" fill="#888896" font-size="10.5" font-family="monospace" letter-spacing="1.5">ZERO-SQL ATOMIC PERSISTENCE · MFDB FLAT-FILE STORAGE · BKS-1 AI WRITER · GRAPHICS 105</text>

  <!-- 3D Isometric Cube Visual Anchor -->
  <g transform="translate(896, {50 + cube_float:.2f})">
    <polygon points="0,-16 18,-6 0,4 -18,-6" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="-18,-6 0,4 0,22 -18,12" fill="#181820" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="0,4 18,-6 18,12 0,22" fill="#DE2626" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
  </g>

  <!-- ================= ZONE 1: WEB SERVICES & CLI ================= -->
  <g transform="translate(40, 94)">
    <rect x="0" y="0" width="268" height="364" fill="#0C0C12" stroke="{t0_border}" stroke-width="1.5" />
    <rect x="0" y="0" width="268" height="28" fill="#14141E" stroke="{t0_border}" stroke-width="1" />
    <text x="12" y="19" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">01 · WEB SERVICES &amp; CLI TIER</text>

    <!-- Card 1: CLI -->
    <g transform="translate(11, 40)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{c_cli}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">cms-manage.py CLI</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Unified 57-Col Router</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Multi-service daemon controls</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Reset, backup &amp; schema audit</text>
    </g>

    <!-- Card 2: Admin -->
    <g transform="translate(11, 146)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{c_admin}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#FFFFFF" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">BEJSON_CMS_Admin :5000</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Site Master &amp; Navigation</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Taxonomy &amp; category routes</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Media asset dropzone &amp; logs</text>
    </g>

    <!-- Card 3: PageEditor -->
    <g transform="translate(11, 252)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{c_editor}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">BEJSON_CMS_PageEditor :5002</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Authoritative Editor</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Pure-HTML visual composing</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• BKS-1 AI post integration</text>
    </g>
  </g>

  <!-- Connectors Zone 1 -> Zone 2 -->
  <line x1="308" y1="180" x2="362" y2="180" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />
  <line x1="308" y1="286" x2="362" y2="286" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />
  <line x1="308" y1="392" x2="362" y2="392" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />

  <!-- Animated Packet traveling Z1 -> Z2 -->
  <circle cx="{pkt_x1}" cy="180" r="4.5" fill="#DE2626" />

  <!-- ================= ZONE 2: MFDB STORAGE ================= -->
  <g transform="translate(362, 94)">
    <rect x="0" y="0" width="268" height="364" fill="#0C0C12" stroke="{t1_border}" stroke-width="1.5" />
    <rect x="0" y="0" width="268" height="28" fill="#14141E" stroke="{t1_border}" stroke-width="1" />
    <text x="12" y="19" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">02 · MFDB STORAGE &amp; BUILD</text>

    <!-- Card 4: MFDB Master -->
    <g transform="translate(11, 40)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{c_mfdb}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">104a.mfdb.bejson</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Master Manifest Ledger</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• O(1) field map index cache</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Entity relationships &amp; locks</text>
    </g>

    <!-- Card 5: Two-Part Page Storage -->
    <g transform="translate(11, 146)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{c_pages}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#FFFFFF" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">pages_db/ &amp; pagerecord</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Two-Part Flat-File Model</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Clean HTML body + BEJSON meta</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Atomic temporary file rename</text>
    </g>

    <!-- Card 6: Publisher -->
    <g transform="translate(11, 252)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{c_pub}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">BEJSON_CMS_Publisher :5001</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Static Compilation</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Jinja2 theme rendering</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Static dist/, RSS/Atom &amp; assets</text>
    </g>
  </g>

  <!-- Connectors Zone 2 -> Zone 3 -->
  <line x1="630" y1="180" x2="684" y2="180" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />
  <line x1="630" y1="286" x2="684" y2="286" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />
  <line x1="630" y1="392" x2="684" y2="392" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />

  <!-- Animated Packet traveling Z2 -> Z3 -->
  <circle cx="{pkt_x2}" cy="286" r="4.5" fill="#DE2626" />

  <!-- ================= ZONE 3: BKS-1 AI & GRAPHICS 105 ================= -->
  <g transform="translate(684, 94)">
    <rect x="0" y="0" width="236" height="364" fill="#0C0C12" stroke="{t2_border}" stroke-width="1.5" />
    <rect x="0" y="0" width="236" height="28" fill="#14141E" stroke="{t2_border}" stroke-width="1" />
    <text x="12" y="19" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">03 · BKS-1 AI &amp; GRAPHICS 105</text>

    <!-- Card 7: BKS Engine -->
    <g transform="translate(10, 40)">
      <rect x="0" y="0" width="216" height="92" fill="#12121A" stroke="{c_bks}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">BKS-1 Blog Job Engine</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Automated Authoring</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• 4-part deep technical plan</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Draft, review, render &amp; post</text>
    </g>

    <!-- Card 8: CLI AI Dispatch -->
    <g transform="translate(10, 146)">
      <rect x="0" y="0" width="216" height="92" fill="#12121A" stroke="{c_ai}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#FFFFFF" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">CLI_AI REST Dispatch</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Zero-SDK AI Engine</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Gemini Interactions API</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Stateful multi-turn loops</text>
    </g>

    <!-- Card 9: Graphics 105 -->
    <g transform="translate(10, 252)">
      <rect x="0" y="0" width="216" height="92" fill="#12121A" stroke="{c_gfx}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">Graphics 105 Triad</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Visual Asset Engine</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• 1280x640 SVG vector hero</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• WebP &amp; PNG synchronized</text>
    </g>
  </g>

  <!-- ================= BOTTOM TELEMETRY STATUS STRIP ================= -->
  <rect x="24" y="468" width="912" height="52" fill="#0E0E14" stroke="#1A1A24" stroke-width="1" />
  <circle cx="44" cy="494" r="5" fill="#DE2626" />
  <text x="58" y="498" fill="#FFFFFF" font-size="11.5" font-family="monospace" font-weight="700">{stages[active_stage][0]}</text>
  <text x="310" y="498" fill="#888896" font-size="10.5" font-family="monospace">│ {stages[active_stage][1]}</text>
</svg>"""


# =============================================================================
# 2. BEJSON Standard Libraries (Foundational 104 vs Integrity 105) (42 frames @ 12 FPS)
# =============================================================================

def build_libraries_frame_svg(frame_idx: int, total_frames: int) -> str:
    progress = frame_idx / float(total_frames)
    active_phase = int(progress * 3) % 3
    pulse_dash = (frame_idx * 4) % 28
    cube_float = -6.0 * math.sin(progress * 2.0 * math.pi)

    phases = [
        ("ERA 104 // FOUNDATIONAL TABULAR STORAGE", "O(1) Field Map Cache · Tabular Envelopes · MFDB v1.31 Multi-File Manifests"),
        ("ERA 105 // INTEGRITY RECORD ERA", "UUIDv4 Primary Keys · Record Hashes · Foreign Key Cascades & Graphics 105"),
        ("POLYGLOT PARITY // ZERO DEPENDENCY", "Unified Standard Libraries Across Python (Lib_PY), TS, JS & Bash (Lib_SH)"),
    ]

    b0 = "#DE2626" if active_phase == 0 else "#22222E"
    b1 = "#DE2626" if active_phase == 1 else "#22222E"
    b2 = "#DE2626" if active_phase == 2 else "#22222E"

    # Packet across upgrade bridge
    pkt_x = 308 + int(((frame_idx % (total_frames // 2)) / float(total_frames // 2)) * (362 - 308))

    return f"""<svg width="960" height="540" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <!-- Obsidian Substrate -->
  <rect width="960" height="540" fill="#0A0A0C" />
  <rect x="24" y="20" width="912" height="500" rx="0" fill="none" stroke="#1A1A24" stroke-width="1.5" />

  <!-- Corner Precision Ticks -->
  <path d="M 24 44 L 24 20 L 48 20" fill="none" stroke="#333342" stroke-width="2" />
  <path d="M 912 20 L 936 20 L 936 44" fill="none" stroke="#333342" stroke-width="2" />
  <path d="M 24 496 L 24 520 L 48 520" fill="none" stroke="#333342" stroke-width="2" />
  <path d="M 912 520 L 936 520 L 936 496" fill="none" stroke="#333342" stroke-width="2" />

  <!-- Header Strip -->
  <rect x="24" y="20" width="912" height="60" fill="#0E0E14" stroke="#1A1A24" stroke-width="1" />
  <rect x="24" y="20" width="6" height="60" fill="#DE2626" />
  <text x="46" y="47" fill="#FFFFFF" font-size="16" font-family="system-ui, -apple-system, sans-serif" font-weight="800" letter-spacing="0.8">BEJSON STANDARD LIBRARIES // ERA EVOLUTION &amp; POLYGLOT PARITY</text>
  <text x="46" y="67" fill="#888896" font-size="10.5" font-family="monospace" letter-spacing="1.5">FOUNDATIONAL ERA 104 vs INTEGRITY ERA 105 · UNIFIED INTERFACES ACROSS PY, TS, JS &amp; SH</text>

  <!-- 3D Isometric Cube Visual Anchor -->
  <g transform="translate(896, {50 + cube_float:.2f})">
    <polygon points="0,-16 18,-6 0,4 -18,-6" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="-18,-6 0,4 0,22 -18,12" fill="#181820" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
    <polygon points="0,4 18,-6 18,12 0,22" fill="#DE2626" stroke="#FFFFFF" stroke-width="1" stroke-linejoin="round" />
  </g>

  <!-- ================= COLUMN 1: FOUNDATIONAL ERA 104 ================= -->
  <g transform="translate(40, 94)">
    <rect x="0" y="0" width="268" height="364" fill="#0C0C12" stroke="{b0}" stroke-width="1.5" />
    <rect x="0" y="0" width="268" height="28" fill="#14141E" stroke="{b0}" stroke-width="1" />
    <text x="12" y="19" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">FOUNDATIONAL ERA (LIBRARIES_104)</text>

    <!-- Card 1: 104 Core -->
    <g transform="translate(11, 40)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{b0}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">lib_bejson_core (104)</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">O(1) Field Map Engine</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Constant-time column lookups</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• MFDB v1.31 multi-file manifests</text>
    </g>

    <!-- Card 2: 104 AI & CMS -->
    <g transform="translate(11, 146)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{b0}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#FFFFFF" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">lib_bejson_ai_cms (104)</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">CMS &amp; AI Integration</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• BKS-1 technical blog engine</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Project Chunker &amp; scoop logic</text>
    </g>

    <!-- Card 3: 104 HTML & Diagrams -->
    <g transform="translate(11, 252)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{b0}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">lib_bejson_html_diag (104)</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Spatial Web &amp; Diagrammer</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• 8-lane Ry=32px UI grids</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Read-only SVG diagram canvas</text>
    </g>
  </g>

  <!-- Connectors: 104 -> 105 Upgrade Bridge -->
  <line x1="308" y1="180" x2="362" y2="180" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />
  <circle cx="{pkt_x}" cy="180" r="4.5" fill="#DE2626" />

  <!-- ================= COLUMN 2: INTEGRITY ERA 105 ================= -->
  <g transform="translate(362, 94)">
    <rect x="0" y="0" width="268" height="364" fill="#0C0C12" stroke="{b1}" stroke-width="1.5" />
    <rect x="0" y="0" width="268" height="28" fill="#14141E" stroke="{b1}" stroke-width="1" />
    <text x="12" y="19" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">INTEGRITY ERA (LIBRARIES_105)</text>

    <!-- Card 4: 105 Core -->
    <g transform="translate(11, 40)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{b1}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">lib_bejson_core (105)</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">UUIDv4 Record Keys</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Primary keys &amp; SHA-256 hashes</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• MFDB v1.40 FK cascade cascades</text>
    </g>

    <!-- Card 5: 105 Graphics -->
    <g transform="translate(11, 146)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{b1}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#FFFFFF" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">lib_bejson_graphics (105)</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Graphics 105 Engine</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Row-per-frame animation schema</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Blank-slate dynamic SVG/GIF</text>
    </g>

    <!-- Card 6: 105 Standards -->
    <g transform="translate(11, 252)">
      <rect x="0" y="0" width="246" height="92" fill="#12121A" stroke="{b1}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">lib_bejson_tax_std (105)</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Standards &amp; Registries</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Global schema registries</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• MTV architecture &amp; AST guards</text>
    </g>
  </g>

  <!-- Connectors: 105 -> Polyglot Runtimes -->
  <line x1="630" y1="180" x2="684" y2="180" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />
  <line x1="630" y1="286" x2="684" y2="286" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />
  <line x1="630" y1="392" x2="684" y2="392" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}" />

  <!-- ================= COLUMN 3: POLYGLOT RUNTIMES & APPS ================= -->
  <g transform="translate(684, 94)">
    <rect x="0" y="0" width="236" height="364" fill="#0C0C12" stroke="{b2}" stroke-width="1.5" />
    <rect x="0" y="0" width="236" height="28" fill="#14141E" stroke="{b2}" stroke-width="1" />
    <text x="12" y="19" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">POLYGLOT ECOSYSTEM PARITY</text>

    <!-- Card 7: Zero Dependency -->
    <g transform="translate(10, 40)">
      <rect x="0" y="0" width="216" height="92" fill="#12121A" stroke="{b2}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">Zero-Dependency Core</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Four-Language Parity</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Python (Lib_PY / stdlib json)</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• TS, JS &amp; Bash (Lib_SH / awk)</text>
    </g>

    <!-- Card 8: BEJSON_CMS -->
    <g transform="translate(10, 146)">
      <rect x="0" y="0" width="216" height="92" fill="#12121A" stroke="{b2}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#FFFFFF" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">BEJSON_CMS (Flagship)</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Zero-SQL Publishing</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• 4 microservices + BKS AI</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Pure flat-file MFDB storage</text>
    </g>

    <!-- Card 9: Subsystems -->
    <g transform="translate(10, 252)">
      <rect x="0" y="0" width="216" height="92" fill="#12121A" stroke="{b2}" stroke-width="1.4" />
      <rect x="0" y="0" width="4" height="92" fill="#DE2626" />
      <text x="12" y="22" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">Autonomous Subsystems</text>
      <text x="12" y="40" fill="#DE2626" font-size="10" font-family="monospace">Stateful Automation</text>
      <text x="12" y="60" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• NewAgent &amp; JobMaker</text>
      <text x="12" y="78" fill="#D1D5DB" font-size="9.5" font-family="system-ui, sans-serif">• Project_Chunker &amp; Reminder</text>
    </g>
  </g>

  <!-- ================= BOTTOM TELEMETRY STATUS STRIP ================= -->
  <rect x="24" y="468" width="912" height="52" fill="#0E0E14" stroke="#1A1A24" stroke-width="1" />
  <circle cx="44" cy="494" r="5" fill="#DE2626" />
  <text x="58" y="498" fill="#FFFFFF" font-size="11.5" font-family="monospace" font-weight="700">{phases[active_phase][0]}</text>
  <text x="365" y="498" fill="#888896" font-size="10.5" font-family="monospace">│ {phases[active_phase][1]}</text>
</svg>"""


# =============================================================================
# 3. Compilation Engine (Playwright + FFmpeg 2-Pass Palettegen)
# =============================================================================

def render_diagram_animation(
    slug: str,
    frame_builder,
    total_frames: int = 42,
    fps: int = 12,
) -> Path:
    frame_dir = TEMP_DIR / slug
    if frame_dir.exists():
        shutil.rmtree(frame_dir)
    frame_dir.mkdir(parents=True, exist_ok=True)

    # 1. Write the static vector SVG (frame 0)
    svg_path = ASSETS_DIR / f"{slug}.svg"
    svg_path.write_text(frame_builder(0, total_frames), encoding="utf-8")
    logger.info("Wrote static vector SVG: %s", svg_path.name)

    # 2. Render discrete PNG frames via headless Chromium
    logger.info("Rendering %d frames for %s via Chromium...", total_frames, slug)
    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/data/data/com.termux/files/usr/lib/chromium/chrome",
            args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
        )
        page = browser.new_page(viewport={"width": 960, "height": 540})
        for i in range(total_frames):
            frame_svg = frame_builder(i, total_frames)
            html_content = (
                "<!DOCTYPE html><html><head><style>"
                "* { margin: 0; padding: 0; background: #0A0A0C; overflow: hidden; }"
                "</style></head><body>"
                f"{frame_svg}</body></html>"
            )
            page.set_content(html_content, wait_until="load")
            frame_png = frame_dir / f"frame_{i:04d}.png"
            page.screenshot(path=str(frame_png), clip={"x": 0, "y": 0, "width": 960, "height": 540})
        browser.close()

    # 3. Compile optimized GIF via FFmpeg 2-pass
    gif_path = ASSETS_DIR / f"{slug}.gif"
    palette_path = frame_dir / "palette.png"

    subprocess.run(
        [
            "ffmpeg", "-y", "-framerate", str(fps),
            "-i", str(frame_dir / "frame_%04d.png"),
            "-vf", "palettegen=stats_mode=diff",
            str(palette_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    subprocess.run(
        [
            "ffmpeg", "-y", "-framerate", str(fps),
            "-i", str(frame_dir / "frame_%04d.png"),
            "-i", str(palette_path),
            "-lavfi", "paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle",
            str(gif_path),
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    shutil.rmtree(frame_dir, ignore_errors=True)
    duration = total_frames / float(fps)
    size_kb = gif_path.stat().st_size // 1024
    logger.info("Compiled %s (%d KB, %d frames @ %d FPS = %.2fs)", gif_path.name, size_kb, total_frames, fps, duration)
    return gif_path


def main():
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    render_diagram_animation("bejson_cms_architecture_diagram", build_cms_frame_svg, total_frames=42, fps=12)
    render_diagram_animation("bejson_104_105_libraries_diagram", build_libraries_frame_svg, total_frames=42, fps=12)
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
    logger.info("All diagram animations synthesized successfully.")


if __name__ == "__main__":
    main()
