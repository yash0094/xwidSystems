---
name: Aether Neomorphic
colors:
  surface: '#f7fafe'
  surface-dim: '#d7dade'
  surface-bright: '#f7fafe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f8'
  surface-container: '#ebeef2'
  surface-container-high: '#e5e8ec'
  surface-container-highest: '#e0e3e7'
  on-surface: '#181c1f'
  on-surface-variant: '#45474b'
  inverse-surface: '#2d3134'
  inverse-on-surface: '#eef1f5'
  outline: '#76777b'
  outline-variant: '#c6c6cb'
  surface-tint: '#5d5e63'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1a1c20'
  on-primary-container: '#828489'
  inverse-primary: '#c6c6cc'
  secondary: '#006b5f'
  on-secondary: '#ffffff'
  secondary-container: '#74f8e3'
  on-secondary-container: '#007165'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#00201d'
  on-tertiary-container: '#668b85'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e8'
  primary-fixed-dim: '#c6c6cc'
  on-primary-fixed: '#1a1c20'
  on-primary-fixed-variant: '#45474b'
  secondary-fixed: '#74f8e3'
  secondary-fixed-dim: '#53dbc7'
  on-secondary-fixed: '#00201c'
  on-secondary-fixed-variant: '#005047'
  tertiary-fixed: '#c3eae3'
  tertiary-fixed-dim: '#a8cec7'
  on-tertiary-fixed: '#00201d'
  on-tertiary-fixed-variant: '#294d48'
  background: '#f7fafe'
  on-background: '#181c1f'
  surface-variant: '#e0e3e7'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 2.5rem
    fontWeight: '700'
    lineHeight: 3rem
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.875rem
    fontWeight: '600'
    lineHeight: 2.375rem
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.375rem
    fontWeight: '600'
    lineHeight: 1.875rem
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '600'
    lineHeight: 1.625rem
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1rem
    fontWeight: '500'
    lineHeight: 1.5rem
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.375rem
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.75rem
    fontWeight: '400'
    lineHeight: 1.125rem
  label-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '600'
    lineHeight: 1.25rem
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: 1rem
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.6875rem
    fontWeight: '500'
    lineHeight: 0.875rem
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  gutter: 1.5rem
  margin: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.25rem
---

## Brand & Style

This design system expresses a forward-thinking, calm, and hyper-tactile aesthetic merging soft neumorphism with frosted glassmorphism and clean Scandinavian minimalism. Crafted for next-generation security dashboards, biometric authentication suites, and executive analytics consoles, it creates an environment of tranquil precision.

The emotional signature is quiet confidence: eliminating visual noise and sharp artificial contrast in favor of extruded surfaces, soft light-play, subtle concave wells, and ambient pastel mint tones. Pill-shaped geometry, translucent overlay panels, and obsidian control capsules ground the interface, providing high legibility and tangible delight.

## Colors

The palette revolves around a calm, cool-tinted daylight base `#EEF1F5` (and soft canvas base `#ECEFF3`), avoiding pure whites or cold harsh greys. Visual weight and primary actions are articulated through deep obsidian `#16181C`, delivering punchy tactile contrast against the soft environment. 

### Palette Application
- **Primary (`#16181C`):** Used for focal buttons, selected states, bold typography headers, and active state pill markers.
- **Secondary (`#36C5B2`):** Vibrant bio-mint used for dynamic state indicators, verified badges, active switches, and data sparklines.
- **Tertiary (`#C4EBE4` / `#A8E1D9`):** Soft frosted mint washes for hero card backdrops, interactive category filters, and pill fills.
- **Neutral & Canvas Surfaces:**
  - Background Canvas: `#ECEFF3` to `#F0F3F7`
  - Elevated Container White: `#FFFFFF` with 80%–95% alpha frosted glass treatment
  - Inset Well / Track Fill: `#E4E8EE`
  - Subtle Border Strokes: `#FFFFFF` (highlight edge) and `rgba(22, 24, 28, 0.04)` (shadow edge)
  - Text Muted: `#7A828F`

## Typography

The typography is powered exclusively by Plus Jakarta Sans, chosen for its humanist geometric curves, open counters, and modern digital poise. Numbers receive tabular sizing to ensure data visualizers and counters align cleanly.

- **Display Metrics & Verification Numbers:** Rendered in bold or semi-bold weights with tight letter tracking (`-0.02em`) to command attention without visual noise.
- **Section Titles & Body:** Medium and regular weights ensure effortless readability across soft-lit surfaces.
- **Labels & Micro-Badges:** Small uppercase or title case tokens are spaced comfortably (`0.02em`) to maintain legibility when enclosed within pill badges and interactive capsules.

## Layout & Spacing

The layout model is architected around floating soft modules contained within an expansive tablet-style shell.

- **Modular Framing:** The master dashboard sits inside a master container flanked by an integrated slim navigation rail (80px) on the left, a central command core, and an auxiliary context drawer (320px) on the right.
- **Grid Hierarchy:** Central views deploy a 12-column dynamic fluid grid with `1.5rem` (24px) gutters. Complex analytic widgets span 8 columns, while telemetry and micro-cards span 4 or 6 columns.
- **Rhythm & Padding:** Component internal paddings scale from `0.75rem` (12px) inside chips and micro-inputs to `1.5rem`–`2rem` (24px–32px) inside master cards, preserving an airy, uncluttered breathing room.
- **Breakpoints:**
  - Desktop (>1280px): Three-panel open layout (Left rail + Main + Right utility).
  - Tablet (768px - 1279px): Two-panel layout; right utility transforms into an overlay sheet or bottom-docked tray.
  - Mobile (<767px): Single-column reflow; persistent bottom navigation pill replaces the vertical rail.

## Elevation & Depth

Visual hierarchy is achieved through a dual-light neumorphic technique combined with semi-translucent backdrop blurs.

### Neumorphic Light Source
Lighting originates from the top-left (-45°). Elements project soft dual-shadow treatments:
- **Raised Surfaces (Cards & Modules):** 
  `box-shadow: -8px -8px 20px rgba(255, 255, 255, 0.9), 10px 14px 28px rgba(166, 175, 195, 0.25);`
- **Soft Inset Wells (Search bars, inactive tracks, bar cavities):** 
  `box-shadow: inset 3px 3px 6px rgba(166, 175, 195, 0.3), inset -3px -3px 6px rgba(255, 255, 255, 0.85);`
- **Floating Obsidian Pills (High-contrast active badges & action buttons):** 
  `box-shadow: 0 10px 24px rgba(22, 24, 28, 0.24), 0 2px 6px rgba(22, 24, 28, 0.12);`
- **Glassmorphic Hero Overlays:**
  Cards rendered in mint or white tints feature `backdrop-filter: blur(16px)` with a delicate outer boundary stroke `1px solid rgba(255, 255, 255, 0.65)`.

## Shapes

The design system embraces high roundedness: pill geometries, rounded rectangles, and organic cylinders.

- **Outer Enclosing Frames:** Softened with a radius of `32px` to evoke physical hardware ergonomics.
- **Dashboard Modules & Cards:** Radii strictly adhere to `24px` to `28px`.
- **Buttons, Badges, Search Bars & Toggles:** Fully rounded continuous pill shapes (`9999px` border radius).
- **Chart Visualizer Blocks:** Segmented stacked pills with distinct `12px` rounded corners, conveying tactile physical blocks rather than flat vector bars.

## Components

### Buttons & Interactive Pills
- **Primary Dark Button:** Solid `#16181C` pill with crisp white text, accompanied by high-spread dark drop shadows. On hover, slightly translates upward by -1px with softened glow.
- **Secondary Mint Pill:** Pale mint background (`#C4EBE4` or `#A8E1D9`) with dark `#16181C` typography and icons.
- **Ghost/Tertiary Pill:** Pure white with dual neumorphic shadow and subtle `rgba(22, 24, 28, 0.04)` border.

### Filter Chips & Navigation Tabs
- Grouped inside a continuous frosted track.
- Active states pop into a white or soft mint extruded pill with mild elevation; inactive states rest flat with muted `#7A828F` text.

### Search & Form Inputs
- Fully rounded pill input shells featuring sunken inset neumorphic shadows (`inset 2px 2px 5px rgba(166,175,195,0.2)`).
- Search icons on the left, voice or filter micro-pills nested inside the right padding.

### Stacked Bar Visualizers & Charts
- Vertical segmented rounded rectangles representing hourly or daily data.
- Stacked elements alternate between subtle grey `#C9D2DC`, deep obsidian `#16181C`, and mint accents `#36C5B2`, creating a tactile physical pegboard effect.

### Toggles & Status Switches
- Inset pill track in pale grey-blue. The circular knob slides smoothly, morphing into obsidian when enabled, accompanied by a glowing status dot.

### User & Security Profile Badges
- Translucent frosted glass tiles featuring user avatars overlapping in pill groups. Biometric face outlines and facial recognition wireframes are rendered with thin, mint and obsidian vector lines.