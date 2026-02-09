# Mironix Furniture | Live Uncommon

A modern, responsive furniture showcase website built with **Tailwind CSS**, **Swiper.js**, and **Lenis smooth scroll**.

## Features

### 🎨 Design Highlights
- **Glassmorphic Navigation**: Frosted glass effect navbar with blur and transparency
- **Hero Carousel**: Full-screen image slider with Ken Burns zoom effect (fade transitions)
- **Featured Carousel**: Continuous auto-scrolling product carousel with 5-second resume after user interaction
- **Smooth Scrolling**: Lenis.js integration for buttery-smooth scroll experience
- **Responsive Design**: Fully responsive across mobile, tablet, and desktop
- **Custom Cursor**: Interactive cursor that scales on hover over clickable elements
- **Reveal Animations**: Staggered scroll-triggered animations using Intersection Observer

### 📦 Collections
- **Home Furniture**: Sofas, Wardrobes, Wall Separators, Pergolas, Gazebos
- **Office Systems**: Executive Desks, Workstations, Conference Tables, Cubicle Panels
- **Institutional**: School Benches, Lab Furniture, Library Sets, Public Seating

### 🔄 Carousel Behavior
- **Hero Swiper**: 6-slide auto-rotating banner (6s delay)
- **Featured Swiper**: Continuous horizontal scroll with pause on:
  - Mouse hover
  - Touch/drag interaction
  - Wheel scroll
  - Pointer/mouse down
  - Auto-resumes after 5 seconds of inactivity

## Tech Stack

- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first styling
- **Swiper.js** - Touch slider library
- **Lenis** - Smooth scroll library
- **Vanilla JavaScript** - Custom interactions and animations

## Project Structure

```
mironix/
├── index.html          # Main page with all sections
├── README.md           # Project documentation
```

## Sections

1. **Navigation** - Fixed glassmorphic navbar with smooth scrolling links
2. **Hero Carousel** - Full-screen slides with call-to-action buttons
3. **About (Saga)** - Company story with rotating border animation
4. **Featured Collections** - Horizontal carousel of furniture pieces
5. **Categories** - Three department showcase cards with hover effects
6. **Footer** - Contact info, social links, and back-to-top button

## Customization

### Navbar
- Adjust opacity: `.background: rgba(253, 251, 247, 0.7)` (change `0.7`)
- Modify blur: `backdrop-filter: blur(15px)` (change `15px`)
- Reduce height: Use `py-2` for compact, `p-5` for spacious padding

### Carousels
**Hero Swiper:**
- `delay: 6000` - Change slide interval (ms)
- `speed: 1000` - Transition duration

**Featured Swiper:**
- `speed: 5000` - Scroll speed
- `spaceBetween: 20` - Gap between slides
- Resume delay: Change `5000` in `scheduleResume()` function

### Colors
Edit CSS variables in `:root`:
```css
--pale-oak: #cdc5b4;
--ink-black: #001524;
--blue-slate: #6a6b83;
--walnut: #6d3d14;
--cream-solid: #fdfbf7;
```

## Installation & Setup

### Local Development
1. Clone the repository:
```bash
git clone https://github.com/CHAITU2405/Mironix.git
cd Mironix
```

2. Open in browser:
   - Use **Live Server** extension in VS Code
   - Or open `index.html` directly in your browser

### No Build Step Required
This is a static HTML project—no npm packages or build tools needed. All libraries are loaded via CDN.

## External Dependencies

All dependencies are loaded from CDN:
- **Tailwind CSS**: https://cdn.tailwindcss.com
- **Swiper.js**: https://cdn.jsdelivr.net/npm/swiper@11
- **Lenis**: https://unpkg.com/@studio-freight/lenis@1.0.42
- **Google Fonts**: Playfair Display, Plus Jakarta Sans

## Browser Support

- Chrome/Edge (Latest)
- Firefox (Latest)
- Safari (Latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Company Info

**Mironix Furniture Pvt. Ltd.**  
📍 Headquarters: Shivnand Nagar, Raipur (C.G.) 492008 & Bhilai (C.G.) 490001  
📞 M Vinod Kumar: +91 74002 64528  
📞 Santosh Kumar: +91 88854 97802  
✉️ mironix2025@gmail.com

---

**© 2025 Mironix Furniture Pvt Ltd. | Live Uncommon**
