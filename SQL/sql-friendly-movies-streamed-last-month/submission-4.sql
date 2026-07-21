SELECT DISTINCT c.title
FROM content c
JOIN tv_program tp ON c.content_id = tp.content_id
WHERE
    c.content_type = 'Movies' AND
    c.kids_content = 'Y' AND
    EXTRACT(YEAR FROM CAST(tp.program_date AS TIMESTAMP)) = 2020 AND
    EXTRACT(MONTH FROM CAST(tp.program_date AS TIMESTAMP)) = 06;