import requests
from datetime import datetime

ASSETS = ["bitcoin", "ethereum", "solana", "cardano"]

def fetch_prices(assets=ASSETS):
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": ",".join(assets),
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def normalize_prices(raw_prices):
    normalized = []
    timestamp = datetime.utcnow()

    for asset, data in raw_prices.items():
        if not isinstance(data, dict):
            continue

        price = data.get("usd")

        if price is None:
            continue

        if not isinstance(price, (int, float)):
            continue

        normalized.append({
            "symbol": asset,
            "price_usd": float(price),
            "timestamp": timestamp
        })

    return normalized
