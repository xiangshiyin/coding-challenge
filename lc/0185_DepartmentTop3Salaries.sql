SELECT Department, Employee, Salary
FROM (
    SELECT
      r.Name AS Department
      , l.Name AS Employee
      , l.Salary
      , DENSE_RANK() OVER(PARTITION BY l.DepartmentId ORDER BY l.Salary DESC) AS rnk
    FROM Employee AS l
    JOIN Department AS r ON l.DepartmentId=r.Id
) AS a
WHERE rnk <= 3
;


