SELECT
  t.Request_at AS Day
  , ROUND(SUM(CASE WHEN t.Status IN ('cancelled_by_driver','cancelled_by_client') THEN 1 ELSE 0 END) / COUNT(*),2) AS "Cancellation Rate"
FROM Trips AS t
JOIN Users AS u1 on t.Client_Id=u1.Users_Id
JOIN Users AS u2 on t.Driver_Id=u2.Users_Id
WHERE u1.Banned='No' AND u2.Banned='No' AND t.Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY 1
;

