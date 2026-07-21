SELECT
    u.name,
    SUM(amount) AS balance
FROM users u
JOIN transactions t ON u.account = t.account
GROUP BY u.account, u.name
HAVING SUM(amount) > 10000;