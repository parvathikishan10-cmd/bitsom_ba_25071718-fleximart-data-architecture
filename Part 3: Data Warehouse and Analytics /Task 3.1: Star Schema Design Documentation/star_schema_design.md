# Task 3.1: Star Schema Design Documentation

## Section 1: Schema Overview
The FlexiMart data warehouse uses a Star Schema optimized for high-performance analytical queries.

### FACT TABLE: fact_sales
* **Grain**: One row per product per order line item.
* **Business Process**: Sales transactions.
* **Measures (Numeric Facts)**:
    * **quantity_sold**: Number of units sold.
    * **unit_price**: Price per unit at time of sale.
    * **discount_amount**: Discount applied.
    * **total_amount**: Final amount (quantity × unit_price - discount).
* **Foreign Keys**:
    * **date_key** → dim_date
    * **product_key** → dim_product
    * **customer_key** → dim_customer

### DIMENSION TABLE: dim_date
* **Purpose**: Date dimension for time-based analysis.
* **Type**: Conformed dimension.
* **Attributes**:
    * **date_key (PK)**: Surrogate key (integer, format: YYYYMMDD).
    * **full_date**: Actual date.
    * **day_of_week**: Monday, Tuesday, etc.
    * **month**: 1-12.
    * **month_name**: January, February, etc.
    * **quarter**: Q1, Q2, Q3, Q4.
    * **year**: 2023, 2024, etc.
    * **is_weekend**: Boolean.

### DIMENSION TABLE: dim_product
* **Purpose**: Stores product attributes for slicing sales by category and brand.
* **Attributes**:
    * **product_key (PK)**: Surrogate key (integer).
    * **product_id**: Original natural key from source system.
    * **product_name**: Full name of the product.
    * **category**: High-level category (Electronics, Fashion, etc.).
    * **subcategory**: Specific product group.
    * **brand**: Manufacturer or brand name.

### DIMENSION TABLE: dim_customer
* **Purpose**: Stores demographic data for customer segmentation analysis.
* **Attributes**:
    * **customer_key (PK)**: Surrogate key (integer).
    * **customer_id**: Original natural key from source system.
    * **customer_name**: Full name (First + Last).
    * **city**: Resident city.
    * **state**: Resident state.
    * **segment**: Customer category (Gold, Silver, Regular).

---

## Section 2: Design Decisions
* **Granularity Choice**: We chose the **transaction line-item level** because it provides the highest level of detail. This allows the business to analyze not just total orders, but specific product performance within those orders. Lower grain (atomic data) ensures we never lose information that might be needed for future unforeseen queries.
* **Surrogate Keys vs. Natural Keys**: We use **Surrogate Keys** (integers) to decouple the data warehouse from source system changes. If a `product_id` changes in the Notion source, the warehouse remains stable. Integers also offer significantly faster JOIN performance than string-based natural keys.
* **Analytical Operations**: This design natively supports **Drill-down** (moving from Year → Quarter → Month via `dim_date`) and **Roll-up** (aggregating individual product sales into Category totals via `dim_product`). By joining the fact table to dimensions, users can easily pivot data across any attribute.

---

## Section 3: Sample Data Flow
**Source Transaction**: Order #101, Customer "John Doe", Product "Laptop", Qty: 2, Price: 50000

**Data Warehouse Representation**:
* **fact_sales**: `{ date_key: 20240115, product_key: 5, customer_key: 12, quantity_sold: 2, unit_price: 50000, total_amount: 100000 }`
* **dim_date**: `{ date_key: 20240115, full_date: '2024-01-15', month: 1, quarter: 'Q1', year: 2024, is_weekend: false }`
* **dim_product**: `{ product_key: 5, product_id: 'PROD_L_01', product_name: 'Laptop', category: 'Electronics', brand: 'Generic' }`
* **dim_customer**: `{ customer_key: 12, customer_id: 'CUST_JD_01', customer_name: 'John Doe', city: 'Mumbai', state: 'Maharashtra' }`
