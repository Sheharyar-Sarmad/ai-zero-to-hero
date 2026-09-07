
# Intro :

> We will be creating an ecommerce project a little one, you can try it by youself it should contain 4 tables customers, products, orders, order_items try to make it yourself or if you want to see then not just copy paste the command think it logically try to understand and rigth queries by youself.

# Working :

# Creating Customers Table : 

CREATE TABLE customers(
   cust_id SERIAL PRIMARY KEY,
   cust_name VARCHAR(100) NOT NULL
);

# Creating Orders Table : 

CREATE TABLE orders(
   ord_id SERIAL PRIMARY KEY,
   ord_date DATE NOT NULL,
   cust_id INTEGER NOT NULL,
   FOREIGN KEY (cust_id) REFERENCES customers (cust_id)
);

# Creating Products Table :

CREATE TABLE products (
   p_id SERIAL PRIMARY KEY,
   p_name VARCHAR(100) NOT NULL,
   price NUMERIC NOT NULL
);

# Creating Order_Items Table :

CREATE TABLE order_items (
   item_id SERIAL PRIMARY KEY,
   ord_id INTEGER NOT NULL,
   p_id INTEGER NOT NULL,
   quantity INTEGER NOT NULL,
   FOREIGN KEY (ord_id) REFERENCES orders(ord_id),
   FOREIGN KEY (p_id) REFERENCES products(p_id)
);

# Inserting Data : 

**Creating customers**

INSERT INTO customers (cust_name)
VALUES
    ('Raju'), ('Sham'), ('Paul'), ('Alex');

**Creating products**

INSERT INTO products (p_name, price)
VALUES
    ('Laptop', 55000.00),
    ('Mouse', 500),
    ('Keyboard', 800.00),
    ('Cable', 250.00);

**Creating orders**

INSERT INTO orders (ord_date, cust_id)
VALUES
    ('2024-01-01', 1),  -- Raju first order
    ('2024-02-01', 2),  -- Sham first order
    ('2024-03-01', 3),  -- Paul first order
    ('2024-04-04', 2);  -- Sham second order

**Creating order_items**

INSERT INTO order_items (ord_id, p_id, quantity)
VALUES
    (1, 1, 1),  -- Raju ordered 1 Laptop
    (1, 4, 2),  -- Raju ordered 2 Cables
    (2, 1, 1),  -- Sham ordered 1 Laptop
    (3, 2, 1),  -- Paul ordered 1 Mouse
    (3, 4, 5),  -- Paul ordered 5 Cables
    (4, 3, 1);  -- Sham ordered 1 Keyboard

# Retreiving Data : 

SELECT * FROM customers;

SELECT * FROM products;

SELECT * FROM orders;

SELECT * FROM order_items;

# Retreiving Product Name & Quantity In Orders : 

SELECT p.p_name, oi.quantity FROM order_items oi
    JOIN 
	    products p ON oi.p_id = p.p_id

# Product Details Report :

SELECT 
    p.p_name,
	oi.quantity,
	o.ord_date
	FROM order_items oi
    JOIN 
	    products p ON oi.p_id = p.p_id
    JOIN
	    orders o ON o.ord_id = oi.ord_id

# Full Invoice Report : 

SELECT
    c.cust_name,
    p.p_name,
	p.price,
	oi.quantity,
	o.ord_date
FROM order_items oi
    JOIN 
	    products p ON oi.p_id = p.p_id
    JOIN
	    orders o ON o.ord_id = oi.ord_id
	JOIN 
	    customers c ON o.cust_id = c.cust_id

# Checking Total Prices Spend By The Users : 

SELECT 
    c.cust_name,
    SUM(p.price * oi.quantity) AS total_spent
FROM order_items oi
    JOIN orders o ON o.ord_id = oi.ord_id
    JOIN customers c ON c.cust_id = o.cust_id
    JOIN products p ON p.p_id = oi.p_id
GROUP BY c.cust_name
ORDER BY total_spent DESC;

# Comprehensive Report :  

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
