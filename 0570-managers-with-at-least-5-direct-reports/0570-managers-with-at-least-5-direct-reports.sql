SELECT m1.name
FROM Employee m
JOIN Employee m1
    ON m.managerId = m1.id
GROUP BY m1.id, m1.name
HAVING COUNT(m.id) >= 5;