# Write your MySQL query statement below


SELECT 
case when count(*) = 1 then num else null end as 'num'
FROM MyNumbers
GROUP BY num
ORDER BY num DESC
LIMIT 1
