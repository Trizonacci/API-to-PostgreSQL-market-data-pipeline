# API → PostgreSQL Market Data Pipeline

## Overview

This project implements an end-to-end data pipeline that fetches real-time market data from an external API, validates and normalizes the response in Python, and stores the results in a PostgreSQL database for structured querying and analysis.

The goal of this project is to demonstrate practical backend and data skills commonly required in SaaS, automation, data engineering, and junior backend roles.

---

## Tech Stack

- Python 3
- Requests (API calls)
- PostgreSQL
- psycopg2
- pgAdmin 4
- CoinGecko API (market data source)

---

### Project Structure

<pre>
API-to-PostgreSQL-market-data-pipeline/
├── src/
│   ├── main.py              # Pipeline entry point
│   ├── fetch_prices.py      # API fetching & data normalization
│   ├── db.py                # Database connection & inserts
│   ├── config.example.py    # Configuration template
│   └── config.local.py      # Local credentials (gitignored)
├── SQL/
│   ├── 01_basic_checks.sql
│   ├── 02_joins_and_aggregates.sql
│   └── 03_analysis_examples.sql
├── requirements.txt
└── README.md
</pre>


## Data Flow

1. Fetch live price data from an external REST API
2. Validate and normalize raw JSON responses
3. Ensure asset records exist in the database
4. Insert normalized price data into PostgreSQL
5. Query stored data using SQL joins and aggregations

This layered approach mirrors how real production systems are built and debugged.

---

## Database Schema

### assets

| column | type | description |
|------|------|-------------|
| id | integer | primary key |
| symbol | text | unique asset identifier |
| name | text | optional descriptive name |

### prices

| column | type | description |
|------|------|-------------|
| id | integer | primary key |
| asset_id | integer | foreign key → assets.id |
| price_usd | numeric | validated price value |
| timestamp | timestamp | ingestion time |

---

## Example SQL Queries

This project includes example SQL queries demonstrating:

- Joining relational tables (`assets` ↔ `prices`)
- Aggregations (average price per asset)
- Time-series analysis (latest price, price history)

All example queries are stored in the `/SQL` directory.

---

## Setup

1. Create a PostgreSQL database named `market_data`
2. Create tables using the provided schema
3. Copy the config template:
   ```bash
   cp src/config.example.py 