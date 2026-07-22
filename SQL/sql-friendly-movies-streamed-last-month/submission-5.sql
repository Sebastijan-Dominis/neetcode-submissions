SELECT DISTINCT c.title
FROM tv_program tp
JOIN content c ON tp.content_id = c.content_id
WHERE
    c.content_type = 'Movies' AND
    c.kids_content = 'Y' AND
    EXTRACT(YEAR FROM CAST(program_date AS TIMESTAMP)) = 2020 AND
    EXTRACT(MONTH FROM CAST(program_date AS TIMESTAMP)) = 06;