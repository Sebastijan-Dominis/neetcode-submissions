SELECT s.seller_name
FROM seller s
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE s.seller_id = o.seller_id AND
    EXTRACT(YEAR FROM o.sale_date) = 2020
)
ORDER BY s.seller_name;