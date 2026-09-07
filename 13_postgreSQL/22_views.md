

# Views : 

> Views are virtual(temporary) tables that do not physically store data; instead, they act as a saved SQL query that runs every time the view is referenced.

# Example : 

> Suppose i need this query a lot in my application so i have to right this query everytime or if i am working in a corporation the other devs will right it byself which is ot difficult super time consuming. Now developers and you can create views and access the query everytime whenever you want

SELECT 
    o.ord_id,
	c.cust_id,
	o.ord_date,
	p.p_name,
	p.price,
	oi.quantity,
    (oi.quantity * p.price) AS total_price
FROM order_items oi
    JOIN
	    products p ON oi.p_id=p.p_id
	JOIN
	    orders o ON o.ord_id=oi.ord_id
	JOIN 
	    customers c ON o.cust_id=c.cust_id;

## Creating Views :

CREATE VIEW billing_info AS
SELECT 
    o.ord_id,
	c.cust_id,
	o.ord_date,
	p.p_name,
	p.price,
	oi.quantity,
    (oi.quantity * p.price) AS total_price
FROM order_items oi
    JOIN
	    products p ON oi.p_id=p.p_id
	JOIN
	    orders o ON o.ord_id=oi.ord_id
	JOIN 
	    customers c ON o.cust_id=c.cust_id;

> Now the view is created and now can access it like: 

SELECT * FROM billing_info;

> See how much our time saves in 4 words instead of writing a query para everytime. But wait there's an important and much more good way than simple view because our goal is to not only get the work done our goal is to maintain the time and space complexity.

# Materialized Views : 

> A Materialized View is a database object that stores the results of a query physically on a disk, rather than running the query fresh every time you look at it **[Materialized-Views]**. Think of a standard view as a shortcut link to a query, while a materialized view is a cached snapshot of the query's output.

# Query Example : 

CREATE MATERIALIZED VIEW billing_info_materialized AS
SELECT 
    o.ord_id,
	c.cust_id,
	o.ord_date,
	p.p_name,
	p.price,
	oi.quantity,
    (oi.quantity * p.price) AS total_price
FROM order_items oi
    JOIN
	    products p ON oi.p_id=p.p_id
	JOIN
	    orders o ON o.ord_id=oi.ord_id
	JOIN 
	    customers c ON o.cust_id=c.cust_id;

> Retreiving output of view is same as standard view 

SELECT * FROM billing_info_materialized;

> A materialized view with a unique index gives you O(log N) lookup speed, which is effectively near O(1) in practice 
**[Materialized-Views]**.