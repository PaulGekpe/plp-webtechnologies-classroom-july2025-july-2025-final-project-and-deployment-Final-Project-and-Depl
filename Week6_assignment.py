# --- Auto-install 'requests' if missing ---
try:
    import requests
except ImportError:
    import subprocess
    import sys
    print("📦 'requests' not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests  # Try again after installing

import os
from urllib.parse import urlparse
import hashlib

# --- Utility Functions ---
def is_image_content(response):
    """Check if the Content-Type header indicates an image."""
    content_type = response.headers.get("Content-Type", "")
    return content_type.startswith("image/")

def file_exists(filepath, content):
    """Check if a file already exists and has the same content (by MD5 hash)."""
    if os.path.exists(filepath):
        with open(filepath, 'rb') as f:
            existing_hash = hashlib.md5(f.read()).hexdigest()
        new_hash = hashlib.md5(content).hexdigest()
        return existing_hash == new_hash
    return False

def download_image(url):
    """Download a single image from a URL with safety checks."""
    try:
        os.makedirs("Fetched_Images", exist_ok=True)

        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check Content-Type
        if not is_image_content(response):
            print(f"✗ Skipped (Not an image): {url}")
            return

        # Check Content-Length (limit to ~5MB for safety)
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 5 * 1024 * 1024:
            print(f"⚠ Skipped (File too large >5MB): {url}")
            return

        # Extract filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
        filepath = os.path.join("Fetched_Images", filename)

        # Prevent duplicates
        if file_exists(filepath, response.content):
            print(f"⚠ Duplicate skipped: {filename}")
            return

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")

# --- Main Program ---
def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Accept multiple URLs
    urls = input("Please enter image URLs (comma-separated): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        download_image(url)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
