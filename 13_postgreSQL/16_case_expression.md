

## CASE Expression :

> A CASE expression in PostgreSQL is a conditional expression used to evaluate conditions and return different values depending on which condition is true. If no condition is true, it returns the value specified in the ELSE clause or NULL if ELSE is omitted.

## Query Example :

**SELECT**
     **fname,**
	 **salary,**
     **CASE** 
	    **WHEN salary >= 50000 THEN 'High'**
		**ELSE 'Low'**
	 **END AS sal_cat**
	 **FROM employees;** <!-- command> 


**SELECT** 
      **fname,**
	  **salary,**
	  **CASE** 
	      **WHEN salary >= 50000 THEN 'HIGH'**
		  **WHEN salary >= 40000 AND salary < 50000**
		  **THEN 'MEDIUM'**
		  **ELSE 'LOW'**
	  **END AS sal_cat**
	  **FROM employees;**
**

**SELECT** 
     **fname,**
	 **dept,**
	 **CASE **
	     **WHEN dept LIKE 'I%' THEN 'High Rank'**
		 **WHEN dept LIKE 'F%' THEN 'Mid Rank'**
		 **WHEN dept LIKE 'M%' THEN 'Normal Rank'**
		 **WHEN dept LIKE 'H%' THEN 'Normal Rank'**
		 ELSE 'Low Rank'**
	  **END AS dept_rank**
	  **FROM employees;**


<!-- EXERCISE QUESTION -->

## WITHOUT CASE EXPRESSION

**SELECT** 
      **fname,**
	  **salary,**
	  **ROUND(salary * 0.10 , 0)** AS Bonus
**FROM employees;**

## WITH CASE EXPRESSION

**SELECT** 
     **fname,**
	 **salary,**
	 **CASE** 
	     **WHEN salary > 0 THEN ROUND(salary*0.10 , 0)**
     **END AS bonus**
	     **FROM employees;**