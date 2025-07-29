from typing import List, Dict
import random

# Sample mock product metadata extractor

def generate_title(brand: str, model: str, type_: str, color: str) -> str:
    return f"{brand} {model} {type_} - {color}"

def generate_description(condition: str, features: List[str]) -> str:
    bullet_points = '\n'.join(f"- {feature}" for feature in features)
    return f"Condition: {condition}\n\nFeatures:\n{bullet_points}"

def recommend_price(market_prices: List[float]) -> str:
    if not market_prices:
        return "$??"
    low, high = min(market_prices), max(market_prices)
    return f"${int(low)}–${int(high)}"


def mock_listing_from_metadata(metadata: Dict) -> Dict:
    return {
        "title": generate_title(metadata['brand'], metadata['model'], metadata['type'], metadata['color']),
        "description": generate_description(metadata['condition'], metadata['features']),
        "price_range": recommend_price(metadata.get('market_prices', []))
    }


# Example usage:
if __name__ == '__main__':
    test_meta = {
        'brand': 'Sony',
        'model': 'WH-1000XM4',
        'type': 'Wireless Headphones',
        'color': 'Black',
        'condition': 'Excellent - minimal wear',
        'features': ["Noise cancelling", "Bluetooth 5.0", "30hr battery life"],
        'market_prices': [199.99, 219.95, 249.00]
    }
    listing = mock_listing_from_metadata(test_meta)
    for k, v in listing.items():
        print(f"{k.title()}:\n{v}\n")