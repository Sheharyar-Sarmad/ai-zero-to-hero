

## Database vs Schema vs Tables: 

**Database = The entire container (like a building) that holds everything. You connect to one database via your DATABASE_URL.**

**Schema = A logical folder/namespace inside a database that organizes tables into groups (e.g., sales, hr, analytics). The default is public.**

**Table = The actual storage unit inside a schema where data lives in rows and columns (e.g., users, orders).**

**Hierarchy: Server → Database → Schema → Table (One database can have many schemas, and each schema can have many tables).**