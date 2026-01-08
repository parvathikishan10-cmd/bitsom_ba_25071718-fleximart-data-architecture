#"This script automates the process of cleaning and migrating retail data. 
# It extracts raw data from CSV files, performs data quality fixes—such as 
# removing duplicate customer/transaction records (C001, T001), 
# standardizing phone formats, and filling missing product prices—and 
# finally loads the cleaned data into a structured SQLite database.

# The text copy-pasted from Notion
data_customer = """customer_id,first_name,last_name,email,phone,city,registration_date
C001,Rahul,Sharma,rahul.sharma@gmail.com,9876543210,Bangalore,2023-01-15
C002,Priya,Patel,priya.patel@yahoo.com,+91-9988776655,Mumbai,2023-02-20
C003,Amit,Kumar,,9765432109,Delhi,2023-03-10
C004,Sneha,Reddy,sneha.reddy@gmail.com,9123456789,Hyderabad,15/04/2023
C005,Vikram,Singh,vikram.singh@outlook.com,09988112233,Chennai,2023-05-22
C006,Anjali,Mehta,anjali.mehta@gmail.com,9876543210,Bangalore,2023-06-18
C007,Ravi,Verma,,+919876501234,Pune,2023-07-25
C008,Pooja,Iyer,pooja.iyer@gmail.com,9123456780,Bangalore,08-15-2023
C009,Karthik,Nair,karthik.nair@yahoo.com,9988776644,Kochi,2023-09-30
C010,Deepa,Gupta,deepa.gupta@gmail.com,09871234567,Delhi,2023-10-12
C001,Rahul,Sharma,rahul.sharma@gmail.com,9876543210,Bangalore,2023-01-15
C011,Arjun,Rao,arjun.rao@gmail.com,9876509876,Hyderabad,2023-11-05
C012,Lakshmi,Krishnan,,9988001122,Chennai,2023-12-01
C013,Suresh,Patel,suresh.patel@outlook.com,9123409876,Mumbai,2024-01-08
C014,Neha,Shah,neha.shah@gmail.com,+91-9876543221,Ahmedabad,2024-01-15
C015,Manish,Joshi,manish.joshi@yahoo.com,9988776611,Jaipur,20/01/2024
C016,Divya,Menon,divya.menon@gmail.com,9123456701,Bangalore,2024-02-05
C017,Rajesh,Kumar,rajesh.kumar@gmail.com,09876123450,Delhi,2024-02-12
C018,Kavya,Reddy,,9988112200,Hyderabad,2024-02-18
C019,Arun,Pillai,arun.pillai@outlook.com,9876543298,Kochi,02-25-2024
C020,Swati,Desai,swati.desai@gmail.com,9123456712,Pune,2024-03-01
C021,Nikhil,Bose,nikhil.bose@gmail.com,+919988776600,Kolkata,2024-03-10
C022,Priyanka,Jain,priyanka.jain@yahoo.com,9876543287,Indore,2024-03-15
C023,Rohit,Kapoor,,9988112211,Chandigarh,2024-03-20
C024,Meera,Nambiar,meera.nambiar@gmail.com,9123456723,Trivandrum,03-25-2024
C025,Sanjay,Agarwal,sanjay.agarwal@gmail.com,09876543276,Lucknow,2024-03-28"""

with open('customers_raw.csv', 'w') as f:
    f.write(data_customer.strip())

print("Conversion complete!")

# The text copy-pasted from Notion
data_products = """product_id,product_name,category,price,stock_quantity
P001,Samsung Galaxy S21,Electronics,45999.00,150
P002,Nike Running Shoes,fashion,3499.00,80
P003,Apple MacBook Pro,ELECTRONICS,,45
P004,Levi's Jeans,Fashion,2999.00,120
P005,Sony Headphones,electronics,1999.00,200
P006,Organic Almonds,Groceries,899.00,
P007,HP Laptop,Electronics,52999.00,60
P008,Adidas T-Shirt,FASHION,1299.00,150
P009,Basmati Rice 5kg,groceries,650.00,300
P010,OnePlus Nord,Electronics,,95
P011,Puma Sneakers,Fashion,4599.00,70
P012,Dell Monitor 24inch,Electronics,12999.00,40
P013,Woodland Shoes,fashion,5499.00,55
P014,iPhone 13,Electronics,69999.00,80
P015,Organic Honey 500g,Groceries,450.00,200
P016,Samsung TV 43inch,ELECTRONICS,32999.00,35
P017,H&M Shirt,Fashion,,90
P018,Masoor Dal 1kg,groceries,120.00,500
P019,Boat Earbuds,Electronics,1499.00,250
P020,Reebok Trackpants,FASHION,1899.00,110"""

with open('products_raw.csv', 'w') as f:
    f.write(data_products.strip())

print("Conversion complete!")

# The text copy-pasted from Notion
data_sales = """transaction_id,customer_id,product_id,quantity,unit_price,transaction_date,status
T001,C001,P001,1,45999.00,2024-01-15,Completed
T002,C002,P004,2,2999.00,2024-01-16,Completed
T003,C003,P007,1,52999.00,15/01/2024,Completed
T004,,P002,1,3499.00,2024-01-18,Pending
T005,C005,P009,3,650.00,2024-01-20,Completed
T006,C006,P012,1,12999.00,01-22-2024,Completed
T007,C007,P005,2,1999.00,2024-01-23,Completed
T008,C008,,1,1299.00,2024-01-25,Completed
T009,C009,P011,1,4599.00,2024-01-28,Cancelled
T010,C010,P006,5,899.00,2024-02-01,Completed
T001,C001,P001,1,45999.00,2024-01-15,Completed
T011,C011,P014,1,69999.00,02/02/2024,Completed
T012,C012,P003,1,52999.00,2024-02-05,Completed
T013,C013,P015,3,450.00,2024-02-08,Completed
T014,C014,P019,2,1499.00,02-10-2024,Completed
T015,C015,P008,3,1299.00,2024-02-12,Completed
T016,,P013,1,5499.00,2024-02-15,Pending
T017,C017,P016,1,32999.00,2024-02-18,Completed
T018,C018,P020,2,1899.00,2024-02-20,Completed
T019,C019,P018,10,120.00,02/22/2024,Completed
T020,C020,P010,1,45999.00,2024-02-25,Completed
T021,C021,P017,2,2999.00,2024-02-28,Completed
T022,C002,P001,1,45999.00,2024-03-01,Completed
T023,C003,P019,3,1499.00,03-02-2024,Completed
T024,C004,P009,5,650.00,2024-03-05,Completed
T025,C005,,1,1999.00,2024-03-08,Completed
T026,C006,P011,1,4599.00,2024-03-10,Completed
T027,C007,P002,2,3499.00,03/12/2024,Completed
T028,C008,P015,4,450.00,2024-03-15,Completed
T029,C009,P007,1,52999.00,2024-03-18,Completed
T030,,P004,3,2999.00,2024-03-20,Pending
T031,C011,P012,1,12999.00,03-22-2024,Completed
T032,C012,P016,1,32999.00,2024-03-25,Completed
T033,C013,P005,2,1999.00,2024-03-28,Completed
T034,C014,P008,2,1299.00,2024-03-30,Completed
T035,C015,P018,8,120.00,04/01/2024,Completed
T036,C016,P014,1,69999.00,2024-04-03,Completed
T037,C017,P006,4,899.00,2024-04-05,Completed
T038,C018,P020,1,1899.00,04-08-2024,Completed
T039,C019,P019,2,1499.00,2024-04-10,Completed
T040,C020,P013,1,5499.00,2024-04-12,Completed """

with open('sales_raw.csv', 'w') as f:
    f.write(data_sales.strip())

print("Conversion complete!")

!pip install pymysql sqlalchemy
import pandas as pd
import sqlalchemy

# Create database engine 
engine = sqlalchemy.create_engine('sqlite:///fleximart.db')

#Database schema provided in assessment instructions.
db_schema = """
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    city VARCHAR(50),
    registration_date DATE
);

CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0
);
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
"""
# Execute the schema
with engine.connect() as conn:
    for statement in db_schema.split(';'):
        if statement.strip():
            conn.execute(sqlalchemy.text(statement))

print(db_schema)

import re
#  ETL PIPELINE
def run_etl():
    print("Starting ETL Pipeline...")

    # --- EXTRACT ---
    df_cust = pd.read_csv('customers_raw.csv')
    df_prod = pd.read_csv('products_raw.csv')
    df_sales = pd.read_csv('sales_raw.csv')

    # --- TRANSFORM ---
    # Strip spaces from column headers to prevent KeyError
    for df in [df_cust, df_prod, df_sales]:
        df.columns = df.columns.str.strip()

    # 1. Handle Duplicates
    cust_dupes = df_cust.duplicated().sum()
    df_cust.drop_duplicates(inplace=True)
    sales_dupes = df_sales.duplicated().sum()
    df_sales.drop_duplicates(inplace=True)

    # 2. Standardize Phone Formats (+91-XXXXXXXXXX)
    def fix_phone(p):
        digits = re.sub(r'\D', '', str(p))
        return f"+91-{digits[-10:]}" if len(digits) >= 10 else p
    df_cust['phone'] = df_cust['phone'].apply(fix_phone)

    # 3. Standardize Categories and Product Names
    df_prod['category'] = df_prod['category'].str.strip().str.capitalize()

    # 4. Handle Missing Values
    df_cust['email'] = df_cust['email'].fillna('unknown@fleximart.com')
    df_prod['price'] = df_prod['price'].fillna(df_prod['price'].median())
    df_prod['stock_quantity'] = df_prod['stock_quantity'].fillna(0)
    df_sales['customer_id'] = df_sales['customer_id'].fillna('GUEST')

    # 5. Normalize Date Formats
    df_cust['registration_date'] = pd.to_datetime(df_cust['registration_date'], dayfirst=False, errors='coerce').dt.strftime('%Y-%m-%d')
    df_sales['transaction_date'] = pd.to_datetime(df_sales['transaction_date'], dayfirst=False, errors='coerce').dt.strftime('%Y-%m-%d')

    # LOAD
    df_cust.to_sql('customers', con=engine, if_exists='replace', index=False)
    df_prod.to_sql('products', con=engine, if_exists='replace', index=False)
    df_sales.to_sql('sales', con=engine, if_exists='replace', index=False)

    print(f"ETL Success: {len(df_cust)} customers, {len(df_prod)} products, and {len(df_sales)} sales records loaded.")
    print(f"Duplicates removed: {cust_dupes + sales_dupes}")

run_etl()

def check_database():
    print("--- DATABASE QUALITY AUDIT ---")
    with engine.connect() as conn:
        # Check 1: Ensure no duplicates remain
        cust_count = conn.execute(sqlalchemy.text("SELECT COUNT(*) FROM customers")).scalar()
        sales_count = conn.execute(sqlalchemy.text("SELECT COUNT(*) FROM sales")).scalar()

        # Check 2: Check for standardized categories
        categories = pd.read_sql("SELECT DISTINCT category FROM products", conn)

        # Check 3: Verify Date Formats
        sample_dates = pd.read_sql("SELECT transaction_date FROM sales LIMIT 5", conn)

    print(f"Total Unique Customers: {cust_count} (Should be 24)") #
    print(f"Total Unique Sales: {sales_count} (Should be 39)") #
    print("\nStandardized Categories Found:")
    print(categories['category'].tolist())
    print("\nNormalized Date Sample:")
    print(sample_dates)

check_database()

# Check the first 5 rows of each table
with engine.connect() as conn:
    print("\n--- CUSTOMERS TABLE SAMPLE ---")
    display(pd.read_sql("SELECT * FROM customers LIMIT 5", conn))

    print("\n--- PRODUCTS TABLE SAMPLE ---")
    display(pd.read_sql("SELECT * FROM products LIMIT 5", conn))

with engine.connect() as conn:
    print("\n--- VERIFYING MISSING DATA FIXES ---")
    # Checking P003 and P010 prices
    missing_price_fix = pd.read_sql("SELECT product_id, price FROM products WHERE product_id IN ('P003', 'P010')", conn)
    display(missing_price_fix)

    # Checking C003 and C007 emails
    missing_email_fix = pd.read_sql("SELECT customer_id, email FROM customers WHERE customer_id IN ('C003', 'C007')", conn)
    display(missing_email_fix)