{{ config(materialized='table') }} -- This tells dbt to build this as a table in BigQuery

-- here we are calculating the tenure in months and the realized LTV for each active subscription. The tenure is calculated as the difference in months between the current date and the start date of the subscription, plus one to include the current month. The realized LTV is calculated by multiplying the monthly revenue by the tenure in months.
SELECT
    *,
    date_diff(current_date(), start_date, month) + 1 as tenure_months,
    monthly_revenue_usd * (date_diff(current_date(), start_date, month) + 1) as realized_ltv_usd
-- IMPORTANT: Use the ref function here
FROM {{ ref('stg_subscriptions') }}
WHERE status = 'active'