

# User Defined Functions : 

> A User-Defined Function (UDF) is a reusable block of code stored in the database database that accepts inputs, runs logic, and returns a value **[User-Defined-Functions]**.

# User Defined Functions VS  Stored Procedure : 

**The Core Difference**

> Functions (UDF) are designed to calculate and return data. They behave like formulas.
> Procedures (SP) are designed to execute business actions. They behave like processing scripts.

# Problem : 

**Find name of the employees in each department having maximum salary.**

<!-- 
CREATE OR REPLACE FUNCTION max_salary_per_dept(dept_name VARCHAR)
RETURNS TABLE(emp_id INT, fname VARCHAR, dept VARCHAR, salary NUMERIC)AS $$
BEGIN
     RETURN QUERY
	 SELECT
	 e.emp_id,
	 e.fname,
	 e.dept,
	 e.salary
	 From 
	    employees e
	 WHERE 
	    e.dept = dept_name 
	 AND e.salary = (
        SELECT MAX(emp.salary)
		FROM employees emp
		WHERE emp.dept = dept_name
	 );
END;
$$ LANGUAGE plpgsql; 
-->

**Thats how we can call functions!**

<!-- 
SELECT * FROM max_salary_per_dept('IT');
 -->
