{{ config(
    materialized='view',
) }}

SELECT
    *
FROM
    {{ source('online_retail', 'country') }}