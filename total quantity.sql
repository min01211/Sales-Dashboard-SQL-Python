SELECT 
	order_product,
    SUM(order_qty) AS total_qty
FROM sales_db.sales
GROUP BY order_product