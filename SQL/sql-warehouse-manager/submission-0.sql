SELECT
    w.name AS warehouse_name,
    COALESCE(SUM(w.units * p.width * p.length * p.height), 0) AS volume
FROM warehouse w
JOIN products p ON w.product_id = p.product_id
GROUP BY w.name;