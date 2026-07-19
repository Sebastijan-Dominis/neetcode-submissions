SELECT user_id, MAX(time_stamp) as last_stamp
FROM logins
WHERE time_stamp LIKE '2020%'
GROUP BY user_id;