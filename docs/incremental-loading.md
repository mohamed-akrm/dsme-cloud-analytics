# Incremental Ingestion Strategy & Watermarking

## Architecture & Pattern
- **Pattern:** Watermarking via high-watermark timestamp tracking on `updated_at` column.
- **State Management:** Stored in a Delta Lake control table `watermark_control`.
- **Write Strategy:** Delta Lake `MERGE` (Upsert) keyed on `resource_id` to eliminate duplicates.

## Verification & Idempotency Evidence
- **Initial Load:** Ingested 5,000 resources (Batch 1).
- **Incremental Load:** Ingested 150 delta records (50 updates + 100 inserts). Total count: 5,100.
- **Rerun Test:** Pipeline re-executed with zero duplicate records and zero redundant ingestion.
