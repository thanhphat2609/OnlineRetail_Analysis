

SELECT DISTINCT StockCode, Description, UnitPrice, 
       CONVERT(BIGINT, HASHBYTES('SHA2_256', StockCode)) AS Product_key
-- FROM "online-retail-kaggle"."STG"."retail_sales"
FROM "online-retail-kaggle"."dbo"."online_retail"
WHERE StockCode IS NOT NULL