# FlexiMart Database Schema Documentation

## 1. Entity-Relationship Description
The FlexiMart database is structured to track the relationship between customers, products, and sales transactions efficiently.

### ENTITY: customers
**Purpose:** Stores profile and contact information for all registered users.
####**Attributes:**
- **customer_id**: Primary Key (PK). Unique ID for each customer.
- **first_name**: Customer's given name.
- **last_name**: Customer's family name.
- **email**: Unique email address (standardized during ETL).
- **phone**: Contact number in +91-XXXXXXXXXX format.
- **city**: Resident city of the customer.
- **registration_date**: Date of account creation (YYYY-MM-DD).
#####**Relationships:** - One customer can place **MANY** sales transactions.

### ENTITY: products
**Purpose:** Stores the inventory catalog and pricing details.
####**Attributes:**
- **product_id**: Primary Key (PK). Unique product code.
- **product_name**: Name of the retail item.
- **category**: Product group (Electronics, Fashion, Groceries).
- **price**: Unit price (imputed with median if missing).
- **stock_quantity**: Number of items available in stock.
#####**Relationships:** - One product can be sold in **MANY** different transactions.

### ENTITY: sales
**Purpose:** Records every purchase transaction made at FlexiMart.
####**Attributes:**
- **transaction_id**: Primary Key (PK). Unique ID for the sale.
- **customer_id**: Foreign Key (FK). Links to the customer who bought the item.
- **product_id**: Foreign Key (FK). Links to the specific product sold.
- **quantity**: Number of units purchased.
- **unit_price**: Price per unit at the time of sale.
- **transaction_date**: Date of the purchase (YYYY-MM-DD).
- **status**: Order status (Completed, Pending, Cancelled).

---

## 2. Normalization Explanation (3NF)
This database design achieves **Third Normal Form (3NF)** by ensuring that every non-key attribute is dependent only on the Primary Key, eliminating transitive dependencies.

### Functional Dependencies
In the `customers` table, attributes like `first_name` and `email` are functionally dependent on `customer_id`. Similarly, in `products`, the `price` is determined strictly by the `product_id`. Because no non-key attribute depends on another non-key attribute, we avoid transitive dependency issues.

### Avoiding Anomalies
- **Update Anomalies**: If a product's price or category changes, we only update it in the `products` table once. This change is automatically reflected across all related sales logic without data inconsistency.
- **Insert Anomalies**: We can add a new product to the catalog even if it has never been sold yet, because the product information is decoupled from the transaction history.
- **Delete Anomalies**: If a transaction record is deleted from the `sales` table, we do not lose the underlying customer's profile or the product's details, as they reside in their own parent tables.

---

## 3. Sample Data Representation

### Customers Table
| customer_id | first_name | last_name | email | phone |
| :--- | :--- | :--- | :--- | :--- |
| C001 | Rahul | Sharma | rahul.sharma@gmail.com | +91-9876543210 |
| C002 | Priya | Patel | priya.patel@yahoo.com | +91-9988776655 |

### Products Table
| product_id | product_name | category | price | stock_quantity |
| :--- | :--- | :--- | :--- | :--- |
| P001 | Samsung Galaxy S21 | Electronics | 45999.00 | 150 |
| P002 | Nike Running Shoes | Fashion | 3499.00 | 80 |

### Sales Table
| transaction_id | customer_id | product_id | quantity | status |
| :--- | :--- | :--- | :--- | :--- |
| T001 | C001 | P001 | 1 | Completed |
| T002 | C002 | P004 | 2 | Completed |
