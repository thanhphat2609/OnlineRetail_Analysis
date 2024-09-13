
  
    

   

    USE [online-retail-kaggle];
    
    

    EXEC('create view "DWH"."dimCountry_temp_view" as 

SELECT
    *
FROM
    "online-retail-kaggle"."dbo"."country";');



    
      EXEC('SELECT * INTO [online-retail-kaggle].[DWH].[dimCountry] FROM [online-retail-kaggle].[DWH].[dimCountry_temp_view];');
    

    
      
      
    
    USE [online-retail-kaggle];
    EXEC('DROP view IF EXISTS "DWH"."dimCountry_temp_view";');



  