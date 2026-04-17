# WebSociology: Design System & UI Guidelines

This document outlines the core design language, typography, color palette, and UI components used in the WebSociology website. You can use this as a blueprint to replicate the premium, modern, and interactive educational aesthetic for any future projects.

## 1. Core Technologies
*   **CSS Framework:** Tailwind CSS (configured via CDN)
*   **Data Visualization:** Chart.js
*   **Icons:** Emojis (used playfully for icons) & SVG for functional UI (like Dark Mode toggles).

## 2. Typography
A modern, highly legible sans-serif font is used to maintain a clean and professional look while ensuring readability for educational content.
*   **Primary Font:** `Inter`, sans-serif
*   **Weights Used:** Regular (400), Medium (500), Semi-Bold (600), Bold (700), Extra-Bold (800)

## 3. Color Palette & Theming
The website features a dynamic Light and Dark mode, utilizing Tailwind's `dark:class` configuration. It employs a neutral base with vibrant, distinct accent colors for different educational modules.

### Neutral Base Colors
*   **Light Mode:** 
    *   Background: `bg-slate-50` (Very light, cool gray)
    *   Text: `text-slate-800` (Deep slate, softer than pure black)
    *   Card Surface: `bg-white` with `slate-100` borders.
*   **Dark Mode:**
    *   Background: `bg-slate-900` (Deep, rich dark gray)
    *   Text: `text-slate-200` (Light, readable gray)
    *   Card Surface: `bg-slate-800` with `slate-700` borders.

### Vibrant Accents (Module Categorization)
Each lesson or module has a distinct color identity used for its icon gradients, hover shadows, text highlights, and decorative background blobs.
*   **Module 1 (Perspectives):** Indigo (`indigo-500`, `indigo-600`, `purple-600`)
*   **Module 2 (Research):** Teal (`teal-500`, `emerald-500`)
*   **Module 3/Quiz:** Amber/Orange (`amber-500`, `orange-600`)

---

## 4. Global Layout & Spacing
*   **Container Width:** The maximum width of the content is restricted to `max-w-5xl`. This ensures lines of text don't span too wide, maximizing readability.
*   **Margin & Padding:** Generous padding (`px-4 sm:px-6 lg:px-8`, `py-12`) is used to let content breathe.
*   **Transitions:** Smooth transitions are applied globally (`transition-colors duration-300`) to seamlessly swap between Light and Dark themes.

---

## 5. Key UI Components

### 5.1. Glassmorphic Navigation Bar
*   **Position:** Sticky at the top (`sticky top-0 z-50`).
*   **Aesthetic:** Uses a translucent background (`bg-white/90` or `bg-slate-900/90`) directly paired with a backdrop blur (`backdrop-blur-md`). This creates a frosted glass effect over the content as the user scrolls.

### 5.2. Hero Section (Header)
A large, cinematic header that introduces the page.
*   **Shape:** heavily rounded corners (`rounded-[2rem] md:rounded-[2.5rem]`).
*   **Background:** An image with a dark overlying blend mode (`mix-blend-overlay opacity-80` layered over `bg-stone-900`) to ensure text readability.
*   **Content Box:** The text is housed inside a prominent glassmorphism container:
    *   `bg-white/10 backdrop-blur-xl border border-white/20 p-10 md:p-14 rounded-3xl shadow-2xl`
    *   The title features heavy weight (`font-extrabold`) and a drop shadow (`drop-shadow-md`).

### 5.3. Interative Module Cards
The grid of lessons is designed to feel highly tactile and premium.
*   **Shape & Shadow:** Large rounded corners (`rounded-[1.5rem]`). Subtle default shadow that drastically expands and glows on hover (`hover:shadow-2xl hover:shadow-{color}-500/10`).
*   **Hover Animation:** On mouse hover, the card floats upwards (`hover:-translate-y-2`) with a smooth 500ms transition (`transition-all duration-500`).
*   **Decorative Background:** An absolute-positioned quarter-circle blob sits in the top-right corner to break the boxed layout (`absolute top-0 right-0 w-32 h-32 bg-{color}-50/50 rounded-bl-full -z-10`).
*   **Gradients:** Icons are placed in vibrant, gradient boxes (`bg-gradient-to-br from-{color}-500 to-{color}-600 rounded-2xl`).
*   **Tag "Pills":** Module numbers/categories are marked with small, uppercase, bold tracking tags (`text-[10px] px-3 py-1 bg-slate-100 rounded-full tracking-wider`).

### 5.4. Informational / "Quick Recap" Panels
Nested information uses distinct "boxes within boxes" styling.
*   **Outer Container:** `bg-white dark:bg-slate-800 rounded-3xl p-6 md:p-8 shadow-lg`.
*   **Inner Fact-Boxes:** `bg-stone-50 dark:bg-slate-900/50 p-4 rounded-xl border border-stone-100 dark:border-slate-700`.
*   **Hierarchy:** Tiny, uppercase labels with a small emoji indicate the subject of the inner box (`text-xs font-bold uppercase tracking-wider`).

---

## 6. Micro-Interactions
*   **Buttons:** Call-to-action buttons feature subtle scaling and arrow translations (`group-hover:translate-x-2`, `group-hover:scale-110`) when the mouse enters the interactive area.
*   **Accordions:** Panel toggles include arrows that smoothly rotate 180 degrees when expanded.

## Replicating the Design
When bringing this design to a new educational website:
1.  **Set up Tailwind CDN** and include the dark mode toggle script at the bottom of the body.
2.  **Import the "Inter" font** via Google Fonts.
3.  **Establish Accent Colors** for your new modules (e.g., using Tailwind's Rose, Cyan, Lime, etc.) and apply them to the gradient icon boxes, the top-right decorative corner blobs, and the hover shadows of your cards.
4.  **Use the HTML structure** of the 'Module Cards' as a direct template component.
