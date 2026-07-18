CREATE TABLE customers (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name TEXT
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  customer_id INTEGER,
  price INTEGER
);

INSERT INTO customers (name) VALUES
  ('Alice'),
  ('Bob'),
  ('Charlie'),
  ('David'),
  ('Eve'),
  ('Frank'),
  ('Grace'),
  ('Hank');

INSERT INTO orders (customer_id, price) VALUES
  (1, 50),
  (2, 100),
  (3, 150),
  (4, 200),
  (5, 250),
  (6, 30),
  (7, 70),
  (8, 400);
-- Do not modify above this line. --

WITH max_price_orders_under_100 AS (
    SELECT customer_id, MAX(price) as max_price
    FROM orders
    GROUP BY customer_id
    HAVING MAX(price) < 100
)

SELECT name
FROM customers c
JOIN max_price_orders_under_100 AS mpou100 ON c.id = mpou100.customer_id 
ORDER BY name;







