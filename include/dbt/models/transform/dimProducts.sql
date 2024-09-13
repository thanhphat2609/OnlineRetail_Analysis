{{ config(
    materialized='table',
) }}

SELECT DISTINCT StockCode, Description, UnitPrice, 
       CONVERT(BIGINT, HASHBYTES('SHA2_256', StockCode)) AS Product_key
FROM {{source ('online_retail_stg', 'retail_sales') }}
WHERE StockCode IS NOT NULL 