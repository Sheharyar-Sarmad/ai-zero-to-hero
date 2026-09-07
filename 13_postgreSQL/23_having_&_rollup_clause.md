

# HAVING Clause : 

> The HAVING clause is used to filter the results of a query after rows have been grouped by an aggregate function (like SUM, COUNT, AVG, MAX, or MIN). Think of it as a WHERE clause, but specifically designed for groups rather than individual rows.

## WHERE vs. HAVING:

**The Golden Rule**
> WHERE filters individual rows before grouping happens. It cannot see aggregate values.
> HAVING filters summary rows after grouping happens.

# Example : 

> This query will give an error because GROUPING is done before the WHERE clause but if we use HAVING clause we will get our desired result.

SELECT p_name, SUM(total_price) FROM billing_info_materialized
     GROUP BY p_name
	 WHERE SUM(total_price) > 1500;



> This is a valid query. 

SELECT p_name, SUM(total_price) FROM billing_info_materialized
     GROUP BY p_name
	 HAVING SUM(total_price) > 1500;

# ROLLUP : 

> The ROLLUP clause is an extension of the GROUP BY clause in SQL **[ROLLUP-extension]**. It allows you to generate multiple levels of grouping and subtotals within a single query, along with a grand total **[ROLLUP-extension]**. Instead of writing multiple separate queries with GROUP BY and combining them with UNION, ROLLUP does all the heavy lifting in a single, highly efficient database scan 
**[ROLLUP-extension]**.

# Example :

> This will give grand total count of all the total prices.

SELECT p_name, COUNT(total_price) FROM billing_info_materialized
     GROUP BY ROLLUP(p_name)
	 ORDER BY SUM(total_price);

> This will give grand total sum of all total prices.

SELECT p_name, SUM(total_price) FROM billing_info_materialized
     GROUP BY ROLLUP(p_name)
	 ORDER BY SUM(total_price);

# Issue :

> The grand total name will be Null so we can fill it like that.
> The COALESCE(p_name, 'total') means if any Null values comes in the p_name then fill it with 'total' just.

SELECT 
     COALESCE(p_name, 'total')
     p_name,
	 COUNT(total_price)
FROM billing_info_materialized
     GROUP BY ROLLUP(p_name)
	 ORDER BY SUM(total_price);

