SELECT user_id, MAX(time_stamp) AS last_stamp
FROM logins
WHERE EXTRACT(YEAR FROM CAST(time_stamp AS TIMESTAMP)) = 2020
GROUP BY user_id;