-- SELECT
--   CASE WHEN max(rnk)=N THEN min(Salary) ELSE NULL END AS Salary
-- FROM (
--     SELECT 
--       Salary
--       , DENSE_RANK() OVER(ORDER BY Salary DESC) AS rnk
--     FROM Employee
-- ) AS a 
-- WHERE rnk <= N      
-- ;

SELECT
  DISTINCT Salary
FROM (
  SELECT 
    Salary
    , DENSE_RANK() OVER(ORDER BY Salary DESC) AS rnk
  FROM Employee
) AS a 
WHERE rnk = N     
;

