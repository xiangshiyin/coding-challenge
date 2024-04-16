SELECT
    l.Name AS Employee
FROM Employee AS l
JOIN Employee AS r ON l.ManagerId=r.Id
WHERE l.Salary > r.Salary
;
