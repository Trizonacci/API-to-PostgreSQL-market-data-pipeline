-- Latest price per asset
SELECT DISTINCT ON (a.symbol)
    a.symbol,
    p.price_usd,
    p.timestamp
FROM prices p
JOIN assets a ON p.asset_id = a.id
ORDER BY a.symbol, p.timestamp DESC;

-- Price history for one asset
SELECT
    p.timestamp,
    p.price_usd
FROM prices p
JOIN assets a ON p.asset_id = a.id
WHERE a.symbol = 'bitcoin'
ORDER BY p.timestamp;
