SELECT s.id, s.name
FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM departments d
    WHERE s.department_id = d.id
);