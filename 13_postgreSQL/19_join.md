
## JOIN :

**A JOIN in PostgreSQL is a SQL clause used to combine rows from two or more tables based on a related column, typically a Primary Key and a Foreign Key.**


## Types of Join :

**...Cross Join**
**...Inner Join**
**...Right Join**
**...Left Join**

# CROSS JOIN : 

> A CROSS JOIN combines every row of one table with every row of another table, regardless of whether there is a matching column or relationship.

## Query Example Of CROSS JOIN :

**SELECT * FROM students CROSS JOIN teachers;** <!-- command>

## INNER JOIN : 

> A INNER JOIN returns only the rows where there is a match betweeen the specified columns in both the left(or first) and right(or second) tables.

## Query Example Of INNER JOIN :

**SELECT * FROM students s INNER JOIN teachers t ON s.teacher_id = t.teacher_id**

**SELECT s.name, s.age, FLOOR(AVG(s.age))** 
**FROM students s**
**INNER JOIN teachers t**
**ON s.teacher_id = t.teacher_id**
**GROUP BY s.name, s.age**

## LEFT JOIN : 

> A LEFT JOIN returns all the rows from left(or first) table and the matching rows from the right(or second) table.

## Query Example Of Left Join :

**SELECT * FROM students s**
**LEFT JOIN teachers t**
**ON s.teacher_id = t.teacher_id;**

> Logical Query Example With Filtering

**SELECT * FROM teachers t**
**LEFT JOIN students s**
**ON t.teacher_id = s.teacher_id**
**WHERE s.name ILIKE 'S%'**
**ORDER BY s.name DESC;**


## RIGHT JOIN : 

> A RIGHT JOIN returns all the rows from the RIGHT (or second) table and the matching rows from the LEFT (or first) table.

## Query Example Of Right Join: 

**SELECT * FROM students s**
**RIGHT JOIN teachers t**
**ON s.teacher_id = t.teacher_id;**


