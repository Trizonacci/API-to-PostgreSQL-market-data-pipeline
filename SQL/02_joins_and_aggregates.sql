-- Join prices with assets
SELECT
    a.symbol,
    p.price_usd,
    p.timestamp
FROM prices p
JOIN assets a ON p.asset_id = a.id
ORDER BY p.timestamp DESC;

-- Average price per asset
SELECT
    a.symbol,
    AVG(p.price_usd) AS avg_price
FROM prices p
JOIN assets a ON p.asset_id = a.id
GROUP BY a.symbol;
