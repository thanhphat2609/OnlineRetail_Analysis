

-- Create a CTE to extract date and time components
WITH datetime_cte AS (  
  SELECT DISTINCT
    InvoiceDate,
    CASE
      WHEN LENGTH(InvoiceDate) = 16 THEN
        -- Date format: "DD/MM/YYYY HH:MM"
        PARSE_DATETIME('%m/%d/%Y %H:%M', InvoiceDate)
      WHEN LENGTH(InvoiceDate) <= 14 THEN
        -- Date format: "MM/DD/YY HH:MM"
        PARSE_DATETIME('%m/%d/%y %H:%M', InvoiceDate)
      ELSE
        NULL
    END AS date_part,
  -- FROM "online-retail-kaggle"."STG"."retail_sales"
  FROM "online-retail-kaggle"."dbo"."online_retail"
  WHERE InvoiceDate IS NOT NULL
)
SELECT
  InvoiceDate,
  CONVERT(BIGINT, HASHBYTES('SHA2_256', InvoiceDate)) AS Date_key,
  date_part as datetime,
  EXTRACT(YEAR FROM date_part) AS year,
  EXTRACT(MONTH FROM date_part) AS month,
  EXTRACT(DAY FROM date_part) AS day,
  EXTRACT(HOUR FROM date_part) AS hour,
  EXTRACT(MINUTE FROM date_part) AS minute,
  EXTRACT(DAYOFWEEK FROM date_part) AS weekday
FROM datetime_cte