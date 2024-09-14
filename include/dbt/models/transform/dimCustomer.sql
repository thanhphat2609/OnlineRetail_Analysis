{{ config(
    materialized='view',
) }}

SELECT DISTINCT CustomerID, Country
-- FROM {{source ('online_retail_stg', 'retail_sales') }}
FROM {{source ('online_retail_test', 'online_retail') }}
WHERE CustomerID IS NOT NULL 