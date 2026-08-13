
<!-- Enhancing the previous data set -->

<!-- Just like we saw we can add same id's data as well as do null data as well to controll and enhance it we use different data types and constraints -->

Data Type:

<!-- Numeric: INT (DOUBLE FLOAT DECIMALS) -->
<!-- String: VARCHAR  -->
<!-- Date: DATE -->
<!-- Boolean: BOOLEAN -->

<!-- A Constraint is rule which is applied to a column -->

Constraints: 

 Primary Key <!-- Uniquely identifies each row in a table — combines NOT NULL and UNIQUE, and only one per table.>
 NOT NULL <!-- Ensures a column cannot have empty/NULL values — data must always be provided.>
 Default <!-- Sets a default value for a column when no value is provided during insertion>
 Serial <!-- Auto-increments integer values (like an automatic counter) — PostgreSQL's version of AUTO_INCREMENT.>
 Unique <!-- Ensures all values in a column are different — no duplicates allowed.>

<!-- IMPORTANT RULE -->

<!-- if you make a column PRIMARY KEY and provide its value then every time you have to provide the value of the primary key its auto increment will be off forever if you want dynamic auto increment then dont provide the value of PRIMARY KEY -->
