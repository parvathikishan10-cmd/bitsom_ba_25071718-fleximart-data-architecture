# Part 2: NoSQL Migration & Analysis

## Overview
This section documents the migration of the FlexiMart product catalog from a relational model to a NoSQL (MongoDB) environment. This shift was designed to accommodate polymorphic product data and nested review structures that were difficult to manage in a fixed SQL schema.

## Files in this Folder
* **products_catalog.json**: The migrated dataset featuring embedded documents and varied product attributes.
* **mongodb_operations.js**: Implementation of CRUD operations and advanced aggregation pipelines.
* **nosql_analysis.md**: This document, outlining the strategic justification for the migration.

## Engineering Challenges

* **Schema Rigidity**: Traditional fixed-column structures proved inefficient for handling products with highly varied specifications (e.g., Electronics vs. Apparel).
* **Nested Data Complexity**: Managing one-to-many relationships, such as customer reviews, required expensive join operations in the relational model.
* **Scalability Constraints**: The need for flexible data structures to support rapid inventory changes without downtime led to the selection of a document-oriented approach.



## Key Findings
* **Data Locality**: By embedding reviews and specifications directly within the product document, we achieved a "single-read" pattern that significantly improves performance for product display pages.
* **Polymorphism**: The JSON/BSON format allows for different categories of items to coexist in the same collection without the need for thousands of NULL values.
* **Agility**: The schema-on-read nature of MongoDB allows the business to add new product lines with unique attributes instantly, without database migrations.

## Sample MongoDB Operations
The implemented scripts demonstrate:
1. **Filtering**: Retrieving specific products based on nested attribute values.
2. **Aggregations**: Calculating average ratings across embedded review arrays.
3. **Updates**: Adding new reviews atomically to existing product documents.
