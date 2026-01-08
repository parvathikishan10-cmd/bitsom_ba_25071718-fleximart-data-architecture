# Part 1: Relational Database & ETL Pipeline

## Overview
This stage involves the extraction, transformation, and loading (ETL) of raw retail data into a normalized relational database. The goal was to ensure data integrity and prepare the foundation for operational business queries.

## Database Schema (3NF)
The database is structured into four primary tables to minimize redundancy:
* **customers**: Personal details and registration metadata.
* **products**: Product catalog with categories and pricing.
* **orders**: High-level transaction headers linked to customers.
* **order_items**: Transaction line-items linking products to orders.



## ETL Process
The `etl_pipeline.py` script performs the following operations:
1.  **Extraction**: Reads raw semi-structured data from Notion exports.
2.  **Transformation**: 
    * Standardizes phone numbers and email formats.
    * Handles missing values via imputation.
    * Validates data types (e.g., ensuring prices are numeric).
3.  **Loading**: Rebuilds the schema and populates the SQLite/MySQL tables.

## Engineering Challenges
* **Schema Rigidity**: Encountered limitations when attempting to store varied product specifications in a fixed-column format.
* **Data Inconsistencies**: Managed discrepancies in the source dataset through a robust validation layer.
* **Join Complexity**: Balanced the level of normalization to ensure that common business queries remained performant.

## Business Queries
The included `business_queries.sql` file provides insights into:
* Revenue trends by month.
* Customer purchasing behavior.
* Inventory and stock alerts.
