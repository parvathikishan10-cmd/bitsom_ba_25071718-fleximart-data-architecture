# Part 3: Data Warehouse & Analytics

## Overview
This section focuses on the implementation of a Star Schema Data Warehouse for FlexiMart. By separating analytical processing from operational data, we enable high-performance reporting on historical sales patterns, customer behavior, and product performance.

## Star Schema Architecture
The warehouse is designed around a central **Fact Table** connected to multiple **Dimension Tables**. This structure is optimized for "slicing and dicing" data across various business attributes.

* **Fact Table (`fact_sales`)**: Contains the quantitative metrics (Quantity, Unit Price, Total Amount) and foreign keys to the dimensions.
* **Dimension Tables**:
    * **dim_date**: Enables time-series analysis (Yearly, Quarterly, Monthly).
    * **dim_product**: Supports analysis by category and subcategory.
    * **dim_customer**: Facilitates demographic and segment-based reporting.



## Engineering Challenges

* **Granularity Determination**: Selecting the appropriate level of detail for the fact table required balancing the need for deep insights with overall system performance.
* **Relational Join Optimization**: Standard analytical queries across large datasets proved computationally expensive, necessitating the use of optimized keys for faster processing.
* **Data Consistency**: Ensuring that the transformed data in the warehouse maintained total alignment with the source records while moving between different schema formats.

## Analytical Capabilities
The included `analytics_queries.sql` demonstrates key OLAP operations:
1.  **Drill-Down Analysis**: Moving from yearly totals down to specific monthly performance.
2.  **Contribution Analysis**: Calculating the revenue percentage contribution of top-performing products.
3.  **Customer Segmentation**: Categorizing the customer base into High, Medium, and Low-value segments using spending thresholds.

## Design Decisions
* **Surrogate Keys**: Used instead of natural keys to decouple the warehouse from source system changes and improve JOIN performance.
* **Line-Item Grain**: We chose the finest level of detail (individual products within an order) to ensure that no analytical information is lost during aggregation.
