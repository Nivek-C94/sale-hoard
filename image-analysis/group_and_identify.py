import os
from typing import List, Dict
from collections import defaultdict
from PIL import Image
import hashlib


def image_hash(image_path: str) -> str:
    with Image.open(image_path) as img:
        img = img.resize((64, 64)).convert("L")
        pixels = list(img.getdata())
        avg = sum(pixels) / len(pixels)
        bits = ''.join('1' if pixel > avg else '0' for pixel in pixels)
        return hashlib.md5(bits.encode()).hexdigest()


def group_similar_images(image_paths: List[str]) -> Dict[str, List[str]]:
    hash_to_images = defaultdict(list)
    for path in image_paths:
        try:
            h = image_hash(path)
            hash_to_images[h].append(path)
        except Exception as e:
            print(f"Error processing {path}: {e}")
    return dict(hash_to_images)


# Placeholder for actual vision-based model or ChatGPT visual input
# For now, assume function is manually invoked with paths
if __name__ == '__main__':
    import sys
    folder = sys.argv[1] if len(sys.argv) > 1 else '.'
    images = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    groups = group_similar_images(images)
    for gid, paths in groups.items():
        print(f"\nProduct Group: {gid[:8]}...")
        for p in paths:
            print(f"  - {os.path.basename(p)}")