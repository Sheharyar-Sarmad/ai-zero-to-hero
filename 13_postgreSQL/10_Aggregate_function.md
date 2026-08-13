
Aggregate Functions in SQL:

Aggregate functions perform calculations on multiple rows and return a single summary value. They're used with GROUP BY to create summaries.\

IMPORTANT AGGREGATE FUNCTION :

COUNT()
SUM()
AVG()
MIN()
MAX()
ARRAY_AGG()

Query Example :

COUNT() :

SELECT COUNT(emp_id) FROM employees; <!-- command> this means count the emp_id data set from employees table
SELECT COUNT(*) FROM employees <!-- command> this means count all the rows columns

SUM() :

SELECT SUM(salary) FROM employees; <!-- command> this go to salary column and sum all the existing data of the salary column and give me one amount. NOTE: this will only run for numeric data types columns.

AVG() :

SELECT AVG(salary) FROM employees; <!-- command> this means analyze all the data of salary column and give me an average salary amount which we are giving to every person in a bank(our db). NOTE: this will only run for numeric data type columns.

MIN() :

SELECT MIN(salary) FROM employees; <!-- commmand> This means give the minimum salary in the salary column.

MAX() :

SELECT MAX(salary) FROM employees; <!-- command> This means give the maximum salary in the salary column.


