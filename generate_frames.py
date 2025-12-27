import os
import math
from PIL import Image, ImageDraw, ImageFont

# Configuration
OUTPUT_DIR = "frames"
WIDTH = 1920
HEIGHT = 1080
TOTAL_FRAMES = 150

# Colors
COLOR_NAVY = (26, 54, 93)     # #1a365d
COLOR_GOLD = (184, 134, 11)   # #b8860b
COLOR_WHITE = (255, 255, 255)
COLOR_RED = (200, 50, 50)
COLOR_GRAY = (200, 200, 200)
COLOR_SHADOW = (0, 0, 0, 100)

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Font loading helper
def load_font(size, bold=False):
    try:
        # MacOS standard fonts
        if bold:
            return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size, index=1) # Index 1 is often Bold
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except IOError:
        try:
            return ImageFont.truetype("Arial.ttf", size)
        except IOError:
            return ImageFont.load_default()

def ease_in_out(t):
    return t * t * (3 - 2 * t)

def draw_centered_text(draw, text, font, y_offset, color, opacity=255, shadow=False):
    # Calculate text size
    try:
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        text_width = right - left
        text_height = bottom - top
    except AttributeError:
        text_width, text_height = draw.textsize(text, font=font)
    
    x = (WIDTH - text_width) // 2
    y = (HEIGHT - text_height) // 2 + y_offset
    
    # Draw Shadow
    if shadow and opacity > 0:
        shadow_color = COLOR_SHADOW[:3] + (int(opacity * 0.5),)
        draw.text((x+5, y+5), text, font=font, fill=shadow_color)

    # Draw Text
    text_color = color + (int(opacity),)
    draw.text((x, y), text, font=font, fill=text_color)

def generate_frame(frame_num):
    # Create base image
    img = Image.new('RGBA', (WIDTH, HEIGHT), COLOR_NAVY + (255,))
    draw = ImageDraw.Draw(img, 'RGBA')
    
    # Common Fonts
    font_xl = load_font(140, bold=True)
    font_l = load_font(100, bold=True)
    font_m = load_font(70)
    font_s = load_font(40)

    # --- ACT 1: The Problem (Frames 1-30) ---
    if 1 <= frame_num <= 30:
        # Title Sequence
        if frame_num <= 15:
            # Fade in "Stop Paying Taxes"
            progress = (frame_num - 1) / 14.0
            opacity = int(255 * ease_in_out(progress))
            draw_centered_text(draw, "Stop Paying Taxes.", font_xl, -80, COLOR_WHITE, opacity, shadow=True)
            
            # Fade in "Start Building Assets" slightly later
            if frame_num > 5:
                sub_progress = (frame_num - 6) / 9.0
                sub_opacity = int(255 * ease_in_out(sub_progress))
                draw_centered_text(draw, "Start Building Assets.", font_xl, 80, COLOR_GOLD, sub_opacity, shadow=True)
        
        # Transition to Pie Chart
        else:
            # Text moves up and fades
            progress = (frame_num - 16) / 14.0
            t_offset = -80 - (progress * 200)
            t_opacity = int(255 * (1 - progress))
            
            draw_centered_text(draw, "Stop Paying Taxes.", font_xl, int(t_offset), COLOR_WHITE, t_opacity)
            draw_centered_text(draw, "Start Building Assets.", font_xl, int(t_offset) + 160, COLOR_GOLD, t_opacity)
            
            # Pie Chart Enters
            chart_opacity = int(255 * progress)
            cx, cy = WIDTH // 2, HEIGHT // 2 + 100
            radius = 300
            
            # Draw Base Circle (Net Income)
            draw.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), outline=COLOR_WHITE + (chart_opacity,), width=8)
            
            # Draw Red Slice (Taxes) - grows
            if progress > 0:
                end_angle = -90 + (360 * 0.40 * progress)
                draw.pieslice((cx-radius, cy-radius, cx+radius, cy+radius), -90, end_angle, fill=COLOR_RED + (chart_opacity,))
                
            # Chart Labels
            if progress > 0.5:
                draw_centered_text(draw, "40% Taxes", font_l, 100, COLOR_WHITE, int(chart_opacity * ((progress-0.5)*2)), shadow=True)


    # --- ACT 2: The Solution (Frames 31-60) ---
    elif 31 <= frame_num <= 60:
        # Dollar to Building Transformation
        progress = (frame_num - 31) / 29.0
        cx, cy = WIDTH // 2, HEIGHT // 2
        
        # 1. The Dollar Sign (Fading Out)
        if progress < 0.5:
            d_opacity = int(255 * (1 - (progress * 2)))
            draw_centered_text(draw, "$", load_font(400, bold=True), 0, COLOR_GOLD, d_opacity)
            
        # 2. The Building (Fading In & Assembling)
        if progress > 0.2:
            b_progress = (progress - 0.2) / 0.8
            b_opacity = int(255 * b_progress)
            
            # Building Body
            bw, bh = 300, 500
            rect = [cx - bw//2, cy - bh//2, cx + bw//2, cy + bh//2]
            draw.rectangle(rect, outline=COLOR_GOLD + (b_opacity,), width=10)
            
            # Windows (Grid appearing)
            rows, cols = 6, 4
            pad = 20
            w_w = (bw - (cols+1)*pad) // cols
            w_h = (bh - (rows+1)*pad) // rows
            
            for r in range(rows):
                for c in range(cols):
                    # Stagger window appearance
                    win_threshold = (r * cols + c) / (rows * cols)
                    if b_progress > win_threshold:
                         wx = rect[0] + pad + c*(w_w+pad)
                         wy = rect[1] + pad + r*(w_h+pad)
                         draw.rectangle([wx, wy, wx+w_w, wy+w_h], fill=COLOR_GOLD + (b_opacity,))

        # Text Overlay
        if progress > 0.6:
            text_opacity = int(255 * ((progress - 0.6) / 0.4))
            draw_centered_text(draw, "Build Real Assets.", font_l, 350, COLOR_WHITE, text_opacity, shadow=True)


    # --- ACT 3: The Mechanics (Frames 61-90) ---
    elif 61 <= frame_num <= 90:
        # Cost Segregation
        progress = (frame_num - 61) / 29.0
        
        # Layout: Building on left, Tax Form on right
        # We simulate this by moving elements
        
        # Building (already there, scale down and move left)
        scale = 1.0 - (0.5 * progress)
        move_x = -400 * progress
        
        cx, cy = WIDTH // 2 + move_x, HEIGHT // 2
        bw, bh = 300 * scale, 500 * scale
        
        # Draw Scaled Building
        draw.rectangle([cx-bw/2, cy-bh/2, cx+bw/2, cy+bh/2], outline=COLOR_GOLD + (255,), width=5)
        # (Simplified windows for scaled version)
        draw.rectangle([cx-bw/2+10, cy-bh/2+10, cx+bw/2-10, cy+bh/2-10], fill=COLOR_GOLD + (100,))

        # Tax Form / Benefits appearing on Right
        if progress > 0.3:
            r_opacity = int(255 * ((progress - 0.3) / 0.7))
            rx = WIDTH // 2 + 300
            
            draw_centered_text(draw, "Tax Savings", font_l, -150, COLOR_WHITE, r_opacity)
            draw_centered_text(draw, "$300,000", font_xl, 0, COLOR_GOLD, r_opacity)
            draw_centered_text(draw, "Year 1 Deduction", font_m, 120, COLOR_WHITE, r_opacity)


    # --- ACT 4: Partnership & Risk (Frames 91-120) ---
    elif 91 <= frame_num <= 120:
        progress = (frame_num - 91) / 29.0
        
        # Shield Animation
        cx, cy = WIDTH // 2, HEIGHT // 2
        
        # Draw Shield Shape
        # Simple shield: rectangle top, triangle bottom
        sw, sh = 400, 500
        
        # Shield Outline
        points = [
            (cx-sw//2, cy-sh//2), # Top Left
            (cx+sw//2, cy-sh//2), # Top Right
            (cx+sw//2, cy),       # Mid Right
            (cx, cy+sh//2),       # Bottom Tip
            (cx-sw//2, cy)        # Mid Left
        ]
        
        s_opacity = int(255 * min(1.0, progress * 2))
        draw.polygon(points, outline=COLOR_GOLD + (s_opacity,), fill=COLOR_NAVY + (s_opacity,))
        if s_opacity > 0:
             draw.line(points + [points[0]], fill=COLOR_GOLD + (s_opacity,), width=8)

        # Layers of protection appearing
        texts = ["LLC Entity", "Hazard Insurance", "D&O Coverage"]
        for i, text in enumerate(texts):
            if progress > (0.3 + i*0.2):
                t_opacity = int(255 * ease_in_out((progress - (0.3+i*0.2))/0.2))
                y_pos = -100 + i*100
                draw_centered_text(draw, text, font_m, y_pos, COLOR_WHITE, t_opacity)


    # --- ACT 5: CTA (Frames 121-150) ---
    else:
        progress = (frame_num - 121) / 29.0
        
        # "Join the Partnership"
        
        # Circle transition
        radius = 100 + (progress * 1000)
        # draw.ellipse((WIDTH//2-radius, HEIGHT//2-radius, WIDTH//2+radius, HEIGHT//2+radius), outline=COLOR_GOLD, width=2)
        
        opacity = int(255 * progress)
        
        draw_centered_text(draw, "Partner With Us", font_xl, -150, COLOR_WHITE, opacity)
        
        if progress > 0.5:
             btn_opacity = int(255 * ((progress-0.5)/0.5))
             # Button Box
             bx, by = WIDTH//2, HEIGHT//2 + 100
             bw, bh = 400, 100
             draw.rectangle([bx-bw, by-bh, bx+bw, by+bh], fill=COLOR_GOLD + (btn_opacity,))
             draw_centered_text(draw, "Schedule a Call", font_l, 100, COLOR_NAVY, btn_opacity)

    return img

# Main Loop
print(f"Generating {TOTAL_FRAMES} frames...")
for i in range(1, TOTAL_FRAMES + 1):
    frame = generate_frame(i)
    filename = f"frame_{i:04d}.webp"
    path = os.path.join(OUTPUT_DIR, filename)
    frame.save(path, "WEBP", quality=90)
    if i % 10 == 0:
        print(f"  ...frame {i}")

print("Done! Frames saved to /frames/")
