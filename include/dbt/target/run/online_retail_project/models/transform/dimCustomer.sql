
  
    

   

    USE [online-retail-kaggle];
    
    

    EXEC('create view "DWH"."dimCustomer_temp_view" as 

SELECT DISTINCT CustomerID, Country
FROM "online-retail-kaggle"."STG"."retail_sales"
WHERE CustomerID IS NOT NULL;');



    
      EXEC('SELECT * INTO [online-retail-kaggle].[DWH].[dimCustomer] FROM [online-retail-kaggle].[DWH].[dimCustomer_temp_view];');
    

    
      
      
    
    USE [online-retail-kaggle];
    EXEC('DROP view IF EXISTS "DWH"."dimCustomer_temp_view";');



  