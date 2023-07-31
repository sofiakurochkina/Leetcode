# Write your MySQL query statement below

SELECT 
v.customer_id,
count(*) AS count_no_trans
FROM Visits AS v 
LEFT JOIN Transactions AS t
ON v.visit_id=t.visit_id
WHERE t.transaction_id is null
GROUP BY customer_id