
-- Query 1: Customer Purchase History
-- Business Question: "Generate a report for customers with 2+ orders and spent > ₹5,000"
SELECT 
    c.first_name || ' ' || c.last_name AS customer_name, 
    c.email, 
    COUNT(o.order_id) AS total_orders, 
    SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
HAVING total_orders >= 2 AND total_spent > 5000
ORDER BY total_spent DESC;

-- Query 2: Product Sales Analysis
-- Business Question: "Category analysis for revenue > ₹10,000"
SELECT 
    p.category, 
    COUNT(DISTINCT p.product_id) AS num_products, 
    SUM(oi.quantity) AS total_quantity_sold, 
    SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
HAVING total_revenue > 10000
ORDER BY total_revenue DESC;

-- Query 3: Monthly Sales Trend
-- Business Question: "Monthly and Cumulative revenue for 2024"
SELECT 
    strftime('%m', order_date) AS month_num,
    CASE strftime('%m', order_date)
        WHEN '01' THEN 'January' WHEN '02' THEN 'February' WHEN '03' THEN 'March'
        WHEN '04' THEN 'April' WHEN '05' THEN 'May' WHEN '06' THEN 'June'
        WHEN '07' THEN 'July' WHEN '08' THEN 'August' WHEN '09' THEN 'September'
        WHEN '10' THEN 'October' WHEN '11' THEN 'November' WHEN '12' THEN 'December'
    END AS month_name,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS monthly_revenue,
    SUM(SUM(total_amount)) OVER (ORDER BY strftime('%m', order_date)) AS cumulative_revenue
FROM orders
WHERE strftime('%Y', order_date) = '2024'
GROUP BY month_num
ORDER BY month_num ASC;
