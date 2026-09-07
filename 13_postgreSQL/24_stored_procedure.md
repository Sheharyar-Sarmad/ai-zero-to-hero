

# Stored Routine :

> An SQL statement or a set of SQL statement that can be stored on database server which can be call no. of times.


# Type of Stored Routine : 

**STORED Procedure**
**User Defined Functions**

# STORED Procedure :

> Set of SQL statements & procedural logic that can perform operations such as Inserting, Updating, Deleting and Quering data.

# Query Syntax : 

<!-- CREATE OR REPLACE PROCEDURE procedure_name (parameter_name parameter_type, ...)
LANGUAGE plpgsql
AS $$
BEGIN
    -- procedural code here
END;
$$; -->

# Example Query :

<!-- CREATE OR REPLACE PROCEDURE update_emp_salary(
   p_emp_id INT,
   p_new_salary NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
     UPDATE employees 
	 SET salary = p_new_salary
	 WHERE emp_id = p_emp_id;
END;
$$; -->

> This query defines a stored procedure in PostgreSQL named update_emp_salary that updates a specific worker's salary in the employees table using parameterized inputs. Technically, it encapsulates a data manipulation language (DML) transaction within the server database layer, eliminating the need to write raw, repetitive SQL strings in your backend code. It provides modular abstraction, improves execution performance by pre-compiling the operational query plan, and secures data by preventing SQL injection vulnerabilities through bound variables (p_emp_id and p_new_salary).

<!-- 
CALL update_emp_salary(3, 72000)
 -->

> This simply means call the update_emp_salary procedure and update the salary to 72k where emp_id is 3

# Whole Procedure in One : 
<!-- 
CREATE OR REPLACE PROCEDURE update_emp_salary(
   p_emp_id INT,
   p_new_salary NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
     UPDATE employees 
	 SET salary = p_new_salary
	 WHERE emp_id = p_emp_id;
END;
$$;

CALL update_emp_salary(3, 72000);

SELECT * FROM employees WHERE emp_id = 3; -->


# Task : 

> Now create the procedure for inserting and if you dont want to you can see my query down.

<!-- 
CREATE OR REPLACE PROCEDURE add_employee(
 p_fname VARCHAR,
 p_lname VARCHAR,
 p_email VARCHAR,  
 p_dept VARCHAR,   
 p_salary NUMERIC  
)
LANGUAGE plpgsql
AS $$
BEGIN
     INSERT INTO employees(
        fname,
		lname,
		email,
		dept,
		salary,
		hire_date
	 )
	 VALUES(
        p_fname,
		p_lname,
		p_email,   
		p_dept,    
		p_salary,  
		CURRENT_DATE
	 )
	 ON CONFLICT (email) DO NOTHING;
END;
$$;

CALL add_employee('Sheharyar', 'Sarmad', 'sheharyar@gmail.com', 'IT', 110000.00);

SELECT * FROM employees WHERE fname = 'Sheharyar' OR lname = 'Sarmad';
 -->
