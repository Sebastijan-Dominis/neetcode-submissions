SELECT COALESCE(e.employee_id, s.employee_id) AS employee_id
FROM employees e
FULL JOIN salaries s ON e.employee_id = s.employee_id
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id;