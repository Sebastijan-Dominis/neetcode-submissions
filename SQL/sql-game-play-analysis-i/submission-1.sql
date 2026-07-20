SELECT DISTINCT ON (player_id)
    player_id,
    event_date AS first_login
FROM activity
ORDER BY player_id, event_date