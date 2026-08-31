# Data Quality Rules
- `tenant_id` must not be null.
- `cost_usd` must be >= 0.
Failed records are routed to a quarantine table.

