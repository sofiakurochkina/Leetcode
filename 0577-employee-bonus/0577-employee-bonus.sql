# Write your MySQL query statement below

SELECT 
t1.name,
t2.bonus
FROM Employee AS t1
LEFT JOIN Bonus AS t2
ON t1.empId=t2.empId
WHERE bonus IS NULL or bonus < 1000