
Relationsip :

A relationship in PostgreSQL is an association between two or more tables, established using primary keys and foreign keys, to maintain data integrity and reduce data duplication.

Types of relationship :

One to One
One to Many 
Many to Many

A One-to-One relationship is a relationship in which one record in the first table is associated with only one record in the second table, and each record in the second table is associated with only one record in the first table. A person can have only one passport, and a passport belongs to only one person.

A One-to-Many relationship is a relationship in which one record in the first table can be associated with multiple records in the second table, but each record in the second table is associated with only one record in the first table. A department can have many employees, but each employee works in only one department.

A Many-to-Many relationship is a relationship in which multiple records in the first table can be associated with multiple records in the second table. This relationship is implemented using a junction (bridge) table.   A student can enroll in many courses, and a course can have many students.