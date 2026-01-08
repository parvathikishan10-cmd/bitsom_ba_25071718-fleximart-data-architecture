# Task 2.1: NoSQL Strategic Justification Report

## Section A: Architectural Limitations of the Relational Model
While the RDBMS structure used in our initial ETL process ensures high data integrity, it introduces significant constraints for an evolving retail catalog.

* **The Problem with products having different attributes**: Our current schema requires a rigid, uniform structure for all products. Forcing diverse categories like 'Electronics' and 'Fashion' into a single table results in "Sparse Data"—rows filled with NULL values for attributes that don't apply to every item. This leads to inefficient storage and complicates backend query logic.
* **Frequent schema changes when adding new product types**: Relational databases follow a "Schema-on-Write" approach. Any expansion of the product line requires manual `ALTER TABLE` operations. In a live production environment, these schema changes can lock tables and cause significant operational downtime.
* **Storing customer reviews as nested data**: Storing dynamic content, such as customer reviews, requires the creation of separate tables and expensive JOIN operations. As the volume of metadata grows, these joins become a performance bottleneck, increasing latency for the end-user.

## Section B: Strategic Benefits of MongoDB Implementation
Transitioning to MongoDB allows FlexiMart to move toward a "Schema-on-Read" architecture, which is inherently better suited for high-growth e-commerce.

* **Flexible schema (document structure)**: MongoDB utilizes BSON documents, allowing each product record to store its own unique set of attributes. This flexibility enables us to add new product specifications on the fly without system-wide schema modifications.
* **Embedded documents (reviews within products)**: By leveraging **Embedded Documents**, we can store customer reviews and related metadata directly within the primary product record. This ensures **Data Locality**, allowing the application to fetch all necessary page data in a single I/O operation, effectively eliminating the "JOIN tax" identified in our SQL analysis.
* **Horizontal Scalability**: MongoDB supports native sharding, allowing data to be distributed across multiple commodity servers. This "Scale-Out" capability ensures that FlexiMart can handle traffic surges and massive data growth without the high costs associated with vertical scaling in traditional RDBMS environments.

## Section C: Technical Trade-offs and Considerations
Adopting a NoSQL approach requires us to manage two primary architectural trade-offs:

1.  **Complexity in Relational Reporting**: MongoDB is not optimized for complex cross-collection joins. Strategic business intelligence—such as the multi-table purchase history reports generated in Task 1.3—becomes more complex to implement at the application level without native SQL `JOIN` capabilities.
2.  **Increased Storage Footprint (Denormalization)**: To optimize for read speed, MongoDB encourages data denormalization. Storing redundant data (like customer metadata within order records) improves performance but increases the storage footprint compared to the 3NF (Third Normal Form) efficiency of our MySQL design.
