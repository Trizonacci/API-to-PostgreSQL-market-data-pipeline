from fetch_prices import fetch_prices, normalize_prices
from db import insert_prices

def main():
    print("Starting Project 9: API → SQL pipeline")

    raw_prices = fetch_prices()
    print("Raw API response:")
    print(raw_prices)

    normalized = normalize_prices(raw_prices)

    print("\nNormalized rows:")
    for row in normalized:
        print(row)

    insert_prices(normalized)

if __name__ == "__main__":
    main()