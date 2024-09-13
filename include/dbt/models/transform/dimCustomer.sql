{{ config(
    materialized='table',
) }}

SELECT DISTINCT CustomerID, Country
FROM {{source ('online_retail_stg', 'retail_sales') }}
WHERE CustomerID IS NOT NULL 