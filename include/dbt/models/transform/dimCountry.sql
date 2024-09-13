{{ config(
    materialized='table',
) }}

SELECT
    *
FROM
    {{ source('online_retail', 'country') }}