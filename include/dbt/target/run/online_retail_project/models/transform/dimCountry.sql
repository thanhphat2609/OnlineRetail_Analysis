USE [online-retail-kaggle];
    
    

    

    
    USE [online-retail-kaggle];
    EXEC('
        create view "DWH"."dimCountry__dbt_tmp" as 

SELECT
    *
FROM
    "online-retail-kaggle"."dbo"."country";
    ')

