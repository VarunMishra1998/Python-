-- practice question

CREATE DATABASE prime;
 
 USE prime;
 
 CREATE TABLE  customers (
 customer_id INT PRIMARY KEY,
 name VARCHAR (50),
 city VARCHAR (50)
 );
 
 INSERT INTO customers VALUES
 (1, 'Alice', 'Mumbai'),
 (2, 'Bob', 'Delhi'),
 (3, 'Charlie', 'Banglore'),
 (4, 'David', 'Mumbai');
 
 CREATE TABLE orders (
 order_id INT PRIMARY KEY,
 customer_id INT,
 amount INT
 );
 
 INSERT INTO orders VALUES
 (101, 1, 500),
 (102, 1, 900),
 (103, 2, 300),
 (104, 5, 700);
 
 SELECT *
 FROM customers as A
 LEFT JOIN orders as B
 ON A.customer_id = B.customer_id;
 
 -- left exclusive join
 SELECT *
 FROM customers as A
 LEFT JOIN orders as B
 ON A.customer_id = B.customer_id
 WHERE B.customer_id is NULL;
 /*
 💡 Easy yaad rakhne ka trick:
LEFT JOIN → sab left + matching right
LEFT EXCLUSIVE → sirf unmatched left (minus matching)
for rexclusive 
 */
 
 SELECT *
 FROM customers as A
 RIGHT JOIN orders as B
 ON A.customer_id = B.customer_id
 WHERE A.customer_id is NULL;
 
 SELECT * FROM customers;
 SElECT * FROM orders;
 