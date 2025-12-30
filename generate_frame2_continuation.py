#!/usr/bin/env python3
"""
Generate continuation frames for frame-2 directory using Gemini/Imagen API.
Theme: Money being shielded from the IRS
Style: Match existing frame-2 painterly/artistic style

Requires billing enabled for Imagen 4.0 access.
"""

import os
import time
import base64
import re
from pathlib import Path
from google import genai
from google.genai import types
from PIL import Image
import io

# Configuration
API_KEY = ""
OUTPUT_DIR = Path("/Users/ronnie.duarte/Development/crp-capsule-site/frame-2")
START_FRAME = 122
NUM_FRAMES = 15  # Generate 15 new frames (122-136)

# Initialize client
client = genai.Client(api_key=API_KEY)

# Style reference based on existing frame-2 images
BASE_STYLE = """
Painterly digital illustration, warm amber and sepia color palette,
ethereal dreamlike atmosphere, dark moody background with golden clouds and mist,
cinematic lighting, concept art style, high detail,
similar to fantasy concept art with warm glowing orbs and silhouetted figures
"""

# Prompts for the "money shielded from IRS" sequence
FRAME_PROMPTS = [
    # Frames 122-124: Introduction of shield concept
    f"{BASE_STYLE}. A silhouetted figure standing with arms outstretched, a large translucent golden protective dome or shield beginning to form around them, scattered dollar bills and gold coins floating inside the shield, warm golden glow emanating from within",

    f"{BASE_STYLE}. A silhouetted person surrounded by a glowing golden energy shield, floating money and coins swirling gently inside the protective barrier, tax documents bouncing off the shield exterior, dramatic lighting",

    f"{BASE_STYLE}. Single figure with arms raised triumphantly inside a radiant golden force field, stacks of money and glowing orbs containing wealth symbols floating peacefully inside, dark storm clouds swirling outside but unable to penetrate",

    # Frames 125-127: Shield strengthening
    f"{BASE_STYLE}. Person standing confidently as a brilliant golden shield dome fully envelops them, inside the shield floating glowing orbs contain images of houses, money, and prosperity, outside the shield faded gray tax forms drift away powerlessly",

    f"{BASE_STYLE}. Majestic golden protective barrier surrounding a silhouetted figure, inside the barrier warm light illuminates floating coins, property deeds, and wealth symbols, the shield reflects and deflects approaching storm clouds",

    f"{BASE_STYLE}. A person with raised arms beneath a cathedral-like dome of golden light, floating within are glowing spheres containing visions of real estate, passive income, and family prosperity",

    # Frames 128-130: Transformation of tax money into assets
    f"{BASE_STYLE}. Figure reaching toward floating golden orbs, each orb shows money transforming into buildings and real estate, a protective aura surrounds everything, warm hopeful atmosphere",

    f"{BASE_STYLE}. Silhouetted person orchestrating the transformation within their golden shield, dollar bills morphing into miniature buildings and homes inside glowing orbs, the shield grows brighter as more assets form",

    f"{BASE_STYLE}. Person standing in center of radiant golden dome, surrounded by floating orbs now filled with thriving rental properties and growing investments",

    # Frames 131-133: Wealth accumulation inside shield
    f"{BASE_STYLE}. The protective golden shield now contains a small universe of wealth - floating orbs with properties, passive income streams visualized as golden rivers, the figure stands peacefully as their protected wealth grows",

    f"{BASE_STYLE}. A figure with arms open wide, their golden protective barrier now filled with countless glowing orbs containing real estate investments, family moments, and financial freedom symbols, warm triumphant lighting",

    f"{BASE_STYLE}. Person silhouetted against their magnificent golden shield filled with floating visions of generational wealth - houses, happy families, growing investments",

    # Frames 134-136: Final triumph
    f"{BASE_STYLE}. Wide shot of figure standing before an expansive golden dome of protection, inside swirl hundreds of glowing orbs containing dreams realized - properties, wealth, legacy - the shield stands impenetrable",

    f"{BASE_STYLE}. Triumphant silhouette with arms raised, surrounded by their fortress of golden light, floating within are orbs showing the journey from tax burden to asset empire, warm rays of light breaking through clouds above",

    f"{BASE_STYLE}. Final frame - a person standing peacefully within their radiant golden sanctuary, orbs of protected wealth float serenely around them, the warm light suggests safety, prosperity, and a secured financial future, cinematic wide shot",
]


def generate_frame_imagen4(prompt: str, frame_number: int) -> bool:
    """Generate a single frame using Imagen 4.0 (requires billing)."""
    try:
        print(f"Generating frame {frame_number:04d} with Imagen 4.0...")

        response = client.models.generate_images(
            model="imagen-4.0-generate-001",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="16:9",
            )
        )

        if response.generated_images:
            generated = response.generated_images[0]
            output_path = OUTPUT_DIR / f"frame_{frame_number:04d}.webp"

            # The image data is in generated.image.image_bytes
            image_bytes = generated.image.image_bytes

            # Open with PIL and save as webp
            img = Image.open(io.BytesIO(image_bytes))
            img.save(output_path, "WEBP", quality=90)

            print(f"  SUCCESS: Saved {output_path}")
            return True
        else:
            print(f"  No image generated for frame {frame_number}")
            return False

    except Exception as e:
        print(f"  Error with Imagen 4.0: {e}")
        import traceback
        traceback.print_exc()
        return False


def generate_frame_gemini(prompt: str, frame_number: int) -> bool:
    """Generate a single frame using Gemini image generation (fallback)."""
    try:
        print(f"Generating frame {frame_number:04d} with Gemini 2.0 Flash Exp...")

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=f"Generate an image: {prompt}",
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            )
        )

        # Extract image from response
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if hasattr(part, 'inline_data') and part.inline_data:
                    inline_data = part.inline_data
                    # The data might already be bytes or need decoding
                    if isinstance(inline_data.data, str):
                        image_data = base64.b64decode(inline_data.data)
                    else:
                        image_data = inline_data.data

                    image = Image.open(io.BytesIO(image_data))

                    # Save as webp
                    output_path = OUTPUT_DIR / f"frame_{frame_number:04d}.webp"
                    image.save(output_path, "WEBP", quality=90)

                    print(f"  SUCCESS: Saved {output_path}")
                    return True

        print(f"  No image in response for frame {frame_number}")
        return False

    except Exception as e:
        print(f"  Error with Gemini: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main generation loop."""
    print(f"Starting frame generation for frame-2 continuation...")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Generating frames {START_FRAME} to {START_FRAME + NUM_FRAMES - 1}")
    print("-" * 50)

    # Ensure output directory exists
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    successful = 0
    failed = 0

    for i, prompt in enumerate(FRAME_PROMPTS):
        frame_num = START_FRAME + i

        # Check if frame already exists
        output_path = OUTPUT_DIR / f"frame_{frame_num:04d}.webp"
        if output_path.exists():
            print(f"Frame {frame_num:04d} already exists, skipping...")
            successful += 1
            continue

        # Try Imagen 4.0 first (best quality), fall back to Gemini
        if generate_frame_imagen4(prompt, frame_num):
            successful += 1
        elif generate_frame_gemini(prompt, frame_num):
            successful += 1
        else:
            failed += 1
            print(f"  FAILED: Could not generate frame {frame_num}")

        # Wait between requests
        if i < len(FRAME_PROMPTS) - 1:
            wait_time = 5
            print(f"  Waiting {wait_time}s before next request...")
            time.sleep(wait_time)

    print("-" * 50)
    print(f"Generation complete!")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total frames in frame-2: {len(list(OUTPUT_DIR.glob('frame_*.webp')))}")


if __name__ == "__main__":
    main()
