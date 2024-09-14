{{ config(
    materialized='view',
) }}

-- Create a CTE to extract date and time components
WITH datetime_cte AS (
  SELECT DISTINCT
    InvoiceDate,
    CASE
      WHEN LEN(InvoiceDate) = 16 THEN
        -- Date format: "DD/MM/YYYY HH:MM"
        TRY_CAST(InvoiceDate AS DATETIME)
      WHEN LEN(InvoiceDate) <= 14 THEN
        -- Date format: "MM/DD/YY HH:MM"
        TRY_CAST(InvoiceDate AS DATETIME)
      ELSE
        NULL
    END AS date_part
  -- Replace the table name accordingly
  -- FROM {{source ('online_retail_stg', 'retail_sales') }}
  FROM {{source ('online_retail_test', 'online_retail') }}
  WHERE InvoiceDate IS NOT NULL
)
SELECT
  InvoiceDate,
  CONVERT(BIGINT, HASHBYTES('SHA2_256', InvoiceDate)) AS Date_key,
  date_part as datetime,
  YEAR(date_part) AS year,
  MONTH(date_part) AS month,
  DAY(date_part) AS day,
  DATEPART(HOUR, date_part) AS hour,
  DATEPART(MINUTE, date_part) AS minute,
  DATEPART(WEEKDAY, date_part) AS weekday
FROM datetime_cte;