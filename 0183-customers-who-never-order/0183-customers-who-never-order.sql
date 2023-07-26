# Write your MySQL query statement below

SELECT customer_name as Customers
FROM
(SELECT c.id as customer_id, c.name as customer_name, o.id as order_id
 FROM Customers c 
 LEFT JOIN Orders o
 ON c.id = o.customerId 
 ) joins
 WHERE joins.order_id is null
 
