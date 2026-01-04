import psycopg2
from psycopg2.extras import execute_batch
from config import DB_CONFIG

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def ensure_assets(symbols):
    sql = """
    INSERT INTO assets (symbol)
    VALUES (%s)
    ON CONFLICT (symbol) DO NOTHING
    """
    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            execute_batch(cur, sql, [(s,) for s in symbols])
    conn.close()

def get_asset_ids():
    sql = "SELECT id, symbol FROM assets"
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
    conn.close()
    return {symbol: asset_id for asset_id, symbol in rows}

def insert_prices(normalized_rows):
    symbols = {row["symbol"] for row in normalized_rows}

    ensure_assets(symbols)
    asset_map = get_asset_ids()

    enriched_rows = []
    for row in normalized_rows:
        asset_id = asset_map.get(row["symbol"])
        if asset_id is None:
            continue

        enriched_rows.append(
            (asset_id, row["price_usd"], row["timestamp"])
        )

    sql = """
    INSERT INTO prices (asset_id, price_usd, timestamp)
    VALUES (%s, %s, %s)
    """

    conn = get_connection()
    with conn:
        with conn.cursor() as cur:
            execute_batch(cur, sql, enriched_rows)
    conn.close()

    print(f"Inserted {len(enriched_rows)} price rows")
