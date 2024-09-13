
  
    

   

    USE [online-retail-kaggle];
    
    

    EXEC('create view "DWH"."dimProducts_temp_view" as 

SELECT DISTINCT StockCode, Description, UnitPrice, 
       CONVERT(BIGINT, HASHBYTES(''SHA2_256'', @StockCode)) AS Product_key
FROM "online-retail-kaggle"."STG"."retail_sales"
WHERE StockCode IS NOT NULL;');



    
      EXEC('SELECT * INTO [online-retail-kaggle].[DWH].[dimProducts] FROM [online-retail-kaggle].[DWH].[dimProducts_temp_view];');
    

    
      
      
    
    USE [online-retail-kaggle];
    EXEC('DROP view IF EXISTS "DWH"."dimProducts_temp_view";');



  