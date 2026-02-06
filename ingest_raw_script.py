import pandas as pd
from google.cloud import bigquery
import random
from datetime import datetime

def get_stripe_data():
    """Simulates raw Stripe API response and flattens it."""
    data = []
    for _ in range(10):
        data.append({
            'sub_id': f"sub_{random.randint(1000, 9999)}",
            'customer_id': f"cus_{random.randint(100, 500)}",
            'status': random.choice(['active', 'canceled', 'past_due']),
            'plan_name': random.choice(['Basic', 'Pro', 'Enterprise']),
            'monthly_amount_cents': random.choice([1000, 5000, 20000]),
            'period_start_ts': datetime.now(),
            'ingested_at': datetime.now()
        })
    return pd.DataFrame(data)

def upload_to_bigquery(df):
    # This automatically uses the GCP_SA_KEY secret from GitHub Actions
    client = bigquery.Client()
    
    # Update this with your actual Project ID from Google Cloud
    table_id = "ltv-sentinel-project.ltv_sentinel_bronze.stripe_raw_subs"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND", # This keeps historical data
    )

    print(f"🚀 Sentinel: Uploading {len(df)} rows to BigQuery...")
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result() 
    print("✅ Success: Data is now in the Bronze Layer.")

if __name__ == "__main__":
    df = get_stripe_data()
    upload_to_bigquery(df)