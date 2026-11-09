#!/usr/bin/env python3
"""
Script:        generate_contextual_animations.py
Description:   Copies the 15 Zero-Bloat Architecture slides into assets/slides/ and
               synthesizes 3 contextual 3.5-second (42 frames @ 12 FPS) animated SVG/GIF
               architecture showcases for:
                 1. NewAgent & JobMaker (5-Surface & 6-Partition Context Bubble Engine)
                 2. Project_Chunker (Dual-MFDB & 4-Stage Zero-Data-Loss Atomic Scoop)
                 3. Reminder_Tool (BEJSON 104a Active/Completed Lifecycle & Termux .bashrc Launch)
Author:        Elton Boehnen · boehnenelton2024@gmail.com · boehnenelton2024.pages.dev · github.com/boehnenelton
Version:       1.0.0
RELATIONAL_ID: c4189d2e-8a73-4f10-9b62-3e1984a05c71
"""

import json
import logging
import math
import os
import shutil
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("generate_contextual_animations")

SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parent.parent
ASSETS_DIR = REPO_ROOT / "assets"
SLIDES_DIR = ASSETS_DIR / "slides"
TEMP_FRAMES_ROOT = REPO_ROOT / "dev" / "temp_ctx_frames"


def resolve_download_dir() -> Path:
    """Resolve DOWNLOAD_ROOT dynamically from DEFINITIONS_FILE or environment."""
    definitions_path = os.environ.get("DEFINITIONS_FILE")
    if definitions_path and Path(definitions_path).exists():
        try:
            with open(definitions_path, "r", encoding="utf-8") as definitions_handle:
                definitions_payload = json.load(definitions_handle)
            fields_list = definitions_payload.get("Fields", [])
            field_map = {field_entry["name"]: idx for idx, field_entry in enumerate(fields_list)}
            name_idx = field_map.get("Variable_Name")
            val_idx = field_map.get("Variable_Value")
            if name_idx is not None and val_idx is not None:
                for row_record in definitions_payload.get("Values", []):
                    if row_record[name_idx] == "DOWNLOAD_ROOT":
                        return Path(row_record[val_idx])
        except Exception as exc:
            logger.warning("Failed reading DEFINITIONS_FILE: %s", exc)
    return Path(os.environ.get("DOWNLOAD_ROOT", str(REPO_ROOT.parent.parent.parent / "Download")))


DOWNLOAD_DIR = resolve_download_dir()

SLIDE_MAPPING = [
    (1, "slide_01_data_revolution.png"),
    (2, "slide_02_architectural_scam.png"),
    (3, "slide_03_paradigm_shift_bejson_mfdb.png"),
    (4, "slide_04_four_stage_execution_pipeline.png"),
    (5, "slide_05_anatomy_bejson_schema.png"),
    (6, "slide_06_mfdb_federation.png"),
    (7, "slide_07_standard_libraries_matrix.png"),
    (8, "slide_08_graphics_105_visual_engine.png"),
    (9, "slide_09_flagship_bejson_cms.png"),
    (10, "slide_10_two_part_page_storage.png"),
    (11, "slide_11_polyglot_natively.png"),
    (12, "slide_12_autonomous_subsystems.png"),
    (13, "slide_13_system_error_registry.png"),
    (14, "slide_14_design_law_cubic_anchors.png"),
    (15, "slide_15_synthesis_zero_bloat.png"),
]


def copy_slide_deck_assets() -> None:
    """Copy all 15 Zero-Bloat Architecture slides into assets/slides/."""
    SLIDES_DIR.mkdir(parents=True, exist_ok=True)
    for slide_num, target_filename in SLIDE_MAPPING:
        source_path = DOWNLOAD_DIR / f"Zero-Bloat_Architecture_-_Slide_{slide_num}.png"
        target_path = SLIDES_DIR / target_filename
        if not source_path.exists():
            raise FileNotFoundError(f"Missing source slide: {source_path}")
        shutil.copy2(source_path, target_path)
        logger.info("Copied Slide %02d -> %s", slide_num, target_path.relative_to(REPO_ROOT))


def build_newagent_frame_svg(frame_idx: int, total_frames: int) -> str:
    """
    Generate frame SVG for Animation 1: NewAgent & JobMaker (v1.2.15 / PKG 135)
    5 Operational Surfaces + 6-Partition Dynamic Context Bubble + Dual AI Engine.
    Duration: 42 frames @ 12 FPS = 3.50 seconds.
    """
    progress = frame_idx / float(total_frames)
    active_stage = int(progress * 6) % 6
    pulse_dash = (frame_idx * 4) % 28
    cube_y = -6.0 * math.sin(progress * 2.0 * math.pi)

    partitions = [
        ("PERSISTENT POLICY", "20%", "Standing directives & persona"),
        ("ACTIVE TASKS", "20%", "JobMaker checklist state"),
        ("ENV DEFINITIONS", "5%", "definitions.json pointers"),
        ("KEYWORD TRIGGERS", "30%", "Matched file & AST context"),
        ("KNOWLEDGE POOL", "15%", "Periodic domain skill drips"),
        ("CWD WORKSPACE", "10%", "Local context.bejson & AGENTS.md"),
    ]

    partition_rows_svg = []
    for idx, (label, pct, desc) in enumerate(partitions):
        y_pos = 162 + idx * 44
        is_active = idx == active_stage
        stroke_col = "#DE2626" if is_active else "#2A2A38"
        fill_col = "#1C1014" if is_active else "#101018"
        badge_fill = "#DE2626" if is_active else "#1E1E2A"
        partition_rows_svg.append(
            f'<g transform="translate(364, {y_pos})">'
            f'<rect x="0" y="0" width="272" height="36" fill="{fill_col}" stroke="{stroke_col}" stroke-width="1.5"/>'
            f'<rect x="0" y="0" width="48" height="36" fill="{badge_fill}"/>'
            f'<text x="24" y="23" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700" text-anchor="middle">{pct}</text>'
            f'<text x="58" y="15" fill="#FFFFFF" font-size="10" font-family="monospace" font-weight="700">{label}</text>'
            f'<text x="58" y="29" fill="#9CA3AF" font-size="9" font-family="monospace">{desc}</text>'
            f'</g>'
        )

    surfaces = [
        ("01 · agent.py", "Interactive Terminal Conversant"),
        ("02 · cliagent.py", "Headless JSON Pipe Daemon"),
        ("03 · config_manager.py", "57-Col 67-Option TUI Matrix"),
        ("04 · webagent.py", "Loopback Web Shell (:5001)"),
        ("05 · JobMaker.py", "Task Blueprint Stager (:5002)"),
    ]
    active_surf = int(progress * 5) % 5
    surface_cards_svg = []
    for idx, (s_title, s_sub) in enumerate(surfaces):
        y_pos = 162 + idx * 53
        is_s_active = idx == active_surf
        s_stroke = "#DE2626" if is_s_active else "#262634"
        s_fill = "#181016" if is_s_active else "#0E0E14"
        surface_cards_svg.append(
            f'<g transform="translate(52, {y_pos})">'
            f'<rect x="0" y="0" width="248" height="44" fill="{s_fill}" stroke="{s_stroke}" stroke-width="1.5"/>'
            f'<rect x="0" y="0" width="5" height="44" fill="{s_stroke}"/>'
            f'<text x="14" y="18" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">{s_title}</text>'
            f'<text x="14" y="34" fill="#888896" font-size="9.5" font-family="monospace">{s_sub}</text>'
            f'</g>'
        )

    engine_active = int(progress * 2) % 2
    eng0_stroke = "#DE2626" if engine_active == 0 else "#2A2A38"
    eng1_stroke = "#DE2626" if engine_active == 1 else "#2A2A38"

    return f"""<svg width="960" height="540" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#0A0A0C" />
  <rect x="24" y="24" width="912" height="492" fill="none" stroke="#1E1E2A" stroke-width="1.5" />
  <rect x="24" y="24" width="912" height="62" fill="#0E0E14" stroke="#1E1E2A" stroke-width="1" />
  <rect x="24" y="24" width="6" height="62" fill="#DE2626" />
  <text x="46" y="52" fill="#FFFFFF" font-size="17" font-family="system-ui, sans-serif" font-weight="800" letter-spacing="0.8">NEWAGENT &amp; JOBMAKER (v1.2.15 · PKG 135) // CONTEXT BUBBLE &amp; EXECUTION TOPOLOGY</text>
  <text x="46" y="72" fill="#888896" font-size="10.5" font-family="monospace" letter-spacing="1.5">5 SURFACES · 6-PARTITION DYNAMIC CONTEXT BUBBLE · DUAL AI ENGINE · NATIVE AGY SKILLS</text>

  <g transform="translate(894, {55 + cube_y:.2f})">
    <polygon points="0,-16 18,-6 0,4 -18,-6" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="1"/>
    <polygon points="-18,-6 0,4 0,24 -18,14" fill="#181820" stroke="#FFFFFF" stroke-width="1"/>
    <polygon points="0,4 18,-6 18,14 0,24" fill="#DE2626" stroke="#FFFFFF" stroke-width="1"/>
  </g>

  <!-- Column 1: 5 Operational Surfaces -->
  <rect x="40" y="106" width="272" height="336" fill="#0C0C12" stroke="#222230" stroke-width="1" />
  <rect x="40" y="106" width="272" height="38" fill="#14141E" stroke="#222230" stroke-width="1" />
  <text x="54" y="130" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="700">01 · 5 OPERATIONAL SURFACES</text>
  {"".join(surface_cards_svg)}

  <!-- Animated Connector 1 -> 2 -->
  <line x1="312" y1="274" x2="352" y2="274" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="8 6" stroke-dashoffset="-{pulse_dash}" />
  <polygon points="348,269 356,274 348,279" fill="#DE2626" />

  <!-- Column 2: 6-Partition Dynamic Context Bubble -->
  <rect x="352" y="106" width="296" height="336" fill="#0C0C12" stroke="#DE2626" stroke-width="1.5" />
  <rect x="352" y="106" width="296" height="38" fill="#1C1014" stroke="#DE2626" stroke-width="1" />
  <text x="366" y="130" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="700">02 · CONTEXT_BUBBLE.MD (6 SLOTS)</text>
  {"".join(partition_rows_svg)}

  <!-- Animated Connector 2 -> 3 -->
  <line x1="648" y1="274" x2="688" y2="274" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="8 6" stroke-dashoffset="-{pulse_dash}" />
  <polygon points="684,269 692,274 684,279" fill="#DE2626" />

  <!-- Column 3: Dual AI Engine & Action Execution -->
  <rect x="688" y="106" width="232" height="336" fill="#0C0C12" stroke="#222230" stroke-width="1" />
  <rect x="688" y="106" width="232" height="38" fill="#14141E" stroke="#222230" stroke-width="1" />
  <text x="702" y="130" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="700">03 · DUAL AI &amp; SKILLS</text>

  <g transform="translate(700, 162)">
    <rect x="0" y="0" width="208" height="78" fill="#12121A" stroke="{eng0_stroke}" stroke-width="1.5"/>
    <text x="12" y="22" fill="#DE2626" font-size="11" font-family="monospace" font-weight="700">ENGINE A: ASYNC REST POOL</text>
    <text x="12" y="42" fill="#D1D5DB" font-size="9.5" font-family="monospace">• 12-Key Affinity Rotation</text>
    <text x="12" y="58" fill="#D1D5DB" font-size="9.5" font-family="monospace">• key_state.bejson Cooldown</text>
  </g>

  <g transform="translate(700, 254)">
    <rect x="0" y="0" width="208" height="78" fill="#12121A" stroke="{eng1_stroke}" stroke-width="1.5"/>
    <text x="12" y="22" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">ENGINE B: INTERACTIONS API</text>
    <text x="12" y="42" fill="#D1D5DB" font-size="9.5" font-family="monospace">• previous_interaction_id</text>
    <text x="12" y="58" fill="#D1D5DB" font-size="9.5" font-family="monospace">• Stateful Tool Scoping</text>
  </g>

  <g transform="translate(700, 346)">
    <rect x="0" y="0" width="208" height="78" fill="#161014" stroke="#DE2626" stroke-width="1.2"/>
    <text x="12" y="22" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">ACTION &amp; AGY SKILL TAGS</text>
    <text x="12" y="42" fill="#D1D5DB" font-size="9.5" font-family="monospace">• &lt;exec&gt; / &lt;edit_file&gt;</text>
    <text x="12" y="58" fill="#D1D5DB" font-size="9.5" font-family="monospace">• &lt;agy_skill action="run"/&gt;</text>
  </g>

  <!-- Bottom Telemetry Strip -->
  <rect x="24" y="458" width="912" height="58" fill="#0E0E14" stroke="#1E1E2A" stroke-width="1" />
  <circle cx="48" cy="487" r="5" fill="#DE2626" />
  <text x="64" y="491" fill="#FFFFFF" font-size="11.5" font-family="monospace" font-weight="700">BUBBLE SYNTHESIS: ACTIVE SLOT [{partitions[active_stage][0]}]</text>
  <text x="520" y="491" fill="#888896" font-size="10.5" font-family="monospace">│ TREE-WALK: / -&gt; CWD (AGENTS.md) │ SHA-256 DEDUP: VERIFIED</text>
</svg>"""


def build_project_chunker_frame_svg(frame_idx: int, total_frames: int) -> str:
    """
    Generate frame SVG for Animation 2: Project_Chunker (v1.8.0 / PKG 114)
    Dual-MFDB Architecture & 4-Stage Zero-Data-Loss Atomic Scoop Verification Pipeline.
    Duration: 42 frames @ 12 FPS = 3.50 seconds.
    """
    progress = frame_idx / float(total_frames)
    active_stage = int(progress * 4) % 4
    pulse_dash = (frame_idx * 4) % 28

    scoop_stages = [
        ("STAGE 1 · BUILD SNAPSHOT", "64 KB streaming SHA-256 + Base64 binary pack", "10 Canonical Fields -> .bejson"),
        ("STAGE 2 · VERIFY DISK WRITE", "os.fsync flush + re-open & re-parse from disk", "Structural & schema gate check"),
        ("STAGE 3 · LIVE BYTE AUDIT", "Compare every live file byte & SHA-256 digest", "Abort w/ ZERO deletes on mismatch"),
        ("STAGE 4 · VERIFIED UNLINK", "100% byte-verified source unlink & dir prune", "Zero-Data-Loss Scoop Complete"),
    ]

    stage_boxes = []
    for idx, (st_title, st_line1, st_line2) in enumerate(scoop_stages):
        x_pos = 44 + idx * 222
        is_active = idx == active_stage
        stroke_col = "#DE2626" if is_active else "#2A2A38"
        fill_col = "#1C1014" if is_active else "#101018"
        header_fill = "#DE2626" if is_active else "#1A1A26"
        stage_boxes.append(
            f'<g transform="translate({x_pos}, 288)">'
            f'<rect x="0" y="0" width="204" height="146" fill="{fill_col}" stroke="{stroke_col}" stroke-width="1.8"/>'
            f'<rect x="0" y="0" width="204" height="32" fill="{header_fill}"/>'
            f'<text x="10" y="20" fill="#FFFFFF" font-size="10.5" font-family="monospace" font-weight="800">{st_title}</text>'
            f'<text x="10" y="58" fill="#E5E7EB" font-size="9.5" font-family="monospace">{st_line1[:28]}</text>'
            f'<text x="10" y="74" fill="#E5E7EB" font-size="9.5" font-family="monospace">{st_line1[28:]}</text>'
            f'<line x1="10" y1="92" x2="194" y2="92" stroke="#262636" stroke-width="1"/>'
            f'<text x="10" y="114" fill="#DE2626" font-size="9.5" font-family="monospace" font-weight="700">{st_line2[:29]}</text>'
            f'<text x="10" y="130" fill="#9CA3AF" font-size="9" font-family="monospace">{st_line2[29:]}</text>'
            f'</g>'
        )

    return f"""<svg width="960" height="540" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#0A0A0C" />
  <rect x="24" y="24" width="912" height="492" fill="none" stroke="#1E1E2A" stroke-width="1.5" />
  <rect x="24" y="24" width="912" height="62" fill="#0E0E14" stroke="#1E1E2A" stroke-width="1" />
  <rect x="24" y="24" width="6" height="62" fill="#DE2626" />
  <text x="46" y="52" fill="#FFFFFF" font-size="17" font-family="system-ui, sans-serif" font-weight="800" letter-spacing="0.8">PROJECT_CHUNKER (v1.8.0 · PKG 114) // DUAL-MFDB &amp; ATOMIC SCOOP ENGINE</text>
  <text x="46" y="72" fill="#888896" font-size="10.5" font-family="monospace" letter-spacing="1.5">3-TIER UUID GOVERNANCE · 10-FIELD SNAPSHOT LEDGER · 4-STAGE ZERO-DATA-LOSS SCOOP</text>

  <!-- Top Tier: Dual-MFDB 3-Pillar Data Model -->
  <g transform="translate(44, 104)">
    <rect x="0" y="0" width="272" height="136" fill="#101018" stroke="#2A2A38" stroke-width="1.5"/>
    <rect x="0" y="0" width="5" height="136" fill="#DE2626"/>
    <text x="16" y="26" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">01 · MASTER REGISTRY MFDB</text>
    <text x="16" y="46" fill="#DE2626" font-size="10" font-family="monospace">storage/master/data/registry.bejson</text>
    <text x="16" y="70" fill="#D1D5DB" font-size="10" font-family="monospace">• Project_GUID (Master-Assigned)</text>
    <text x="16" y="90" fill="#D1D5DB" font-size="10" font-family="monospace">• Versioned_UUID Primary Key</text>
    <text x="16" y="110" fill="#D1D5DB" font-size="10" font-family="monospace">• Status: active | archived</text>
  </g>

  <line x1="316" y1="172" x2="344" y2="172" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}"/>

  <g transform="translate(344, 104)">
    <rect x="0" y="0" width="272" height="136" fill="#101018" stroke="#2A2A38" stroke-width="1.5"/>
    <rect x="0" y="0" width="5" height="136" fill="#FFFFFF"/>
    <text x="16" y="26" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">02 · HISTORICAL TRACKERS</text>
    <text x="16" y="46" fill="#DE2626" font-size="10" font-family="monospace">storage/trackers/data/&lt;proj&gt;.bejson</text>
    <text x="16" y="70" fill="#D1D5DB" font-size="10" font-family="monospace">• Full bejson_project.json Lineage</text>
    <text x="16" y="90" fill="#D1D5DB" font-size="10" font-family="monospace">• Solid Integer Version History</text>
    <text x="16" y="110" fill="#D1D5DB" font-size="10" font-family="monospace">• Superseded Conflict Routing</text>
  </g>

  <line x1="616" y1="172" x2="644" y2="172" stroke="#DE2626" stroke-width="2" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}"/>

  <g transform="translate(644, 104)">
    <rect x="0" y="0" width="272" height="136" fill="#161014" stroke="#DE2626" stroke-width="1.5"/>
    <rect x="0" y="0" width="5" height="136" fill="#DE2626"/>
    <text x="16" y="26" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">03 · 10-FIELD SNAPSHOT CHUNK</text>
    <text x="16" y="46" fill="#DE2626" font-size="10" font-family="monospace">&lt;Project&gt;-V&lt;ver&gt;-PKG&lt;pkg&gt;.bejson</text>
    <text x="16" y="70" fill="#D1D5DB" font-size="10" font-family="monospace">• File_Content (UTF-8) / Base64</text>
    <text x="16" y="90" fill="#D1D5DB" font-size="10" font-family="monospace">• Streaming 64KB SHA-256 Hash</text>
    <text x="16" y="110" fill="#D1D5DB" font-size="10" font-family="monospace">• Is_Empty_Dir &amp; Modified_Time</text>
  </g>

  <!-- Section Banner: 4-Stage Atomic Scoop Gate -->
  <rect x="44" y="252" width="872" height="26" fill="#14141E" stroke="#262636" stroke-width="1"/>
  <text x="480" y="269" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700" text-anchor="middle" letter-spacing="1">ZERO-DATA-LOSS ATOMIC SCOOP VERIFICATION GATE (--scoop)</text>

  {"".join(stage_boxes)}

  <!-- Connectors between Scoop Stages -->
  <line x1="248" y1="361" x2="266" y2="361" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}"/>
  <line x1="470" y1="361" x2="488" y2="361" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}"/>
  <line x1="692" y1="361" x2="710" y2="361" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}"/>

  <!-- Bottom Telemetry Strip -->
  <rect x="24" y="458" width="912" height="58" fill="#0E0E14" stroke="#1E1E2A" stroke-width="1" />
  <circle cx="48" cy="487" r="5" fill="#DE2626" />
  <text x="64" y="491" fill="#FFFFFF" font-size="11.5" font-family="monospace" font-weight="700">ACTIVE GATE: {scoop_stages[active_stage][0]}</text>
  <text x="515" y="491" fill="#888896" font-size="10.5" font-family="monospace">│ SURFACES: CLI · 57-COL TUI · FLASK WEB</text>
</svg>"""


def build_reminder_tool_frame_svg(frame_idx: int, total_frames: int) -> str:
    """
    Generate frame SVG for Animation 3: Reminder_Tool (v1.0.0)
    BEJSON 104a Active Queue, Termux ~/.bashrc Launch Banner, & Pop-and-Archive Completion.
    Duration: 42 frames @ 12 FPS = 3.50 seconds.
    """
    progress = frame_idx / float(total_frames)
    active_phase = int(progress * 3) % 3
    pulse_dash = (frame_idx * 4) % 28

    phase_labels = [
        "PHASE 1 · ADD REMINDER (remind add \"<text>\" -p urgent -> reminders.104a.bejson)",
        "PHASE 2 · TERMUX ~/.BASHRC LAUNCH HOOK (reminder_tool.py --print-termux)",
        "PHASE 3 · COMPLETE & POP (remind done 1 -> Pops Active & Archives to completed_reminders.104a.bejson)",
    ]

    b0 = "#DE2626" if active_phase == 0 else "#2A2A38"
    b1 = "#DE2626" if active_phase == 1 else "#2A2A38"
    b2 = "#DE2626" if active_phase == 2 else "#2A2A38"

    row1_opacity = "1.0" if active_phase in (0, 1) else "0.28"
    archive_highlight = "#DE2626" if active_phase == 2 else "#262636"

    return f"""<svg width="960" height="540" viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg">
  <rect width="960" height="540" fill="#0A0A0C" />
  <rect x="24" y="24" width="912" height="492" fill="none" stroke="#1E1E2A" stroke-width="1.5" />
  <rect x="24" y="24" width="912" height="62" fill="#0E0E14" stroke="#1E1E2A" stroke-width="1" />
  <rect x="24" y="24" width="6" height="62" fill="#DE2626" />
  <text x="46" y="52" fill="#FFFFFF" font-size="17" font-family="system-ui, sans-serif" font-weight="800" letter-spacing="0.8">REMINDER_TOOL (v1.0.0) // BEJSON 104a LIFECYCLE &amp; TERMUX ~/.BASHRC HOOK</text>
  <text x="46" y="72" fill="#888896" font-size="10.5" font-family="monospace" letter-spacing="1.5">AI &amp; CLI ADDITION · 57-COL TERMUX STARTUP BANNER · POP-ON-COMPLETE ARCHIVAL</text>

  <!-- Left Panel: Termux 57-Column Interactive Launch Terminal -->
  <g transform="translate(42, 104)">
    <rect x="0" y="0" width="436" height="336" fill="#0C0C10" stroke="{b1}" stroke-width="1.8"/>
    <rect x="0" y="0" width="436" height="32" fill="#161620" stroke="{b1}" stroke-width="1"/>
    <circle cx="16" cy="16" r="4.5" fill="#DE2626"/>
    <text x="30" y="20" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">TERMUX INTERACTIVE LAUNCH (~/.bashrc)</text>

    <text x="14" y="54" fill="#9CA3AF" font-size="10" font-family="monospace">$ python3 reminder_tool.py --print-termux</text>
    <text x="14" y="74" fill="#FFFFFF" font-size="10" font-family="monospace">=========================================================</text>
    <text x="14" y="92" fill="#DE2626" font-size="10.5" font-family="monospace" font-weight="700"> [REMINDERS] ACTIVE PENDING TASKS (2)</text>
    <text x="14" y="108" fill="#888896" font-size="10" font-family="monospace">---------------------------------------------------------</text>

    <g opacity="{row1_opacity}">
      <text x="14" y="128" fill="#DE2626" font-size="10.5" font-family="monospace" font-weight="700">  [1] [URGENT] Audit MFDB v1.40 cascade locks</text>
      <text x="14" y="144" fill="#888896" font-size="9.5" font-family="monospace">      Added: 2026-11-09 | ID: rem_20261109_112004</text>
    </g>

    <text x="14" y="168" fill="#FFFFFF" font-size="10.5" font-family="monospace" font-weight="700">  [2] [HIGH]   Publish BEJSON_CMS static bundle</text>
    <text x="14" y="184" fill="#888896" font-size="9.5" font-family="monospace">      Added: 2026-11-09 | ID: rem_20261109_112519</text>

    <text x="14" y="204" fill="#888896" font-size="10" font-family="monospace">---------------------------------------------------------</text>
    <text x="14" y="220" fill="#D1D5DB" font-size="10" font-family="monospace">  Complete task via: remind done &lt;#&gt;</text>
    <text x="14" y="236" fill="#FFFFFF" font-size="10" font-family="monospace">=========================================================</text>

    <rect x="14" y="252" width="408" height="68" fill="#141016" stroke="{b0}" stroke-width="1.2"/>
    <text x="24" y="272" fill="#DE2626" font-size="10" font-family="monospace" font-weight="700">AGENT &amp; CLI COMMAND DISPATCH:</text>
    <text x="24" y="290" fill="#FFFFFF" font-size="10" font-family="monospace">$ remind add "Audit MFDB v1.40 cascade locks" -p urgent</text>
    <text x="24" y="308" fill="#FFFFFF" font-size="10" font-family="monospace">$ remind done 1   # Pops from active -&gt; Archives</text>
  </g>

  <!-- Animated Connector Left -> Right -->
  <line x1="478" y1="210" x2="518" y2="210" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="8 6" stroke-dashoffset="-{pulse_dash}"/>
  <polygon points="514,205 522,210 514,215" fill="#DE2626"/>

  <!-- Right Top: Active Registry (data/reminders.104a.bejson) -->
  <g transform="translate(518, 104)">
    <rect x="0" y="0" width="400" height="154" fill="#101018" stroke="{b0}" stroke-width="1.8"/>
    <rect x="0" y="0" width="6" height="154" fill="#DE2626"/>
    <text x="18" y="26" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">01 · ACTIVE QUEUE (reminders.104a.bejson)</text>
    <text x="18" y="46" fill="#DE2626" font-size="10" font-family="monospace">7 Fields · O(1) compile_bejson_field_map()</text>
    <text x="18" y="70" fill="#D1D5DB" font-size="10" font-family="monospace">• Fields: reminder_id, reminder_text, priority,</text>
    <text x="18" y="86" fill="#D1D5DB" font-size="10" font-family="monospace">          status, creation_date, due_date, tags</text>
    <text x="18" y="110" fill="#FFFFFF" font-size="10" font-family="monospace">• Atomic Write: .tmp swap -&gt; reminders.104a.bejson</text>
    <text x="18" y="130" fill="#9CA3AF" font-size="9.5" font-family="monospace">• Zero terminal output when active Values == []</text>
  </g>

  <!-- Animated Pop-and-Archive Connector Top -> Bottom -->
  <line x1="718" y1="258" x2="718" y2="286" stroke="#DE2626" stroke-width="2.5" stroke-dasharray="6 4" stroke-dashoffset="-{pulse_dash}"/>
  <polygon points="713,282 718,290 723,282" fill="#DE2626"/>

  <!-- Right Bottom: Completed Registry (data/completed_reminders.104a.bejson) -->
  <g transform="translate(518, 286)">
    <rect x="0" y="0" width="400" height="154" fill="#141014" stroke="{b2}" stroke-width="1.8"/>
    <rect x="0" y="0" width="6" height="154" fill="{archive_highlight}"/>
    <text x="18" y="26" fill="#FFFFFF" font-size="12" font-family="monospace" font-weight="800">02 · ARCHIVE (completed_reminders.104a.bejson)</text>
    <text x="18" y="46" fill="#DE2626" font-size="10" font-family="monospace">Pop-on-Complete (rows.pop -&gt; archive_row)</text>
    <text x="18" y="70" fill="#D1D5DB" font-size="10" font-family="monospace">• Removes completed item from active queue</text>
    <text x="18" y="88" fill="#D1D5DB" font-size="10" font-family="monospace">• Stamps UTC completion_date in archive table</text>
    <text x="18" y="108" fill="#D1D5DB" font-size="10" font-family="monospace">• Queryable via: remind completed | remind --json</text>
    <text x="18" y="130" fill="#FFFFFF" font-size="10" font-family="monospace">[✓] reminder completed &amp; removed from launch banner</text>
  </g>

  <!-- Bottom Telemetry Strip -->
  <rect x="24" y="458" width="912" height="58" fill="#0E0E14" stroke="#1E1E2A" stroke-width="1" />
  <circle cx="48" cy="487" r="5" fill="#DE2626" />
  <text x="64" y="491" fill="#FFFFFF" font-size="11" font-family="monospace" font-weight="700">{phase_labels[active_phase]}</text>
</svg>"""


def render_svg_sequence_to_gif(
    name_slug: str,
    frame_builder,
    total_frames: int = 42,
    fps: int = 12,
) -> Path:
    """Render 42 SVG frames (3.5 seconds @ 12 FPS) via Playwright and encode to optimized GIF via FFmpeg."""
    frame_dir = TEMP_FRAMES_ROOT / name_slug
    if frame_dir.exists():
        shutil.rmtree(frame_dir)
    frame_dir.mkdir(parents=True, exist_ok=True)

    # Save canonical static SVG (frame 0) to assets/
    svg_path = ASSETS_DIR / f"{name_slug}.svg"
    svg_path.write_text(frame_builder(0, total_frames), encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            executable_path="/data/data/com.termux/files/usr/lib/chromium/chrome",
            args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
        )
        page = browser.new_page(viewport={"width": 960, "height": 540})
        for idx in range(total_frames):
            svg_markup = frame_builder(idx, total_frames)
            html_doc = (
                "<!DOCTYPE html><html><head><style>"
                "* { margin: 0; padding: 0; background: #0A0A0C; }"
                "</style></head><body>"
                f"{svg_markup}</body></html>"
            )
            page.set_content(html_doc, wait_until="load")
            frame_png = frame_dir / f"frame_{idx:04d}.png"
            page.screenshot(path=str(frame_png), clip={"x": 0, "y": 0, "width": 960, "height": 540})
        browser.close()

    gif_path = ASSETS_DIR / f"{name_slug}.gif"
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
    duration_sec = total_frames / float(fps)
    size_kb = gif_path.stat().st_size // 1024
    logger.info("Compiled %s (%d KB, %d frames @ %d FPS = %.2fs)", gif_path.name, size_kb, total_frames, fps, duration_sec)
    return gif_path


def main() -> None:
    copy_slide_deck_assets()
    render_svg_sequence_to_gif("newagent_context_bubble_anim", build_newagent_frame_svg, total_frames=42, fps=12)
    render_svg_sequence_to_gif("project_chunker_scoop_anim", build_project_chunker_frame_svg, total_frames=42, fps=12)
    render_svg_sequence_to_gif("reminder_tool_termux_anim", build_reminder_tool_frame_svg, total_frames=42, fps=12)
    if TEMP_FRAMES_ROOT.exists():
        shutil.rmtree(TEMP_FRAMES_ROOT, ignore_errors=True)
    logger.info("All 15 slides and 3 contextual 3.5-second animations successfully generated.")


if __name__ == "__main__":
    main()
