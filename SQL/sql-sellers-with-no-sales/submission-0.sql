-- Write your query below
SELECT seller_name
FROM seller s
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE s.seller_id = o.seller_id AND o.sale_date > '2019-12-31' AND o.sale_date < '2021-01-01'
)
ORDER BY seller_name;