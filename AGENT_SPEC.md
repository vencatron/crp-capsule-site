# Scroll-Driven Video Animation Site Specification

## Overview
This is a reference implementation of a scroll-driven video animation website. As the user scrolls, video frames are displayed sequentially to create a smooth animation effect tied to scroll position.

**Live Reference:** https://capsules.thirdroom.studio/1/

---

## Frame Image Specifications

### File Format & Naming
- **Format:** WebP (optimized for web, great compression)
- **Naming Convention:** `frame_XXXX.webp` (4-digit zero-padded)
- **Example:** `frame_0001.webp`, `frame_0002.webp`, ... `frame_0156.webp`

### Frame Statistics (from reference site)
| Metric | Value |
|--------|-------|
| Total Frames | 156 |
| File Size Range | 43-58 KB per frame |
| Average Size | ~52 KB per frame |
| Total Size (all frames) | ~8.1 MB |

### Frame Size Progression
The frames slightly increase in file size through the animation:
- Frames 1-30: ~45-48 KB
- Frames 31-70: ~48-55 KB  
- Frames 71-120: ~54-58 KB
- Frames 121-156: ~50-55 KB

This suggests the visual complexity changes throughout the animation.

---

## How It Works

### Core Concept
1. All frames are preloaded as images
2. JavaScript listens to scroll events
3. Scroll position (0-100%) maps to frame index (1-156)
4. The visible frame updates based on scroll percentage
5. Result: scrolling plays the video forwards/backwards

### Scroll-to-Frame Mapping
```javascript
// Pseudocode
const totalFrames = 156;
const scrollPercentage = window.scrollY / (document.body.scrollHeight - window.innerHeight);
const currentFrame = Math.floor(scrollPercentage * (totalFrames - 1)) + 1;
const framePath = `frame_${String(currentFrame).padStart(4, '0')}.webp`;
```

### Key Implementation Details
- Frames are displayed in a fixed/sticky container
- Content scrolls over/under the video
- Progress indicator shows scroll percentage
- Hardware-accelerated CSS for smooth performance

---

## Generating Your Own Frames

### Option 1: From Video File
```bash
# Extract frames from video using ffmpeg
ffmpeg -i source_video.mp4 -vf "fps=10,scale=1920:-1" frame_%04d.webp

# Adjust fps for more/fewer frames:
# fps=5  → ~30 frames per 6 seconds
# fps=10 → ~60 frames per 6 seconds  
# fps=15 → ~90 frames per 6 seconds
```

### Option 2: AI Image Generation
Generate a sequence where each frame shows subtle progression:
1. Define start and end states
2. Generate 100-200 intermediate frames showing gradual transition
3. Export as WebP with quality 80-85 for optimal size/quality

### WebP Compression Settings
```bash
# Convert PNG sequence to optimized WebP
for f in *.png; do
  cwebp -q 82 "$f" -o "${f%.png}.webp"
done
```

Target: 40-60 KB per frame at 1920px width

---

## File Structure

```
project/
├── index.html
├── styles.css
├── script.js
├── frames/
│   ├── frame_0001.webp
│   ├── frame_0002.webp
│   ├── frame_0003.webp
│   └── ... (up to frame_0156.webp or more)
└── assets/
    └── logo.png
```

---

## Minimum Viable Implementation

### HTML Structure
```html
<div class="scroll-container">
  <div class="video-frame-container">
    <img id="video-frame" src="frames/frame_0001.webp" alt="Animation">
    <div class="progress-indicator">0%</div>
  </div>
  <div class="content">
    <!-- Scrollable content goes here -->
    <section>...</section>
  </div>
</div>
```

### CSS Essentials
```css
.video-frame-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: -1;
}

.video-frame-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.content {
  position: relative;
  z-index: 1;
  min-height: 300vh; /* Creates scroll distance */
}
```

### JavaScript Core
```javascript
const frameCount = 156;
const frames = [];
const frameImage = document.getElementById('video-frame');

// Preload all frames
for (let i = 1; i <= frameCount; i++) {
  const img = new Image();
  img.src = `frames/frame_${String(i).padStart(4, '0')}.webp`;
  frames.push(img);
}

// Update frame on scroll
window.addEventListener('scroll', () => {
  const scrollTop = window.scrollY;
  const maxScroll = document.body.scrollHeight - window.innerHeight;
  const scrollFraction = scrollTop / maxScroll;
  const frameIndex = Math.min(
    frameCount - 1,
    Math.floor(scrollFraction * frameCount)
  );
  frameImage.src = frames[frameIndex].src;
});
```

---

## Performance Tips

1. **Preload frames** before allowing scroll interaction
2. **Use requestAnimationFrame** for scroll handler
3. **Throttle scroll events** if needed
4. **Use CSS will-change: transform** on frame container
5. **Consider lazy loading** frames in chunks for mobile

---

## Reference Files Included

This folder contains the complete frame sequence from the reference site:
- 156 WebP frames (`frame_0001.webp` through `frame_0156.webp`)
- Original JS/CSS from the site for reference
- Total reference assets: ~9.5 MB


#####Additional context from Claude Chrome extension agent:#####



The Core Technique: Scroll-Driven Frame Sequence Animation
The site uses a canvas-based image sequence that updates based on scroll position. Here's the breakdown:
1. Prepare Your Image Sequence
Export your animation/video as a sequence of images (they use ~121 WebP frames named frame_0001.webp through frame_0121.webp). You can create these by:

Exporting frames from After Effects, Premiere, or similar
Using FFmpeg: ffmpeg -i video.mp4 -vf fps=12 frame_%04d.webp

2. The Layout Structure
html<div class="container"> <!-- position: relative; height matches content -->
  <div class="video-container"> <!-- position: sticky; top: 0 -->
    <canvas class="frame-canvas"></canvas>
  </div>
  <div class="article-sidebar"> <!-- position: fixed; z-index: 1000 -->
    <div class="article-content">
      <!-- Your story text goes here -->
    </div>
  </div>
</div>
3. Key CSS
css.container {
  position: relative;
  /* Height is set by your content length - more content = more scroll = more animation */
}

.video-container {
  position: sticky;
  top: 0;
  width: 100vw;
  height: 100vh;
  z-index: 1;
}

.frame-canvas {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.article-sidebar {
  position: fixed;
  bottom: 0;
  z-index: 1000;
  /* Text appears over the canvas */
}
4. JavaScript Scroll Handler
javascriptconst canvas = document.querySelector('.frame-canvas');
const ctx = canvas.getContext('2d');
const frameCount = 121;
const images = [];

// Preload all frames
for (let i = 1; i <= frameCount; i++) {
  const img = new Image();
  img.src = `/frames/frame_${String(i).padStart(4, '0')}.webp`;
  images.push(img);
}

// On scroll, calculate which frame to show
window.addEventListener('scroll', () => {
  const scrollProgress = window.scrollY / (document.body.scrollHeight - window.innerHeight);
  const frameIndex = Math.min(frameCount - 1, Math.floor(scrollProgress * frameCount));
  
  // Draw current frame to canvas
  ctx.drawImage(images[frameIndex], 0, 0, canvas.width, canvas.height);
});
5. Progress Indicator
Track reading progress with: (scrollY / (documentHeight - windowHeight)) * 100
Tools & Frameworks to Consider

Next.js or React - The site uses Next.js for the framework
GSAP ScrollTrigger - A popular alternative for scroll animations (though this site uses custom code)
Lottie - If you want vector animations instead of image sequences
Scrollama - Lightweight scroll-driven storytelling library

Performance Tips

Use WebP format for frames (better compression)
Preload frames before allowing scroll interaction (notice their loading indicator)
Consider lazy loading frames in chunks rather than all at once
Use requestAnimationFrame for smooth canvas updates
Set canvas dimensions explicitly to match the viewport
