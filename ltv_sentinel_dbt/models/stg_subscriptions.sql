# -- Ensure this file is executed within dbt, or replace dbt-specific syntax with standard SQL.
# -- dbt config(materialized='view')

# -- This tells dbt to build this as a view in BigQuery
{{ config(materialized='view') }}
# using this we got all the field we need to work on the gold stage and we can also do some transformation here if needed
SELECT
    sub_id,
    customer_id,
    status,
    plan_name,
    round(monthly_amount_cents / 100, 2) as monthly_revenue_usd,
    date(period_start_ts) as start_date
-- IMPORTANT: Use the source function here
FROM {{ source('stripe_source', 'stripe_raw_subs') }}