# CRP Capsule Scroll Site

This is a scroll-driven animation site prototype using a sequence of 150 WebP frames.

## How to Run

1.  Open your terminal.
2.  Navigate to this directory:
    ```bash
    cd /Users/ronnie.duarte/Development/crp-capsule-site/frames
    ```
3.  Start a simple local web server:
    *   **Python 3:**
        ```bash
        python3 -m http.server
        ```
    *   **Node (if `http-server` is installed):**
        ```bash
        npx http-server .
        ```
4.  Open your browser and go to `http://localhost:8000` (or the port shown in your terminal).

## Structure

*   `index.html`: Main entry point and content structure.
*   `style.css`: Styles for sticky canvas and overlay text.
*   `script.js`: Handles image preloading, canvas rendering, and scroll mapping.
*   `frame_XXXX.webp`: The image sequence.

## Customization

*   **Speed:** Adjust the height of `.content` in `style.css` (currently `500vh`) to make the scroll faster or slower.
*   **Text:** Edit `index.html` to change the overlay text.
*   **Frames:** Replace the images in this folder to change the animation.
