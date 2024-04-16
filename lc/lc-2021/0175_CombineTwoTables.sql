# Write your MySQL query statement below

SELECT l.FirstName, l.LastName, r.City, r.State
FROM Person AS l
LEFT JOIN Address AS r ON l.PersonId=r.PersonId;
