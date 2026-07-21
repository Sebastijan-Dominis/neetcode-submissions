SELECT DISTINCT c.title
FROM content c
JOIN tv_program tp on c.content_id = tp.content_id
WHERE
    tp.program_date LIKE '2020-06%' AND
    c.kids_content = 'Y' AND
    c.content_type = 'Movies';