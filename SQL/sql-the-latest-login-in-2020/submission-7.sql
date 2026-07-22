SELECT
    l.user_id,
    MAX(l.time_stamp) AS last_stamp
FROM logins l
WHERE EXTRACT(YEAR FROM CAST(time_stamp AS TIMESTAMP)) = 2020
GROUP BY l.user_id;