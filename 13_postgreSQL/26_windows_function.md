

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

# Core Components OVER:

> OVER: Mandatory clause that defines the window or context of rows the function operates on.
> ORDER BY: Dictates the exact sequence in which the numbers are assigned. Without this, the numbering order is unpredictable.
> PARTITION BY (Optional): Divides the rows into logical groups (partitions). The row numbers reset back to 1 at the start of each new group.
 
# ROW_NUMBER() :

> In PostgreSQL, ROW_NUMBER() is a window function that assigns a sequential, unique integer to each row within a query result set. The numbering always starts at 1 for the first row.


<!-- 
SELECT
	  ROW_NUMBER() OVER(ORDER BY dept)
      fname, dept,salary
FROM employees;
-->

# RANK() :

> RANK() is a window function that assigns a unique position number to each row within an ordered group, but skips subsequent numbers if rows share identical values.

<!-- 
SELECT 
      RANK() OVER(ORDER BY dept),
      fname,
      dept,
      salary
FROM employees 
-->

# DENSE_RANK() :

> DENSE_RANK() is a window function that assigns a sequential position number to each row within an ordered group, but never skips any numbers when ties occur.

> RANK() skips positions after a tie (e.g., 1, 2, 2, 4), whereas DENSE_RANK() leaves no gaps in the ranking sequence (e.g., 1, 2, 2, 3). We need DENSE_RANK() when we want a continuous list of consecutive podium places without missing any rank numbers due to identical scores.

<!-- 
SELECT 
      fname, salary,
	  DENSE_RANK() OVER(ORDER BY salary DESC)
FROM employees; 
-->

# LAG() & LEAD() :

> LAG() and LEAD() are PostgreSQL window functions used to grab data from neighboring rows without using complex self-joins. LAG() looks backward to pull a value from a previous row, making it perfect for comparing current records against past data, like calculating day-over-day revenue growth. Conversely, LEAD() looks forward to pull a value from a subsequent row, which is ideal for predicting next steps or calculating the time elapsed between a current event and the next chronological action.

**LEAD**

<!-- 
SELECT
    fname, 
    dept, 
    salary,
    LEAD(salary) OVER(ORDER BY salary)
FROM employees;
 -->

<!-- 
SELECT
      fname,
	  dept,
	  salary,
	  ROUND(
         COALESCE(
            LEAD(salary) OVER(ORDER BY dept),
			AVG(salary) OVER()
		 )::numeric,
		 2
	  ) AS next_salary
FROM employees
 -->

**LAG**

<!-- 
SELECT
    fname, 
    dept, 
    salary,
    LEAD(salary) OVER(ORDER BY salary)
FROM employees;
 -->

 <!-- 
 SELECT
      fname,
	  dept,
	  salary,
	  ROUND(
         COALESCE(
            LAG(salary) OVER(ORDER BY dept),
			AVG(salary) OVER()
		 )::numeric,
		 2
	  ) AS previous_salary
FROM employees
  -->

