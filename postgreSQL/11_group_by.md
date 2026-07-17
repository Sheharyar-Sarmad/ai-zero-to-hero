

Group By :

def: GROUP BY is a SQL clause used to group rows that have the same values in one or more columns, allowing aggregate functions like COUNT(), SUM(), AVG(), MIN(), and MAX() to perform calculations on each group instead of the entire table.

Query example :

SELECT dept, 
COUNT(emp_id)
FROM employees
GROUP BY dept; <!--command> GROUP BY dept groups all employees who belong to the same department. COUNT(emp_id) counts the number of employees in each department and returns one row per department.


SELECT dept,
SUM(salary) 
FROM employees
WHERE dept = 'IT'
GROUP BY dept; <!-- command> The WHERE dept = 'IT' clause first filters the table so that only employees from the IT department are included in the result. Then, GROUP BY dept groups those filtered rows (which will only be the IT department), and SUM(salary) adds together the salaries of all IT employees, returning the total salary paid to the IT department.


SELECT dept,
MAX(salary) , COUNT(dept) , SUM(salary)
FROM employees WHERE salary >= 50000 GROUP BY dept; <!-- command> The WHERE salary >= 50000 clause first filters the table and keeps only employees whose salary is 50,000 or more. Then, GROUP BY dept groups these filtered employees according to their department. For each department, MAX(salary) returns the highest salary, COUNT(dept) counts the number of employees, and SUM(salary) calculates the total salary paid to that department.


SELECT dept,
       MAX(salary),
       COUNT(dept),
       SUM(salary)
FROM employees
WHERE dept LIKE 'M%'
GROUP BY dept; <!-- commmand> The WHERE dept LIKE 'M%' clause filters the table and selects only those departments whose names start with the letter 'M', such as Marketing, Management, or Maintenance. Then, GROUP BY dept groups the filtered rows by department, and for each department SQL returns the highest salary (MAX), the number of employees (COUNT), and the total salary paid (SUM).