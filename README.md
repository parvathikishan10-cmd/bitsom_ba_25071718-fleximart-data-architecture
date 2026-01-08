 #FlexiMart Data Architecture Project

**Student Name:** Parvathi Gubba

**Student ID:** bitsom_ba_25071718

**Email:** parvathikishan10@gmail.com  

**Date:** January 8, 2026

## Project Overview
I built a complete end-to-end data ecosystem for FlexiMart, transitioning from a raw Notion dataset to a structured Relational (SQL) database, a flexible NoSQL (MongoDB) catalogue, and finally a high-performance Data Warehouse (Star Schema). This project demonstrates the full data lifecycle: ETL, schema design, NoSQL migration, and OLAP analytical reporting.

## Repository Structure
├── part1-database-etl/
│     ├── etl_pipeline.py

│     ├── schema_documentation.md

│     ├── business_queries.sql

│     └── data_quality_report.txt

├── part2-nosql/
│     ├── nosql_analysis.md

│     ├── mongodb_operations.js

│     └── products_catalog.json

├── part3-datawarehouse/
│     ├── star_schema_design.md

│     ├── warehouse_schema.sql

│     ├── warehouse_data.sql

│     └── analytics_queries.sql

└── README.md

## Technologies Used
- **Python 3.x**: pandas, sqlite3/mysql-connector (ETL and Automation)
- **SQL (MySQL/SQLite)**: Relational modeling and complex business logic
- **MongoDB**: Document-based modeling for flexible product catalogs
- **Data Warehousing**: Star Schema design for dimensional modeling and OLAP

## Setup Instructions

### Database Setup
```bash
# Create databases
# Note: For Colab testing, we used SQLite; for production MySQL:
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse
mysql -u root -p fleximart_dw < part3-datawarehouse_and_analytics/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse_and_analytics/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse_and_analytics/analytics_queries.sql

## Setup Instructions
1. Run `part1-database-etl/etl_pipeline.py` to initialize the operational database.
2. Use `mongoimport` to load `part2-nosql/products_catalog.json`.
3. Run the SQL scripts in `part3-datawarehouse_and_analytics/` to build the Data Warehouse.

## Key Learnings
I learned the importance of **Schema Evolution**. 
Moving from SQL to NoSQL highlighted how document-based storage handles 'messy' 
retail data more efficiently than fixed tables.

## Challenges Faced
Schema Flexibility vs. Rigidity: Managing diverse data types within a traditional fixed-schema environment created significant structural constraints. Transitioning to a document-oriented approach was necessary to resolve storage and query inefficiencies.
Source Data Discrepancies: The raw dataset presented several inconsistencies that required a robust validation and cleaning layer before the data was fit for production use.
Granularity Determination: Selecting the appropriate level of detail for the analytical fact tables required careful consideration to balance reporting depth with system performance.
Relational Join Optimization: Standard join operations on certain data types proved to be computationally expensive, requiring the implementation of optimized keys to streamline analytical query execution.
