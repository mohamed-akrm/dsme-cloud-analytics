# Data Quality Rules
- `tenant_id` must not be null.
- `cost_usd` must be >= 0.
Failed records are routed to a quarantine table.

## Data Quality Execution Results
- Total Ingested: 50,000
- Passed to Silver: 49,002
- Quarantined (Anomalies caught): 998