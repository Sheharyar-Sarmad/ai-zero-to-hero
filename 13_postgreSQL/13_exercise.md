
## Task 1:

## output: 1:Raj:Sharma:IT
## query: 

**SELECT CONCAT_WS(':' , emp_id , fname , lname , dept)**
**FROM employees**
**WHERE fname = 'Raj';**

## Task 2:

## output: 1:Raj Sharma:IT:50000
## query: 

**SELECT CONCAT_WS(':' , emp_id , CONCAT_WS(' ',fname,lname) , dept , salary)**
**FROM employees**
**WHERE emp_id = 1;**

## Task 3:

## output: 4:Suman:FINANCE
## query:

**SELECT CONCAT_WS(':',emp_id,fname,UPPER(dept))**
**FROM employees**
**WHERE fname = 'Suman';**

## TASK 4:

## output: I1 Raju 
## H2 Priya
## query: 

**SELECT CONCAT_WS(' ' , CONCAT(LEFT(dept,1) , emp_id) , fname)**
**FROM employees**
**WHERE fname IN ('Raj','Priya');**

## TASK 5:

## Find different types of departments in database.

## query:

**SELECT dept,COUNT(dept)**
**FROM employees**
**GROUP BY dept;**

## TASK 6:

## Display records with high and low salary.

## query:

**SELECT MAX(salary) , MIN(salary) FROM employees;**

## TASK 7:

## How to see only top three records in the table

## query:

**SELECT * FROM employees LIMIT 3;**

## TASK 8 :

## Show records where name starts with 'A'

## query:

**SELECT * FROM employees**
**WHERE fname LIKE 'A%';**

## TASK 9 :

## Show the records of the data where the length of lname is 4.

## query:

**SELECT * FROM employees**
**WHERE LENGTH(lname) = 4;**