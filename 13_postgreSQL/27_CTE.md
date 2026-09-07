

# CTE(Common Table Expression) : 

> A Common Table Expression (CTE) is a temporary, named result set in SQL that you can reference within a single SELECT, INSERT, UPDATE, or DELETE statement.


> "Write a query to find all employees who earn more than the average salary of their respective departments." 

<!--
WITH avg_salary AS (
   SELECT dept, AVG(salary) AS avg_salary 
   FROM employees 
   GROUP BY dept
) -- The semicolon and extra closing parenthesis from here
SELECT 
      e.emp_id,
      e.fname,
      e.dept,
      e.salary
FROM employees e 
JOIN avg_salary a ON e.dept = a.dept; -- Added the semicolon at the end
WHERE e.salary > a.salary;
-->

