# Write your MySQL query statement below

SELECT 
Register.contest_id AS contest_id,
ROUND(COUNT(*)/ (SELECT COUNT(*) FROM Users) * 100,2) AS percentage 
FROM Register LEFT JOIN Users
ON Register.user_id = Users.user_id
GROUP BY Register.contest_id
ORDER BY percentage DESC, contest_id ASC