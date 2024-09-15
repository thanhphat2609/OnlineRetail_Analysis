-- Invoice by Year
SELECT d.year,  COUNT(DISTINCT InvoiceNo) 'TotalInvoice'
FROM factInvoice f INNER JOIN dimDateTime d ON f.Date_key = d.Date_key
GROUP BY d.year

-- Invoice by WeekDay
SELECT 
    CASE 
        WHEN d.weekday = 1 THEN 'Monday'
        WHEN d.weekday = 2 THEN 'Tuesday'
        WHEN d.weekday = 3 THEN 'Wednesday'
        WHEN d.weekday = 4 THEN 'Thursday'
        WHEN d.weekday = 5 THEN 'Friday'
        WHEN d.weekday = 6 THEN 'Saturday'
        ELSE 'Invalid Day'
    END AS WeekDay,  
    COUNT(DISTINCT InvoiceNo) AS TotalInvoice
FROM factInvoice f 
INNER JOIN dimDateTime d ON f.Date_key = d.Date_key
GROUP BY d.weekday

-- Total Invoice by Month
SELECT 
    CASE 
        WHEN d.month = 1 THEN 'Jan'
        WHEN d.month = 2 THEN 'Feb'
        WHEN d.month = 3 THEN 'Mar'
        WHEN d.month = 4 THEN 'Apr'
        WHEN d.month = 5 THEN 'May'
        WHEN d.month = 6 THEN 'Jun'
        WHEN d.month = 7 THEN 'Jul'
        WHEN d.month = 8 THEN 'Aug'
        WHEN d.month = 9 THEN 'Sep'
        WHEN d.month = 10 THEN 'Oct'
        WHEN d.month = 11 THEN 'Nov'
        WHEN d.month = 12 THEN 'Dec'
    END AS Month, d.month AS Month_Sort,
    COUNT(DISTINCT InvoiceNo) AS TotalInvoice
FROM factInvoice f 
INNER JOIN dimDateTime d ON f.Date_key = d.Date_key
GROUP BY d.month


