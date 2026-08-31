import csv
import random
from datetime import datetime, timedelta

# Company Stats Mapped to our Data
NUM_TENANTS = 85 # Matches "75+ Happy Customers"
COUNTRIES = ['Egypt', 'KSA', 'UAE', 'USA', 'UK', 'Germany', 'France', 'Canada', 'Australia', 'Japan', 'India', 'Brazil'] # Matches "12+ Countries"
SERVICES = ['Compute', 'Storage', 'Database', 'Network', 'Analytics']

# 1. Generate Tenants
tenants = []
print("Generating Tenants...")
with open('sample-data/raw/cloud_tenants.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['tenant_id', 'tenant_name', 'subscription_plan', 'region', 'status'])
    for i in range(1, NUM_TENANTS + 1):
        t_id = f"T-{1000 + i}"
        plan = random.choice(['Basic', 'Pro', 'Enterprise'])
        region = random.choice(COUNTRIES)
        status = random.choices(['Active', 'Inactive'], weights=[0.9, 0.1])[0] # 90% active
        tenants.append(t_id)
        writer.writerow([t_id, f"Client_{i}_Corp", plan, region, status])

# 2. Generate Billing Data (Batch) with Intentional Errors for DQ
NUM_BILLS = 50000 # Large volume for realistic testing
print(f"Generating {NUM_BILLS} Billing Records...")

start_date = datetime(2026, 1, 1)

with open('sample-data/raw/cloud_billing.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['invoice_id', 'tenant_id', 'service_category', 'cost_usd', 'compute_hours', 'billing_date'])
    
    for i in range(1, NUM_BILLS + 1):
        inv_id = f"INV-{100000 + i}"
        t_id = random.choice(tenants)
        service = random.choice(SERVICES)
        
        # Simulate massive compute hours (to align with 1,065,000+ hours stat)
        hours = round(random.uniform(10, 500), 2)
        cost = round(hours * random.uniform(0.5, 5.0), 2)
        
        b_date = start_date + timedelta(days=random.randint(0, 240)) # Random date in 2026
        
        # INTENTIONAL BAD DATA FOR DATA QUALITY CHECKS (Requirement 5)
        error_chance = random.random()
        if error_chance < 0.01:
            cost = -cost # Negative cost error
        elif error_chance < 0.02:
            t_id = "" # Null tenant error
        elif error_chance < 0.03:
            service = "UnknownService" # Invalid category error
            
        writer.writerow([inv_id, t_id, service, cost, hours, b_date.strftime('%Y-%m-%d')])

print("Data generation complete! Files saved in sample-data/raw/")
