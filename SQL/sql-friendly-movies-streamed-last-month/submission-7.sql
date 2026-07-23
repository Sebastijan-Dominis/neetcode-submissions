SELECT DISTINCT c.title
FROM tv_program tp
JOIN content c ON tp.content_id = c.content_id
WHERE
    EXTRACT(YEAR FROM CAST(tp.program_date AS TIMESTAMP)) = 2020 AND
    EXTRACT(MONTH FROM CAST(tp.program_date AS TIMESTAMP)) = 06 AND
    c.kids_content = 'Y' AND
    c.content_type = 'Movies';