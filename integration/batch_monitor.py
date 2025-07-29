import os
import time
import json
from image_analysis.group_and_identify import group_similar_images
from listing_generator.generate_listing import mock_listing_from_metadata

SHARED_FOLDER = "uploaded_batches/"
OUT_FOLDER = "generated_listings/"
POLL_INTERVAL = 10  # seconds

os.makedirs(OUT_FOLDER, exist_ok=True)


def simulate_metadata(image_group: list):
    # Placeholder — in real flow, vision search would be used
    return {
        'brand': 'GenericBrand',
        'model': 'ModelX',
        'type': 'Electronic Accessory',
        'color': 'Black',
        'condition': 'Good - minor wear',
        'features': ['Test feature A', 'Feature B', 'Feature C'],
        'market_prices': [25.0, 30.0, 29.5]
    }


def process_new_batches():
    seen_batches = set()
    while True:
        for folder in os.listdir(SHARED_FOLDER):
            full_path = os.path.join(SHARED_FOLDER, folder)
            if os.path.isdir(full_path) and folder not in seen_batches:
                print(f"🟢 New batch detected: {folder}")
                images = [os.path.join(full_path, f) for f in os.listdir(full_path)
                          if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                groups = group_similar_images(images)
                batch_data = {}
                for gid, img_list in groups.items():
                    metadata = simulate_metadata(img_list)
                    listing = mock_listing_from_metadata(metadata)
                    listing['images'] = img_list
                    batch_data[gid] = listing
                with open(os.path.join(OUT_FOLDER, folder + ".json"), 'w') as f:
                    json.dump(batch_data, f, indent=2)
                seen_batches.add(folder)
        time.sleep(POLL_INTERVAL)


if __name__ == '__main__':
    process_new_batches()