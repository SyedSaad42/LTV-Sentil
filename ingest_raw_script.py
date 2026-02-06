import pandas as pd
import random
from datetime import datetime, timedelta

def generate_daily_batch(date):
    """Simulates raw API data for a specific date."""
    user_ids = range(100, 150)
    event_types = ['signup', 'upgrade', 'downgrade', 'churn']
    plans = ['Basic', 'Pro', 'Enterprise']
    
    data = []
    for _ in range(20):  # 20 events per day
        data.append({
            'event_id': random.randint(1000, 9999),
            'customer_id': random.choice(user_ids),
            'event_type': random.choice(event_types),
            'plan_name': random.choice(plans),
            'amount': random.choice([10, 50, 200]),
            'event_timestamp': date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return pd.DataFrame(data)

# Execution
today = datetime.now()
df = generate_daily_batch(today)
filename = f"raw_sub_events_{today.strftime('%Y%m%d')}.csv"
df.to_csv(f"ingestion/{filename}", index=False)
print(f"✅ Bronze Layer: {filename} created successfully.")