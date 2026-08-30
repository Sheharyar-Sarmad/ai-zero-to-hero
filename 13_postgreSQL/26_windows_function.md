

# Window Functions :

> Window functions, also known as analytic functions allow you to perform calculations accross a set of rows related to the current row.
> Defined by a **OVER** clause.

# Issue **OVER** Cluase Is Solving : 

<!-- 
SELECT
      SUM(salary)
	  FROM employees;
-->

> This will only give you the numeric value nothing else no other data.

<!-- 
SELECT
      fname,
	  salary,
      SUM(salary) OVER()
	  FROM employees;
-->

> This will give you the data but the issue is it will show exact sum of the salary by scaning all the rows but we dont want it our goal is to get the salary sum till the current row, so we can add ORDER BY salary inside OVER parenthesis like OVER(GROUP BY salary)

<!--
SELECT
      fname,
	  salary,
      SUM(salary) OVER(ORDER BY salary)
	  FROM employees;
-->

> Or if you want every field and want to add sum field with specific column name 

<!--
SELECT
     *,
	 SUM(salary) OVER(ORDER BY salary) AS total_salary
FROM employees;
-->

# Benefits of Window Functions : 

> Advanced Analytics: They enable complex calculations like running totals, moving averages, rank calculations, and cumulative distributions.

> Non-Aggregating: Unlike aggregate functions, window functions do not collapse rows. This means you can calculate aggregates while retaining individual row details.

> Flexibility: They can be used in various clauses of SQL, such as SELECT, ORDER BY, and HAVING, providing a lot of flexibility in writing queries.

# Some Other Important Window Functions :

**ROW_NUMBER()**
**RANK()**
**DENSE_RANK()**
**LAG()**
**LEAD()**
 