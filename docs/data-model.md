# Gold Layer Star Schema & Data Model

## Overview
The Gold layer implements a dimensional model (Star Schema) designed for FinOps and cloud cost analytics.

## Fact Tables

### `fact_billing`
- **Description:** Granular cloud resource billing records.
- **Grain:** One record per billing transaction per cloud service.
- **Columns:**
  - `invoice_id` (STRING): Natural invoice identifier.
  - `tenant_key` (BIGINT): Surrogate foreign key linking to `dim_tenant`.
  - `service_category` (STRING): Cloud service type (Compute, Storage, Network, Database).
  - `cost_usd` (DOUBLE): Monetary cost charged.
  - `compute_hours` (DOUBLE): Consumed hours.
  - `billing_date` (DATE): Transaction date.

## Dimension Tables

### `dim_tenant`
- **Description:** Dimension containing customer/tenant profile data.
- **SCD Strategy:** Implements Slowly Changing Dimension (SCD Type 2 ready with status tracking).
- **Columns:**
  - `tenant_key` (BIGINT): Surrogate primary key.
  - `tenant_id` (STRING): Business natural key.
  - `subscription_plan` (STRING): Tier level (e.g., Enterprise).
  - `region` (STRING): Deployment region.
  - `is_current` (BOOLEAN): Current active record indicator.
