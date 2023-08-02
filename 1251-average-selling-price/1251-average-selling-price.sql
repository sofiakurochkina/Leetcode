# Write your MySQL query statement below

SELECT 
Prices.product_id,
ROUND(SUM(Prices.price*UnitsSold.units)/SUM(UnitsSold.units),2) as average_price
FROM Prices
JOIN UnitsSold
ON Prices.product_id = UnitsSold.product_id
WHERE UnitsSold.purchase_date >= Prices.start_date
AND UnitsSold.purchase_date <= Prices.end_date
GROUP BY Prices.product_id