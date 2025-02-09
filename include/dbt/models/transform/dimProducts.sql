{{ config(
    materialized='view',
) }}

SELECT DISTINCT StockCode, Description, UnitPrice, 
       CONVERT(BIGINT, HASHBYTES('SHA2_256', StockCode)) AS Product_key
-- FROM {{source ('online_retail_stg', 'retail_sales') }}
FROM {{source ('online_retail_test', 'online_retail') }}
WHERE StockCode IS NOT NULL 