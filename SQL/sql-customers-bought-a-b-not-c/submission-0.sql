-- Write your query below

WITH bought_a AS (
    SELECT DISTINCT customer_id
    FROM orders
    WHERE product_name = 'A'
),

bought_b AS (
    SELECT DISTINCT customer_id
    FROM orders
    WHERE product_name = 'B'
),

did_not_buy_c AS (
    SELECT DISTINCT customer_id
    FROM customers c
    WHERE NOT EXISTS (
        SELECT 1
        FROM orders o
        WHERE c.customer_id = o.customer_id AND product_name = 'C'
    )
)

SELECT c.customer_id, c.customer_name
FROM customers c
JOIN bought_a A ON c.customer_id = A.customer_id
JOIN bought_b B ON c.customer_id = B.customer_id
JOIN did_not_buy_c NO_C ON c.customer_id = NO_C.customer_id
ORDER BY c.customer_name;