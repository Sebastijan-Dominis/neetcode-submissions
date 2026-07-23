SELECT s.id, s.name
FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM departments d
    WHERE d.id = s.department_id
);