# Write your MySQL query statement below

# can't get the expected results for null
SELECT 
    CASE WHEN COUNT(DISTINCT Salary) = 2 THEN MIN(Salary) ELSE NULL END AS SecondHighestSalary
FROM (
    SELECT Salary, RANK() OVER(ORDER BY Salary DESC) AS rnk
    FROM Employee
) AS a   
WHERE rnk<=2
;


# SELECT max(salary) AS SecondHighestSalary
# FROM Employee
# WHERE Salary < (SELECT max(Salary) FROM Employee);

