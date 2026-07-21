SELECT DISTINCT seat_id
FROM cinema c
WHERE 1 = ANY (
    SELECT free
    FROM cinema
    WHERE (seat_id = c.seat_id-1) OR (seat_id = c.seat_id+1)
) AND free = 1