-- # Write your MySQL query statement below

SELECT *
FROM (
    SELECT employee_id
    FROM Employees
    WHERE employee_id != 1 AND manager_id=1

    UNION

    SELECT l.employee_id
    FROM Employees AS l
    JOIN Employees AS r ON l.manager_id=r.employee_id
    WHERE l.employee_id != 1 AND r.manager_id=1

    UNION

    SELECT l.employee_id
    FROM Employees AS l
    JOIN Employees AS m ON l.manager_id=m.employee_id
    JOIN Employees AS r ON m.manager_id=r.employee_id
    WHERE l.employee_id != 1 AND r.manager_id=1
) AS a
;


