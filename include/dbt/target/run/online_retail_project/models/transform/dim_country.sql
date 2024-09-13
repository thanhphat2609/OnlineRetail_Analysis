
  
    

   

    USE [online-retail-kaggle];
    
    

    EXEC('create view "DWH_DWH"."dim_country_temp_view" as 

SELECT
    *
FROM
    "online-retail-kaggle"."dbo"."country";');



    
      EXEC('SELECT * INTO [online-retail-kaggle].[DWH_DWH].[dim_country] FROM [online-retail-kaggle].[DWH_DWH].[dim_country_temp_view];');
    

    
      
      
    
    USE [online-retail-kaggle];
    EXEC('DROP view IF EXISTS "DWH_DWH"."dim_country_temp_view";');



  