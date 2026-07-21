SELECT id, name
FROM students s
WHERE department_id IS NULL OR NOT EXISTS (
    SELECT 1
    FROM departments d
    WHERE d.id = s.department_id
)