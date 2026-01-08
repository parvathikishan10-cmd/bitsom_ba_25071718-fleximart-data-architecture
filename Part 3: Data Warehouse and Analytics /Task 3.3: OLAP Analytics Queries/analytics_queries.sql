-- Task 3.3: OLAP Analytics Queries
-- Database: fleximart_dw

-- Query 1: Monthly Sales Drill-Down Analysis
-- Business Scenario: "The CEO wants to see sales performance broken down by time periods. 
-- Start with yearly total, then quarterly, then monthly sales for 2024."
-- Demonstrates: Drill-down (Year -> Quarter -> Month)

SELECT 
    d.year, 
    d.quarter, 
    d.month_name, 
    SUM(f.total_amount) AS total_sales, 
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
WHERE d.year = 2024
GROUP BY d.year, d.quarter, d.month, d.month_name
ORDER BY d.year, d.month;


-- Query 2: Product Performance Analysis
-- Business Scenario: "The product manager needs to identify top-performing products. 
-- Show the top 10 products by revenue, along with their category, total units sold, and revenue contribution percentage."

WITH TotalRevenueCTE AS (
    SELECT SUM(total_amount) as grand_total FROM fact_sales
)
SELECT 
    p.product_name, 
    p.category, 
    SUM(f.quantity_sold) AS units_sold, 
    SUM(f.total_amount) AS revenue,
    ROUND((SUM(f.total_amount) / (SELECT grand_total FROM TotalRevenueCTE)) * 100, 2) || '%' AS revenue_percentage
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
GROUP BY p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;


-- Query 3: Customer Segmentation Analysis
-- Business Scenario: "Marketing wants to target high-value customers. 
-- Segment customers into 'High Value' (>₹50,000 spent), 'Medium Value' (₹20,000-₹50,000), and 'Low Value' (<₹20,000). 
-- Show count of customers and total revenue in each segment."

SELECT 
    customer_segment_group,
    COUNT(customer_id) AS customer_count,
    SUM(total_spent) AS total_revenue,
    ROUND(AVG(total_spent), 2) AS avg_revenue
FROM (
    SELECT 
        c.customer_id,
        SUM(f.total_amount) AS total_spent,
        CASE 
            WHEN SUM(f.total_amount) > 50000 THEN 'High Value'
            WHEN SUM(f.total_amount) BETWEEN 20000 AND 50000 THEN 'Medium Value'
            ELSE 'Low Value'
        END AS customer_segment_group
    FROM fact_sales f
    JOIN dim_customer c ON f.customer_key = c.customer_key
    GROUP BY c.customer_id
) AS customer_spending
GROUP BY customer_segment_group
ORDER BY total_revenue DESC;
