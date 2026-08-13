

CRUD(Create , Read , Update and Delete) operations are most basic data manipluation methods used in all the db's.

<!-- Create -->
<!-- Read -->
<!-- Update -->
<!-- Delete -->

<!-- Create -->

Table is a collection of related data held in a table format within a data base.

<!-- How to create a table -->

CREATE TABLE person(
    id: int,
    name: VARCHAR(100),
    city: VARCHAR(100)
); <!-- command for creating table inside a db >


<!-- Inserting data into table -->

<!-- 1st COMMAND -->

INSERT INTO person(id , name , city) <!-- commmad>
VALUES (101 , 'Sheharyar' , 'Lahore') <!-- commmad>

<!-- 2nd COMMAND -->

INSERT INTO students VALUES (102 , 'Sarmad' , 'Lahore') <!-- command>

<!-- 3rd way for insertng more than one document -->

INSERT INTO person <!-- or you can also (id , name , city) as well but the query will only run if you provide all the three values>
VALUES
(102 , 'Sham' , 'Mumbai'),
(103 , 'Paul' , 'Chennai'),


<!-- Reading Data -->

SELECT * FROM <table_name> <!-- command, * means get all the columns from table> 
SELECT <column_name> from students <!-- command if you want a single column>
SELECT <column-name>,<column_name> from students <!-- command if you want two or more rows>


<!-- Update data -->

UPDATE person <!-- command>
SET city = "Lahore" <!-- command>
WHERE id = 2 <!-- command>

<!-- another real life tricky example  -->
UPDATE person 
SET city = 'Lahore'
WHERE city = 'Karachi';

COMMIT;

SELECT * FROM person WHERE city = 'Lahore' <!-- command>

<!-- Deleting data table -->

DELETE FROM person
WHERE id = 101