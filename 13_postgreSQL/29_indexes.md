# Indexes

> An index is a special database object that improves the speed of data retrieval operations on a table. Think of it like the index at the back of a book – instead of reading every page to find a topic, you go directly to the index and find the page number.

## Types of Indexes

### 1. Clustered Index
> A clustered index determines the physical order of data rows in a table based on the key values. A table can have only one clustered index because data rows themselves can be sorted in only one order.

> * **Analogy**: A phone book or dictionary, where the actual data is inherently organized alphabetically.
> * **When to use**: Automatically created on columns with a Primary Key. Ideal for range queries and highly unique columns.

<!-- 
CREATE CLUSTERED INDEX idx_employees_emp_id 
ON employees(emp_id);
-->

### 2. Non-Clustered Index
> A non-clustered index is a structure separate from the data rows. It contains the indexed columns and a pointer (row identifier) back to the actual row where the rest of the data lives.

> * **Analogy**: The index at the back of a textbook. The topics are ordered alphabetically, but the actual chapters are scattered elsewhere.
> * **When to use**: On columns frequently used in `WHERE`, `JOIN`, or `ORDER BY` clauses that are not part of the primary key.

<!--
CREATE NONCLUSTERED INDEX idx_employees_dept 
ON employees(dept);
-->

### 3. Unique Index
> Ensures that the indexed column(s) do not contain duplicate values. The database engine automatically creates a unique index when you define a `UNIQUE` or `PRIMARY KEY` constraint.

> * **Analogy**: A list of passport numbers or national IDs where no two citizens can share the same value.
> * **When to use**: To enforce data integrity on non-primary key columns that must remain distinct.

<!--
CREATE UNIQUE INDEX idx_employees_email 
ON employees(email);
-->

### 4. Composite Index
> An index built on two or more columns combined. It optimizes queries that filter or sort by multiple columns together in a specific sequence.

> * **Analogy**: A city directory organized first by state, then by city, and finally by street name.
> * **When to use**: When your queries consistently look up data using multiple criteria (e.g., searching by both `last_name` and `first_name`).

<!--
CREATE INDEX idx_employees_name 
ON employees(last_name, first_name);
-->

---

## Core Explanations

### The Trade-off (Read vs. Write Speed)
> Indexes significantly boost the performance of `SELECT` queries because the database engine does not have to scan the entire table (called a "Full Table Scan"). However, indexes slow down data modification statements:

> * **INSERT**: New rows must be written to the table, and the new keys must be sorted and placed into the index structure.
> * **UPDATE / DELETE**: If an indexed column changes or a row is removed, the corresponding index pointer must be found and reorganized.

### Internal Structure (B-Trees)
> Most standard database indexes utilize a balanced tree (B-Tree) data structure.

> * **Root Node**: The top entry point of the search tree.
> * **Intermediate Nodes**: Mid-level routing pointers that guide the search down to the correct page.
> * **Leaf Nodes**: The bottom layer containing the actual index keys and pointers to the data rows.

> This structure allows the database engine to find any specific row in a multi-million row table in just 3 to 4 quick operations.
