import json
import random
from datetime import datetime, timedelta

def generate_resources():
    resource_types = ['Virtual Machine', 'SQL Database', 'Storage Account', 'Kubernetes Cluster']
    statuses = ['Running', 'Stopped', 'Deallocated']
    
    # Batch 1: Initial load (Base data at 08:00 AM)
    base_time = datetime(2026, 9, 1, 8, 0, 0)
    batch_1 = []
    for i in range(1, 5001):
        batch_1.append({
            "resource_id": f"res-{i:05d}",
            "tenant_id": f"tenant-{random.randint(1, 85):03d}",
            "resource_type": random.choice(resource_types),
            "status": random.choice(statuses),
            "region": "ME-South",
            "updated_at": (base_time + timedelta(minutes=random.randint(0, 60))).strftime("%Y-%m-%d %H:%M:%S")
        })

    with open('sample-data/raw/resources_batch_1.json', 'w') as f:
        json.dump(batch_1, f, indent=2)

    # Batch 2: Incremental updates & new inserts (after 10:00 AM)
    inc_time = datetime(2026, 9, 1, 10, 0, 0)
    batch_2 = []
    # 50 updated records (existing resources)
    for i in range(1, 51):
        batch_2.append({
            "resource_id": f"res-{i:05d}",
            "tenant_id": f"tenant-{random.randint(1, 85):03d}",
            "resource_type": random.choice(resource_types),
            "status": "Stopped", # Changed status
            "region": "ME-South",
            "updated_at": (inc_time + timedelta(minutes=random.randint(1, 30))).strftime("%Y-%m-%d %H:%M:%S")
        })
    # 100 new resources
    for i in range(5001, 5101):
        batch_2.append({
            "resource_id": f"res-{i:05d}",
            "tenant_id": f"tenant-{random.randint(1, 85):03d}",
            "resource_type": random.choice(resource_types),
            "status": "Running",
            "region": "ME-South",
            "updated_at": (inc_time + timedelta(minutes=random.randint(1, 30))).strftime("%Y-%m-%d %H:%M:%S")
        })

    with open('sample-data/raw/resources_batch_2.json', 'w') as f:
        json.dump(batch_2, f, indent=2)

    print("Resource batches generated successfully in sample-data/raw/!")

if __name__ == "__main__":
    generate_resources()
