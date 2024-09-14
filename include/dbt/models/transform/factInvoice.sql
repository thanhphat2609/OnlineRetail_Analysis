{{ config(
    materialized='view',
) }}

SELECT 
    InvoiceNo, Quantity, CONVERT(BIGINT, HASHBYTES('SHA2_256', StockCode)) AS Product_key, 
    CONVERT(BIGINT, HASHBYTES('SHA2_256', InvoiceDate)) AS Date_key, CustomerID
-- FROM {{ source('online_retail_stg', 'retail_sales') }}
FROM {{source ('online_retail_test', 'online_retail') }}