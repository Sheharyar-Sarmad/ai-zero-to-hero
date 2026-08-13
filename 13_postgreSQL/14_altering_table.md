

Altering Table :

ALTER TABLE is a SQL command used to add, remove, rename, or modify columns and constraints in an existing table.

Query example: 

ALTER TABLE person
ADD COLUMN age INT; <!-- command> This alter table person means update the table person and add column age int means that add a new column with data type int.

ALTER TABLE peron
DROP COLUMN age; <!-- command> This means drop the age column from person table.

ALTER TABLE person 
RENAME COLUMN name TO fname; <!-- command> this means rename column name to fname

ALTER TABLE persons
RENAME TO person; <!-- command> this will rename the table persons to person.

ALTER TABLE person
ALTER COLUMN name
SET DATA TYPE VARCHAR(50); <!-- command> this will update the column name