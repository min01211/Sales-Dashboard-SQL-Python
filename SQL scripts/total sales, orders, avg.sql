SELECT
	SUM(order_price) AS total_sales,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(order_price) / COUNT(DISTINCT order_id), 2) AS avg_order_value
FROM sales_db.sales;