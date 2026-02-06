# Project Context: Rees Cricket Website

## Project Overview
Rees Cricket is a static website for a Melbourne-based cricket bat repair and refurbishment business. The site showcases services (handle replacement, re-gripping, etc.), displays a gallery of work, includes customer testimonials, and provides contact information.

## Tech Stack
- **Core:** HTML5, CSS3
- **Scripting:** Minimal/None (Standard JS if needed)
- **Styling:**
    - Vanilla CSS with CSS Variables for theming.
    - Flexbox and Grid layouts.
    - Responsive design using media queries (implied).
- **Hosting:** Static hosting (likely).

## Project Structure
- `index.html`: The single-page application structure containing all sections (Hero, Services, About, Process, Gallery, Testimonials).
- `images/`: Directory storing assets (inferred from `list_dir`).
- `context.md`: This file, serving as AI context.

## Design System
### Color Palette
- **Backgrounds:**
    - Primary: `#0a0a0a` (Very dark grey/black)
    - Secondary: `#111111`
    - Card: `rgba(20, 20, 20, 0.8)`
- **Accents:**
    - Red (Primary Accent): `#c41e3a`
    - Light Red: `#e63950`
    - Dark Red: `#9a1830`
    - Gold: `#d4a959`
- **Text:**
    - Primary: `#ffffff`
    - Secondary: `#b0b0b0`
    - Muted: `#666666`
- **Borders:**
    - Default: `rgba(255, 255, 255, 0.08)`
    - Accent: `rgba(196, 30, 58, 0.3)`

### Typography
- **Headings:** 'Playfair Display', serif (Weights: 400, 600)
- **Body:** 'Inter', sans-serif (Weights: 300, 400, 500, 600, 700)

### UI Components
- **Buttons:**
    - Primary: Accent background, white text, hover lift & shadow.
    - Secondary: Transparent background, border, hover accent color.
- **Cards:** Dark semi-transparent backgrounds with subtle borders and hover effects (transform translateY).
- **Navigation:** Fixed, glassmorphism effect (`backdrop-filter: blur`).
