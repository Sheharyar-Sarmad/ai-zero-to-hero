

## String Function :

> String functions in PostgreSQL are built-in functions used to manipulate, modify, analyze, format, and retrieve information from string (text) data. They perform operations such as converting letter case, finding string length, extracting characters, replacing text, concatenating strings, trimming spaces, and searching within text values.

## Most common string methods:

**. CONCAT , CONCAT_WS**
**. SUBSTR**
**. LEFT , RIGHT**
**. LENGTH**
**. UPPER , LOWER**
**. TRIM , LTRIM , RTRIM**
**. REPLACE**
**. POSTION**
**. STRING_AGG**

## CONCAT :

**SELECT CONCAT(fname , lname) FROM employees;** <!-- command> CONCAT() is a PostgreSQL string function that combines two or more strings into a single string. In this query, PostgreSQL reads each row from the employees table and joins the values of the fname and lname columns. The result is returned as one combined string for every employee, such as AliKhan. To include a space between the names, use CONCAT(fname, ' ', lname).

**SELECT emp_id , CONCAT(fname, ' ', lname) AS FULLNAME ,**
**dept FROM employees;** <!-- command> This query retrieves the emp_id, department (dept), and a full name for each employee from the employees table. The CONCAT(fname, ' ', lname) function combines the first name and last name with a space between them, and AS FULLNAME gives the combined column the alias FULLNAME in the output.

## CONCAT_WS :

**SELECT emp_id , CONCAT_WS('-',fname,lname) AS FullName ,**
**dept , hire_date FROM employees;** <!-- command> CONCAT_WS() (Concatenate With Separator) is a PostgreSQL string function that joins two or more strings into a single string while automatically inserting a specified separator between each value. The separator is given as the first argument, followed by the strings to be combined. This query retrieves the employee ID, department, and hire date from the employees table. The CONCAT_WS('-', fname, lname) function combines the fname and lname columns into a single string, inserting a hyphen (-) between them (e.g., Ali-Khan). The AS FullName clause assigns the alias FullName to the concatenated column in the result.

## Difference between CONCAT() and CONCAT_WS():

**CONCAT(fname, lname) → AliKhan (no separator unless you add one manually).**
**CONCAT(fname, ' ', lname) → Ali Khan (you provide the separator yourself).**
**CONCAT_WS('-', fname, lname) → Ali-Khan (the separator is supplied once and automatically placed between all values).**

## SUBSTR :

**SELECT SUBSTR('Hello Budy!',1,5);** <!-- command> SUBSTR() is a PostgreSQL string function that extracts a specific portion of a string. In this query, PostgreSQL starts from the 1st character of 'Hello Budy!' and returns the next 5 characters, resulting in Hello.

## REPLACE :

**SELECT REPLACE('Hello world','Hello','HELLO');** <!-- command> REPLACE() is a PostgreSQL string function that searches for a specified substring within a string and replaces every occurrence of that substring with a new substring, returning the modified string. This query uses the REPLACE() function to search for the word Hello in the string 'Hello world'. It replaces every occurrence of Hello with HELLO and returns the updated string. The final output is HELLO world.

## REVERSE :

**SELECT REVERSE(lname) FROM employees;** <!-- command> REVERSE() is a PostgreSQL string function that returns a new string with the characters of the original string in reverse order. It does not modify the actual data stored in the table; it only reverses the string in the query result. This query retrieves the lname (last name) column from the employees table and applies the REVERSE() function to each value. PostgreSQL reverses the characters of every last name and returns the reversed string in the result set, while the original data in the table remains unchanged. For example, Khan becomes nahK.

## LENGTH :

**SELECT fname,LENGTH(fname) AS Length From employees;** <!-- command> This query retrieves the fname (first name) of each employee from the employees table. The LENGTH(fname) function calculates the number of characters in each first name, and AS Length assigns the alias Length to the resulting column. The output displays each employee's first name along with its character count.

**SELECT fname FROM employees WHERE LENGTH(fname) > 5;** <!-- command> This query retrieves the fname (first name) of employees from the employees table. The LENGTH(fname) function calculates the number of characters in each first name, and the WHERE clause filters the results to include only those names whose length is greater than 5. Only matching first names are displayed in the output.

## LEFT :

**SELECT LEFT('HELLO WORLD',6);** <!-- command> This query uses the LEFT() function to extract the first 6 characters from the string 'HELLO WORLD'. PostgreSQL starts from the leftmost character and returns exactly six characters, including spaces if they fall within the specified length. The output is HELLO (notice the space after HELLO).

## RIGHT :

**SELECT RIGHT('HELLO WORLD', 6);** <!-- command> This query uses the RIGHT() function to extract the last 6 characters from the string 'HELLO WORLD'. PostgreSQL starts from the rightmost character and returns exactly six characters, including spaces if they are part of the selected portion. The output is WORLD, where the first character is a space.

## TRIM :

**SELECT TRIM('   HELLO WORLD   ');** <!-- command> This query uses the TRIM() function to remove all extra spaces from the beginning and end of the string ' HELLO WORLD '. The spaces surrounding the text are removed, while the spaces inside the string remain unchanged. The final output is HELLO WORLD.

# FUNCTION INSIDE A FUNCTION :

**SELECT LENGTH(TRIM('  H '));** <!-- command> output : 1

## POSITION :

**SELECT POSITION('om' in 'Thomas');** <!-- command> This query uses the POSITION() function to search for the substring 'om' within the string 'Thomas'. PostgreSQL returns the position where the substring first begins, counting characters from 1. Since 'om' starts at the 3rd character, the output is 3.