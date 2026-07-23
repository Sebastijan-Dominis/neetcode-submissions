SELECT DISTINCT p.email
FROM person p
JOIN (
    SELECT
        email,
        COUNT(*)
    FROM person
    GROUP BY email
    HAVING COUNT(*) > 1
) AS c ON p.email = c.email;