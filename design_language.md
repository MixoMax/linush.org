This is a highly stylized, **"Cyberpunk / Technical Minimalist"** design system. It relies heavily on a dark mode aesthetic, monospaced typography for metadata, and high-performance motion graphics.

Here is the design system breakdown to give to your junior developer.

---

### 1. Design Philosophy: "The Navigator's Terminal"
The UI treats the user not just as a reader, but as an operator of a futuristic interface.
*   **Keywords:** Precision, Holographic, Industrial, Sci-Fi, Data-Driven.
*   **Core Concept:** Content floats on top of a "living" 3D deep-sea/network background.

### 2. Color Palette
The scheme is a high-contrast dark mode with a single electric accent color.

| Variable | Hex / Value | Usage |
| :--- | :--- | :--- |
| **Canvas / Bg** | `#050505` | Main page background (Near Black). |
| **Surface** | `#0a0a0a` | Terminal windows, heavy cards. |
| **Glass** | `rgba(255, 255, 255, 0.03)` | Standard card background. **Must have backdrop-filter: blur(10px).** |
| **Primary Text** | `#e0e0e0` | Headings and body copy. |
| **Muted Text** | `#9ca3af` (Tailwind gray-400) | Secondary descriptions, footer text. |
| **Accent (Electric Cyan)** | `#00f3ff` | Active states, hover effects, timeline nodes, key highlights. |
| **Accent Glow** | `rgba(0, 243, 255, 0.05)` | Box shadows and atmospheric glow. |
| **Status Colors** | Green, Yellow, Purple | Used sparingly for "system status" indicators (dots). |

### 3. Typography
The system uses a pairing of a Geometric Sans-serif and a Coding Monospace font.

**Primary Font:** `Space Grotesk`
*   **Usage:** Headlines, large display text, paragraph body.
*   **Weights:** 300 (Light), 400 (Regular), 700 (Bold).
*   **Styling:** Headings are often `uppercase` and `tracking-tighter` (tight letter spacing).

**Secondary Font:** `JetBrains Mono`
*   **Usage:** Navigation links, buttons, dates, tags, "system" data, metadata.
*   **Styling:** Usually `uppercase`, smaller size (`text-xs` or `text-sm`), often paired with colors or borders.

### 4. UI Components & "Atoms"

#### A. The Glass Panel (Standard Card)
Used for work experience and project showcases.
*   **Border:** `1px solid rgba(255, 255, 255, 0.05)`
*   **Background:** Very low opacity white (`3%`) + Blur.
*   **Hover:** Border color changes to transparent Cyan (`#00f3ff` at ~50% opacity).

#### B. The Terminal Box
Used for technical infrastructure/server data.
*   **Background:** Solid dark (`#0a0a0a`).
*   **Border:** Darker gray (`#333`).
*   **Shadow:** Cyan glow (`0 0 20px rgba(0, 243, 255, 0.05)`).
*   **Content:** Exclusively `JetBrains Mono` font inside.

#### C. Buttons & Links
1.  **Nav Links:** Text only, Monospace. `mix-blend-mode: difference` (inverts color based on background).
2.  **Primary Action:** Solid White background, Black text, sharp corners or rounded-full. Hover: Cyan background.
3.  **Secondary Action:** Transparent background, White border. Hover: Cyan text + Cyan border.
4.  **Tags:** Small badges with low-opacity backgrounds (e.g., `bg-cyan-900/30 text-cyan-300`).

#### D. The "Cursor" (Crucial Interaction Detail)
Do not use the default system cursor.
*   **Default State:** A small 20px circle (outline only).
*   **Hover State:** Expands to 50px, becomes solid Cyan, 50% opacity.
*   **CSS Logic:** `pointer-events: none`, `position: fixed`, `mix-blend-mode: difference`.

### 5. Layout Patterns

*   **Grid System:** Uses a standard 12-column grid logic (via Tailwind).
*   **Whitespace:** Extremely generous. Sections are separated by `py-24` (approx 6rem/96px).
*   **Asymmetry:** Project cards alternate (Image Left/Text Right -> Image Right/Text Left).
*   **Timeline:** Vertical line with dots (`absolute` positioning) connected to content blocks.

### 6. Motion & Behavior (GSAP & CSS)

*   **Scroll:** Must use **Lenis** (or similar) for momentum-based smooth scrolling.
*   **Entrance:** Elements do not exist statically. They fade in and slide up (`y: 50px -> 0`) as they enter the viewport (ScrollTrigger).
*   **Images:**
    *   Start **Grayscale**.
    *   On Hover: Full Color + Scale Up (`transform: scale(1.05)`).
*   **Background Layer:**
    *   A Three.js canvas sits at `z-index: -1` and `position: fixed`.
    *   It contains a particle system and a wireframe mesh that rotates slowly and reacts to mouse movement (parallax).

---

### Task List for Junior Developer

If you are assigning this, here is the specific ticket description:

> **Ticket: Implement New Feature Page (Style Match)**
>
> **Objective:** Create a new page that seamlessly integrates with the existing "Linus Horn" portfolio design system.
>
> **Requirements:**
> 1.  **Setup:** Import `Space Grotesk` and `JetBrains Mono`. Install Tailwind CSS.
> 2.  **Base Layer:** Set `body` background to `#050505` and hide the default cursor. Implement the custom `div#cursor` with the specific JS blend-mode logic provided in the reference.
> 3.  **Glassmorphism:** All containers must use the `glass-panel` class: `bg-white/5`, `backdrop-blur-md`, `border-white/5`.
> 4.  **Typography:**
>     *   Use `JetBrains Mono` for all labels, dates, and buttons (uppercase).
>     *   Use `Space Grotesk` for all headings (bold, tight tracking).
> 5.  **Interactions:**
>     *   Implement `GSAP ScrollTrigger` for fade-up animations on all sections.
>     *   Ensure all clickable elements have the class `.hover-trigger` so the custom cursor expands when hovering them.
> 6.  **Color:** Use `#00f3ff` strictly for accents. Do not overuse.
> 7.  **Images:** Wrap images in a container with `overflow-hidden`. Apply a grayscale filter that removes on hover, while simultaneously scaling the image to 1.1x.