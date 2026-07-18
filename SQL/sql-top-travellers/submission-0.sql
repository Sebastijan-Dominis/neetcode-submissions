-- Write your query below

SELECT 
    u.name, 
    CASE
        WHEN tds.td IS NOT NULL THEN tds.td
        ELSE 0
    END AS travelled_distance
FROM users u
LEFT JOIN (
    SELECT SUM(distance) as td, user_id
    FROM rides
    GROUP BY user_id
) AS tds ON u.id = tds.user_id
ORDER BY travelled_distance DESC, u.name;