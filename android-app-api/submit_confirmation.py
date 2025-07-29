import os
import json
from desktop_automation.ebay_auto_lister import launch_ebay_lister

CONFIRM_FOLDER = "confirmed_batches/"
CREDS_FILE = "credentials/ebay.json"


def process_confirmed_listings():
    for file in os.listdir(CONFIRM_FOLDER):
        if not file.endswith(".json"):
            continue
        filepath = os.path.join(CONFIRM_FOLDER, file)
        with open(filepath, 'r') as f:
            listings = json.load(f)

        with open(CREDS_FILE, 'r') as c:
            creds = json.load(c)

        for gid, data in listings.items():
            url = launch_ebay_lister(
                metadata={
                    'title': data['title'],
                    'description': data['description'],
                    'price': int(data['price_range'].split('–')[0].strip('$'))
                },
                images=data['images'],
                credentials=creds
            )
            print(f"✅ Listed {gid[:8]}: {url}")


if __name__ == '__main__':
    process_confirmed_listings()