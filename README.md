<div align="center">
  <img src="assets/boehnenelton_cubic_engine.gif" alt="boehnenelton BEJSON Schema-Driven Cubic Vector Engine" width="100%" />
</div>

# Elton Boehnen

> Autonomous Systems Architecture, Deterministic Data Formats & Databaseless Computing Environments.

[![Architecture](https://img.shields.io/badge/Architecture-BEJSON%20104a%20%2F%20105-DE2626.svg)](#bejson-schema-driven-graphics-engine)
[![Persistence](https://img.shields.io/badge/Persistence-MFDB%20Flat--File-black.svg)](#multi-file-database-mfdb)
[![Discipline](https://img.shields.io/badge/CLI%20Discipline-57--Column%20Portrait-black.svg)](#57-column-portrait-cli-discipline)
[![Website](https://img.shields.io/badge/Portal-boehnenelton2024.pages.dev-blue.svg)](https://boehnenelton2024.pages.dev)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#license--attribution)

---

## Table of Contents

- [Overview](#overview)
- [BEJSON Schema-Driven Graphics Engine](#bejson-schema-driven-graphics-engine)
  - [1. The Tabular Schema Specification](#1-the-tabular-schema-specification)
  - [2. O(1) Field Map Cache Resolution](#2-o1-field-map-cache-resolution)
  - [3. Deterministic Vector Compilation Pipeline](#3-deterministic-vector-compilation-pipeline)
- [Core Architectural Pillars](#core-architectural-pillars)
  - [BEJSON 104a & 105 Format Matrix](#bejson-104a--105-format-matrix)
  - [Multi-File Database (MFDB)](#multi-file-database-mfdb)
  - [57-Column Portrait CLI Discipline](#57-column-portrait-cli-discipline)
  - [Tri-Color Visual Palette](#tri-color-visual-palette)
- [Flagship Ecosystem Platforms](#flagship-ecosystem-platforms)
  - [1. System Management Tool Suite](#1-system-management-tool-suite-management_tool)
  - [2. Databaseless Content Management System](#2-databaseless-content-management-system-management_cms)
  - [3. Autonomous Agent Platform](#3-autonomous-agent-platform-newagent)
  - [4. Project Portfolio Governor](#4-project-portfolio-governor-project_manager)
  - [5. Standalone Launch Reminders](#5-standalone-launch-reminders-reminder_tool)
  - [6. Standard Development Libraries](#6-standard-development-libraries-libraries_104--libraries_105)
- [Cubic Architecture Visual Anchors](#cubic-architecture-visual-anchors)
- [Technical Specifications & Storage Standards](#technical-specifications--storage-standards)
- [Author & Verification](#author--verification)

---

## Overview

This repository serves as the central architectural hub and profile landing portal for **Elton Boehnen** (`boehnenelton`). It documents the design philosophy, data formats, execution engines, and software platforms developed across the BEJSON and autonomous systems ecosystem.

The ecosystem eliminates external database server overhead (such as PostgreSQL, MySQL, or heavy ORMs) in favor of portable, deterministic, flat-file structures. By combining high-speed structured JSON ledgers with strict schema boundaries, zero-dependency Python runtime libraries, and bounded autonomous execution agents, the system delivers complete local-first durability across Linux and Android Termux ARM64 environments.

---

## BEJSON Schema-Driven Graphics Engine

In the BEJSON ecosystem, visual assets, diagrams, and branding anchors are not arbitrary drawings; they are **deterministic data artifacts** compiled directly from structured tabular schemas.

The animated visual anchor above demonstrates this principle in real time: every vertex of the 3D isometric cube, the floating top diamond cap, the focal red divider, and the coordinate boundaries are stored as structured tabular rows in [`assets/cubic_schema.104a.bejson`](assets/cubic_schema.104a.bejson).

### 1. The Tabular Schema Specification

```json
{
  "Header": {
    "Table_Name": "cubic_graphic_primitives",
    "Format": "104a",
    "Record_Count": 7,
    "Author": "Elton Boehnen",
    "Description": "BEJSON 104a tabular vector graphic schema defining the canonical 3D isometric open branding cube and stage coordinates."
  },
  "Fields": [
    "element_id",
    "primitive_type",
    "points_or_coords",
    "fill_color",
    "stroke_color",
    "stroke_width",
    "animation_mode",
    "semantic_label"
  ],
  "Data": [
    ["elem_01_substrate",   "rect",    "0,0,1280,640",              "#0A0A0C", "none",    0.0, "static",         "Canvas Obsidian Substrate"],
    ["elem_02_frame",       "rect",    "48,48,1184,544",            "none",    "#1A1A22", 1.5, "static",         "Structural Inset Boundary Frame"],
    ["elem_03_notch",       "rect",    "48,270,4,100",              "#DE2626", "none",    0.0, "static",         "Left Boundary Accent Notch"],
    ["elem_04_divider",     "line",    "364,256,364,404",           "none",    "#DE2626", 3.0, "pulse_alpha",    "Primary Red Focal Divider"],
    ["elem_05_floating_cap","polygon", "0,-48,56,-18,0,12,-56,-18", "#FFFFFF", "#FFFFFF", 1.5, "harmonic_float", "104a Hovering Diamond Cap"],
    ["elem_06_left_facet",  "polygon", "-56,-18,0,12,0,72,-56,42",  "#181820", "#FFFFFF", 1.5, "static",         "Left Obsidian Shading Facet"],
    ["elem_07_right_facet", "polygon", "0,12,56,-18,56,42,0,72",   "#DE2626", "#FFFFFF", 1.5, "static",         "Right Signature Red Facet"]
  ]
}
```

### 2. O(1) Field Map Cache Resolution

To prevent fragile positional indexing or repetitive dictionary searches over millions of frames, the engine compiles a constant-time field map cache on ingestion:

```python
# Mandatory O(1) Field Map Cache
fields = bejson_doc["Fields"]
field_map = {name: idx for idx, name in enumerate(fields)}

# Instantaneous column addressability with zero string allocations in render loops
col_type   = field_map["primitive_type"]
col_coords = field_map["points_or_coords"]
col_fill   = field_map["fill_color"]
col_stroke = field_map["stroke_color"]
col_width  = field_map["stroke_width"]
col_anim   = field_map["animation_mode"]
```

### 3. Deterministic Vector Compilation Pipeline

The graphics engine parses rows through the field map cache, applies harmonic time offsets for elements with `harmonic_float` or `pulse_alpha`, and emits standards-compliant SVG:

```python
def compile_bejson_to_svg(bejson_doc: dict, time_sec: float = 0.0) -> str:
    """Compiles BEJSON 104a tabular graphic rows into deterministic SVG markup."""
    field_map = {name: idx for idx, name in enumerate(bejson_doc["Fields"])}
    rendered_elements = []

    for row in bejson_doc["Data"]:
        p_type = row[field_map["primitive_type"]]
        coords = row[field_map["points_or_coords"]]
        fill   = row[field_map["fill_color"]]
        stroke = row[field_map["stroke_color"]]
        width  = row[field_map["stroke_width"]]
        anim   = row[field_map["animation_mode"]]

        if anim == "harmonic_float":
            # 104a dynamic floating diamond cap hovering above cube body
            y_offset = -22.0 * math.sin(time_sec * 2.0 * math.pi)
            rendered_elements.append(
                f'<g transform="translate(0, {y_offset:.2f})">'
                f'<polygon points="{coords}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
                f'</g>'
            )
        elif p_type == "polygon":
            rendered_elements.append(
                f'<polygon points="{coords}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
            )
        elif p_type == "rect":
            x, y, w, h = coords.split(",")
            rendered_elements.append(
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
            )
        elif p_type == "line":
            x1, y1, x2, y2 = coords.split(",")
            rendered_elements.append(
                f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{width}"/>'
            )

    return f'<svg width="1280" height="640">{"".join(rendered_elements)}</svg>'
```

---

## Core Architectural Pillars

### BEJSON 104a & 105 Format Matrix

The foundational substrate of all ecosystem storage is **BEJSON** (Binary/Bounded Encapsulated JSON), structured across two canonical eras:

```
+-------------------------------------------------------------------------+
| FOUNDATIONAL ERA (Format 104 / 104a / 104db)                           |
| - Header metadata + 1D 'Fields' schema array + 2D tabular 'Data' rows   |
| - O(1) Field Map Cache for zero-allocation column resolution            |
| - Format 104: Core single-table flat file                               |
| - Format 104a: Dynamic schema registry integration                      |
| - Format 104db: Relational multi-table entity bindings                  |
+-------------------------------------------------------------------------+
| INTEGRITY ERA (Format 105 / 105a / 105db)                               |
| - UUIDv4 primary identity minting per record at column 0                |
| - Cryptographic SHA-256 record verification digests                     |
| - Cross-entity relational cascades and foreign-key integrity             |
+-------------------------------------------------------------------------+
```

### Multi-File Database (MFDB)

MFDB federates multiple independent tabular entity tables into a cohesive relational database without a background daemon or network socket:
- **Manifest-Driven**: Master manifest documents (`104a.mfdb.bejson`) register entities, schemas, primary keys, and relative table paths.
- **Atomic Operations**: In-place mutations write through temp files and atomic rename guards to eliminate file corruption.
- **Portability**: The entire database lives directly on disk as a folder of plain-text JSON files, fully readable by standard tools and zero-cost to backup, transfer, or version-control.

### 57-Column Portrait CLI Discipline

Every command-line interface in the ecosystem adheres to a strict 57-column width ceiling. Engineered specifically for mobile touchscreens, terminal emulators (Termux), and vertical split panes:
- **Zero Horizontal Truncation**: Menus, logs, tables, and metric reports render without wrapping or clipping on standard mobile portrait displays.
- **Structured ANSI Styling**: Headers and labels in `#DE2626`, success states in clean lowercase white, failures in bold red uppercase, and neutral metrics in muted gray.

### Tri-Color Visual Palette

All visual assets, presentation stages, web interfaces, and terminal outputs enforce strict high-contrast color boundaries:
- **Pitch Black (`#0A0A0C` / `#000000`)**: Deep canvas substrate providing high contrast.
- **Pure White (`#FFFFFF`)**: High-legibility text and structural boundaries.
- **Signature Vivid Red (`#DE2626`)**: Directional dividers, focal anchors, active highlights, and primary brand accents.
- **Zero-Curvature Geometry**: Sharp non-rounded borders (`rx="0"`, `border-radius: 0px`) conveying mechanical precision and structural integrity.

---

## Flagship Ecosystem Platforms

```
                          +-------------------------+
                          |      boehnenelton       |
                          |  Ecosystem Master Hub   |
                          +------------+------------+
                                       |
       +------------------+------------+------------+------------------+
       |                  |                         |                  |
+------v-------+   +------v-------+          +------v-------+   +------v-------+
| Management   |   | Management   |          |   NewAgent   |   |   Project    |
|     Tool     |   |     CMS      |          |  Autonomous  |   |   Manager    |
| Master Router|   | Databaseless |          | Orchestration|   |  Portfolio   |
+--------------+   +--------------+          +--------------+   +--------------+
       |                  |                         |                  |
+------v-------+   +------v-------+          +------v-------+   +------v-------+
|   Reminder   |   | BEJSON 104/5 |          |  JobMaker    |   | 57-Col TUI   |
|     Tool     |   |  Libraries   |          | State Engine |   |  Dashboards  |
+--------------+   +--------------+          +--------------+   +--------------+
```

### 1. System Management Tool Suite (`Management_Tool`)
- **Repository**: [`Management_Tool`](https://github.com/boehnenelton/Management_Tool)
- **Role**: Master operational router and command center across local development environments.
- **Subsystems**:
  - **Structured Logging (`MD2HTML`)**: Parses and transforms daily markdown operational notes into responsive, self-contained HTML reports with syntax highlighting.
  - **Research Reports Indexer**: Indexes, categorizes, and audits technical architectural research documents across persistent storage.
  - **Categorized Notes Hub**: MFDB-backed note-taking engine with category routing, full-text search, and static site export pipelines.
  - **Stateful Job Chamber**: Sequential task processor running scheduled and urgent jobs against registered maintenance schedules.
  - **Launch Reminders**: Embedded launch checklist verifying active developer tasks on session initialization.

### 2. Databaseless Content Management System (`Management_CMS`)
- **Repository**: [`Management_CMS`](https://github.com/boehnenelton/Management_CMS)
- **Role**: Self-hosted administrative publishing console and static site compiler built on BEJSON 104a and MFDB.
- **Key Capabilities**:
  - Serves an administrative browser console for managing Pages, Posts, Media, Categories, and Navigation menus.
  - Integrates an offline static site build engine compiling dynamic BEJSON tables into static HTML, CSS, RSS/Atom feeds, and JSON endpoints.
  - Built-in media pipeline providing automatic WebP conversion and metadata registration with zero external DB dependencies.

### 3. Autonomous Agent Platform (`NewAgent`)
- **Repository**: [`NewAgent`](https://github.com/boehnenelton/NewAgent)
- **Role**: Autonomous task decomposition, agent orchestration, and execution daemon.
- **Key Capabilities**:
  - **`JobMaker.py`**: State machine converting high-level goals into phased sequential milestone jobs with atomic rollback locks.
  - **`agent.py` & `cliagent.py`**: Headless CLI runners executing autonomous shell, filesystem, and code refactoring tasks.
  - **`webagent.py`**: Web-based monitoring console displaying live job progression, system telemetry, and configuration state.

### 4. Project Portfolio Governor (`Project_Manager`)
- **Repository**: [`Project_Manager-V180`](https://github.com/boehnenelton/Project_Manager-V180)
- **Role**: Central project registry, build manager, and directory topology governor.
- **Key Capabilities**:
  - Tracks `bejson_project.json` manifests across active development directories.
  - Manages package version increments, release ZIP archiving, and dependency validation.
  - Provides interactive 57-column terminal menus for repository discovery and status reporting.

### 5. Standalone Launch Reminders (`Reminder_Tool`)
- **Repository**: [`Reminder_Tool`](https://github.com/boehnenelton/Reminder_Tool)
- **Role**: Lightweight, zero-friction task and launch reminder system designed for mobile terminal environments.
- **Key Capabilities**:
  - Priority levels (`urgent`, `high`, `normal`), due date tracking, and automated completion archiving.
  - Strict 57-column ANSI formatted display with color-coded badges and sub-10ms startup latency.

### 6. Standard Development Libraries (`libraries_104` & `libraries_105`)
- **Role**: Foundational Python standard libraries powering all BEJSON data access, validation, and mutation.
- **Components**:
  - `bejson_core`: High-speed row manipulation and field map caching.
  - `bejson_validator`: Conformance verification against 104 and 105 schema invariants.
  - `mfdb_core`: Relational multi-file joins, foreign key cascade enforcement, and manifest locking.
  - `bejson_crypto`: AES-GCM encryption and SHA-256 record ledger digest generation.

---

## Cubic Architecture Visual Anchors

The visual identity of the ecosystem is governed by the **3D Isometric Cube** visual taxonomy:

| Architecture Style | Era / Paradigm | Visual Signature | Purpose |
|---|---|---|---|
| **Format 104** | Foundational Standard | Single Open Isometric Cube | Base single-table schema representation |
| **Format 104a** | Dynamic Schema Matrix | Hovering Diamond Cap (Harmonic Float) | Schema registry integration & animated vector engines |
| **Format 104db** | Relational Multi-Table | Stacked Interlocking Dual Cubes | MFDB multi-file databases and foreign key cascades |
| **Architectural Light** | High-Contrast Contrast | White Substrate & Sharp Borders | Editorial documentation, light themes, and print |

<div align="center">

| Canonical 104 | Format 104a (Dynamic) | Format 104db (MFDB) | Light Minimal |
|:---:|:---:|:---:|:---:|
| <img src="assets/boehnenelton_banner_canonical.png" width="220" /> | <img src="assets/boehnenelton_banner_floating_cube.png" width="220" /> | <img src="assets/boehnenelton_banner_stacked_pillar.png" width="220" /> | <img src="assets/boehnenelton_banner_light_minimal.png" width="220" /> |

</div>

---

## Technical Specifications & Storage Standards

```
Standard Parameter         Specification
-------------------------  -------------------------------------------------------------
Substrate Operating System Linux (x86_64 / ARM64), Android Termux (Bionic libc)
Core Programming Language  Python 3.10+ (Standard Library Centric)
Data Interchange Standard  BEJSON 104a (Tabular Rows) & Format 105 (UUIDv4 Hash Chains)
Database Paradigms         MFDB (Multi-File Flat-File Databases, Zero-SQL)
Terminal Geometry          57-Column Mobile Portrait Ceiling
Web User Interface         Tri-Color Palette (#0A0A0C, #FFFFFF, #DE2626), Zero Curvature
Build Pipelines            Headless Chromium Automation, Native Pillow WebP/GIF Encoding
```

---

## Author & Verification

- **Author**: Elton Boehnen
- **Email**: [boehnenelton2024@gmail.com](mailto:boehnenelton2024@gmail.com)
- **Web Portal**: [boehnenelton2024.pages.dev](https://boehnenelton2024.pages.dev)
- **GitHub**: [github.com/boehnenelton](https://github.com/boehnenelton)

---

### License

Distributed under the MIT License. Copyright (c) Elton Boehnen. All rights reserved.
