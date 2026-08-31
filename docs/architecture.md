# Architecture Overview
1. **Bronze Layer:** Raw data ingestion (CSV via Batch).
2. **Silver Layer:** PySpark Data Quality checks and quarantine routing.
3. **Gold Layer:** Star schema with SCD Type 2.