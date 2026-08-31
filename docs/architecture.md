# Architecture Overview

## Data Sources
1. **Billing Data (Batch):** CSV files containing monthly cloud costs.
2. **Resource Inventory (Incremental):** REST API (JSON) tracked via `updated_at` watermark.
3. **Telemetry (Streaming):** Simulated Python events for CPU/Memory utilization.

## Ingestion & Processing (Microsoft Fabric)
- **Bronze Layer:** Raw data ingestion (JSON/CSV) without schema enforcement.
- **Silver Layer:** Data quality checks, deduplication, and routing bad records to Quarantine.
- **Gold Layer:** Star schema (Delta tables) with SCD Type 2 for historical resource tracking.
- **Consumption:** Power BI Semantic Model answering cost and utilization queries.