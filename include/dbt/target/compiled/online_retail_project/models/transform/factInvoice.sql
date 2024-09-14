

SELECT 
    InvoiceNo, Quantity, CONVERT(BIGINT, HASHBYTES('SHA2_256', StockCode)) AS Product_key, 
    CONVERT(BIGINT, HASHBYTES('SHA2_256', InvoiceDate)) AS Date_key, CustomerID
-- FROM "online-retail-kaggle"."STG"."retail_sales"
FROM "online-retail-kaggle"."dbo"."online_retail"