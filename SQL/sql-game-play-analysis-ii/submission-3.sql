SELECT a.player_id, a.device_id
FROM activity a
INNER JOIN (
    SELECT player_id, MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id
) AS fl ON a.player_id = fl.player_id AND a.event_date = fl.first_login;