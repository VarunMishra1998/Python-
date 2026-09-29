-- SUB-QURIES
/*A subquery or Inner query or a Nested
  query is a quety within another SQL query.
  It involves 2 select statements.
  SYNTAX-->
  SELECT column(s)
  FROM table_name 
  WHERE col_name operator
  (subquery);
  
  🎯 Question:
Average salary se jyada 
salary wale employees lao
  subquery ham select , from, aur where ke 
  andar bhi likh sakate hai*/
  
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
 
/*here subquery 
inside WHERE 
*/ 

 SELECT * 
 FROM orders
 WHERE amount > (
 SELECT AVG (amount)
 FROM orders
 );
 
 /*kitane customers ne kitana order
 kiya hai ab ham use count karenge
 here subquery select
 inside SELECT*/
 
 -- corelated subquery
 SELECT name,
    (
       SELECT COUNT(*)
	   FROM orders o 
       WHERE o.customer_id = c.customer_id
       
    ) AS order_count
    /*yha par as order_count karake
    ek nya column banaya hai*/
    /*
    Simple rule:

SELECT ... AS name
→ column alias
FROM (subquery) AS name
→ table alias
    */
FROM customers c;

/*AVERAGE SPENDING*/

SELECT 
summary.customer_id,summary.avg_amount
FROM 
(
 SELECT customer_id , AVG(amount) AS avg_amount
 FROM orders
 GROUP BY customer_id
 
 )AS summary;
 
 SELECT c.name, COUNT(*)
FROM orders o
 JOIN customers c
ON o.customer_id = c.customer_id
GROUP BY c.name;
/*
Yaha:

summary = temporary table
customer_id aur avg_amount = uske columns
*/
 
 
 
 SELECT * FROM customers;
 SELECT * FROM orders;
 
 /*
 1. SELECT me subquery

Jab har row ke saath ek single value nikalni ho.

Example:

har customer ka order count

SELECT name,
(
   SELECT COUNT(*)
   FROM orders o
   WHERE o.customer_id = c.customer_id
) AS order_count
FROM customers c;

Yaha subquery:

har customer ke liye
ek value return kar rahi hai (3, 5, etc.)

Isliye SELECT me aayi.

2. FROM me subquery

Jab subquery ka result ek temporary table ki tarah use karna ho.

Example:

SELECT *
FROM
(
   SELECT customer_id, AVG(amount) AS avg_amount
   FROM orders
   GROUP BY customer_id
) AS summary;

Yaha inner query:

rows + columns return kar rahi hai
isliye table ban gayi

To FROM me likha.

3. WHERE me subquery

Jab filtering karni ho.

Example:

sirf un customers ko lao jinhone order kiya hai

SELECT name
FROM customers
WHERE customer_id IN
(
   SELECT customer_id
   FROM orders
);

Yaha subquery:

IDs ki list de rahi hai
outer query filter kar rahi hai

Isliye WHERE me.

Shortcut yaad rakho:

Place	Use
SELECT	ek value nikalni ho
FROM	temporary table banana ho
WHERE	filtering/checking karni ho

Simple thinking:

“Mujhe extra value chahiye?” → SELECT
“Mujhe temporary table chahiye?” → FROM
“Mujhe condition/filter lagana hai?” → WHERE
 */
  
  
  