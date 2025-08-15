SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
	SUM(order_price) AS monthly_sales
FROM sales_db.sales
GROUP BY month
ORDER BY month;
