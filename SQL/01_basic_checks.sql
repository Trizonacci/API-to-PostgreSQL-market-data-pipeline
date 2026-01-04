-- View all assets
SELECT * FROM assets;

-- View recent prices
SELECT * FROM prices
ORDER BY timestamp DESC
LIMIT 10;