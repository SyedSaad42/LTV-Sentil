# LTV-Sentil
LTV Sentinel: Predictive Revenue & Churn Platform
LTV Sentinel is an end-to-end (E2E) data platform that transforms raw subscription logs into actionable Customer Lifetime Value (LTV) insights. Built with a data-centric approach, it utilizes a "Sentinel" logic layer to proactively identify high-churn-risk cohorts before revenue loss occurs.

🚀 The Pipeline Flow
Ingest: A Python-based "Continuous Caller" fetches daily transaction and event logs from REST APIs.

Load: Data is streamed into a Cloud Data Warehouse (Snowflake/BigQuery) using a Medallion Architecture.

Transform: dbt models apply business logic to calculate MRR, Churn, and LTV.

Sentinel Logic: Implements SCD Type 2 to track customer lifecycle changes and triggers alerts for data anomalies or "Ghost Churn."

Visualize: A real-time Streamlit app provides executive-level drill-downs into cohort health.

🛠️ Tech Stack (The Modern Data Stack)
Language: Python 3.12 (Requests, Pandas, Pytest)

Orchestration: GitHub Actions (Automated CI/CD & Pipeline Scheduling)

Warehouse: Snowflake / Google BigQuery

Transformation: dbt Core (SQL Modeling & Testing)

Infrastructure: Terraform (Infrastructure as Code)

Observability: dbt-tests & Great Expectations

📊 Advanced Analyst Features
Predictive LTV Modeling: Uses historical cohort behavior to forecast future revenue.

Automated Data Contracts: Ensures the pipeline fails gracefully if API schemas change, preventing "Bad Data" from reaching the dashboard.

Churn Risk Scoring: A custom logic gate that flags users based on declining engagement velocity.
