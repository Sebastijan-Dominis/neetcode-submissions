SELECT employee_id
FROM employees e WHERE NOT EXISTS (
    SELECT 1
    FROM salaries s
    WHERE e.employee_id = s.employee_id
)
UNION
SELECT employee_id
FROM salaries s WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    WHERE s.employee_id = e.employee_id
)
ORDER BY employee_id;