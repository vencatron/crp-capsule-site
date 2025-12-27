#!/usr/bin/env python3
"""
Generate continuation frames using image-to-image with Gemini.
Each frame is a subtle variation of the previous frame (flip-book style).
"""

import time
import base64
from pathlib import Path
from google import genai
from google.genai import types
from PIL import Image
import io

# Configuration
API_KEY = "AIzaSyAnVDboJXeLmcEK-9Ao4pvBiqqPIKk-TNc"
OUTPUT_DIR = Path("/Users/ronnie.duarte/Development/crp-capsule-site/frame-2")
START_FRAME = 122
NUM_FRAMES = 15

# Initialize client
client = genai.Client(api_key=API_KEY)

# Subtle variation prompt - asking for MINIMAL changes
VARIATION_PROMPT = """Look at this image carefully. Create an almost identical version with only these VERY SUBTLE changes:
- The glowing orbs should float/drift by just 1-2 pixels in random directions
- The central glowing orb's brightness can pulse very slightly (2-3% brighter or dimmer)
- The mist/clouds at the bottom can shift very slightly
- The figure remains in the EXACT same position and pose

CRITICAL: The output must be 99% identical to the input. Only the tiniest animation-like changes.
Maintain the exact same:
- Color palette (warm amber/sepia)
- Composition and framing
- Art style (painterly digital illustration)
- All major elements in their positions

This is for a flip-book animation - changes must be nearly imperceptible."""


def load_image_as_base64(image_path: Path) -> str:
    """Load an image and return as base64 string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def generate_variation(input_path: Path, output_path: Path, frame_num: int) -> bool:
    """Generate a subtle variation of the input image."""
    try:
        print(f"Generating frame {frame_num:04d} from {input_path.name}...")

        # Load the input image
        with open(input_path, "rb") as f:
            image_bytes = f.read()

        # Create the image part for Gemini
        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/webp"
        )

        # Generate variation using Gemini
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=[
                image_part,
                VARIATION_PROMPT
            ],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            )
        )

        # Extract generated image
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                if hasattr(part, 'inline_data') and part.inline_data:
                    inline_data = part.inline_data
                    if isinstance(inline_data.data, str):
                        image_data = base64.b64decode(inline_data.data)
                    else:
                        image_data = inline_data.data

                    # Open and save as webp
                    img = Image.open(io.BytesIO(image_data))
                    img.save(output_path, "WEBP", quality=90)

                    print(f"  SUCCESS: Saved {output_path}")
                    return True

        print(f"  No image in response for frame {frame_num}")
        return False

    except Exception as e:
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main generation loop - chain frames together."""
    print(f"Starting image-to-image frame generation...")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Generating frames {START_FRAME} to {START_FRAME + NUM_FRAMES - 1}")
    print("-" * 50)

    successful = 0
    failed = 0

    # Start from the last existing frame
    current_input = OUTPUT_DIR / f"frame_{START_FRAME - 1:04d}.webp"

    if not current_input.exists():
        print(f"ERROR: Starting frame {current_input} does not exist!")
        return

    for i in range(NUM_FRAMES):
        frame_num = START_FRAME + i
        output_path = OUTPUT_DIR / f"frame_{frame_num:04d}.webp"

        # Skip if already exists
        if output_path.exists():
            print(f"Frame {frame_num:04d} already exists, using as next input...")
            current_input = output_path
            successful += 1
            continue

        # Generate variation from current input
        if generate_variation(current_input, output_path, frame_num):
            successful += 1
            # Use this frame as input for the next one
            current_input = output_path
        else:
            failed += 1
            print(f"  FAILED: Could not generate frame {frame_num}")
            # Don't break - try to continue with same input

        # Wait between requests to avoid rate limiting
        if i < NUM_FRAMES - 1:
            wait_time = 3
            print(f"  Waiting {wait_time}s before next request...")
            time.sleep(wait_time)

    print("-" * 50)
    print(f"Generation complete!")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total frames in frame-2: {len(list(OUTPUT_DIR.glob('frame_*.webp')))}")


if __name__ == "__main__":
    main()
