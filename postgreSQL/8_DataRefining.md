Data refining:

Data refining means filtering, sorting, and cleaning raw data to get only the specific, meaningful information you need from a database.

It uses clauses like WHERE, ORDER BY, DISTINCT, LIMIT, and LIKE to transform messy or large datasets into precise, organized results.

CLAUSES :
<!-- Where -->
Filters rows based on a condition (e.g., WHERE salary > 50000).

<!-- Distinct -->

Removes duplicate rows from the result (e.g., SELECT DISTINCT dept FROM employees).

<!-- Order By -->

Sorts results in ascending (ASC) or descending (DESC) order (e.g., ORDER BY salary DESC).

<!-- Limit -->

Restricts the number of rows returned (e.g., LIMIT 5).

<!-- Like -->

Searches for a pattern in a text column using wildcards (% for any characters, \_ for a single character). (e.g., WHERE name LIKE 'A%').


<!-- SOME IMPORTANT AND ADVANCE COMMANDS -->

select * from employees
where dept in ('HR','Finance'); <!-- command>

where dept = 'HR' or dept = 'Finance'; <!-- command>

SELECT * FROM employees
WHERE dept = 'IT' AND  SALARY >= 50000;

<!-- AND , OR difference in sql queries -->

The Difference Between AND and OR in SQL
These are logical operators used in the WHERE clause to combine multiple conditions. The difference is how they filter results.

The One-Line Answer:
Operator	What It Does
AND	        All conditions must be TRUE → results are narrower (more restrictive)
OR	        Any condition can be TRUE → results are broader (less restrictive)

<!-- ORDER BY  -->

SELECT * FROM employees ORDER BY fname; <!-- COMMAND>
-- by defualt its asc to desc
-- If you want to make it desc order than add DESC at the end

SELECT * FROM employees ORDER BY fname DESC; <!-- command>

<!-- LIKE -->

SELECT * FROM employees WHERE fname LIKE 'A%'; <!-- command> 'A%' this means fname starts from A and % means can contain any type of data no restriction of how much and what types of chars are coming next after A.
SELECT * FROM employees WHERE fname LIKE '%a'; <!-- command> '%a' this means fname should conatain any char and no matter how much chars but only ends at 'a'.
SELECT * FROM employees WHERE fname LIKE '%i%; <!-- command> this means get all the data sets which contain i in thier fname.
SELECT * FROM employees WHERE dept LIKE '__'; <!-- command> this means get all those data sets which have 2 chars in their dept column.
SELECT * FROM employees WHERE dept LIKE '_a%' <!-- command> this means get those data sets which have _ one char and after it contains 'a' char and after a it can contain anything like any char and any length.
SELECT * FROM employees WHERE hire_date::TEXT LIKE '2019%' <!-- command> this means get all the data set which contain 2019 as hire_date and ::TEXT LIKE means it convert int and non-string to strings