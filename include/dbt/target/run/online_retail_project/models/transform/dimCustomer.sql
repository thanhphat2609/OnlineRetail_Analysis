USE [online-retail-kaggle];
    
    

    

    
    USE [online-retail-kaggle];
    EXEC('
        create view "DWH"."dimCustomer__dbt_tmp" as 

SELECT DISTINCT CustomerID, Country
-- FROM "online-retail-kaggle"."STG"."retail_sales"
FROM "online-retail-kaggle"."dbo"."online_retail"
WHERE CustomerID IS NOT NULL;
    ')

