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
 
 -- VIEWS in sql
 /*
 A views is a virtul table based 
 on the result-set of an SQL
 SYNTAX-
 CREATE VIEW view AS
 SELECT col1,col2 from table_name;
 A view always shows up-to-date data
 the database engine recreate the view,
 every time a user queries it.
 
 */
 CREATE VIEW view1 AS
 SELECT customer_id, name FROM customers;
 
 
 SELECT * FROM view1;
 -- filtering in view1
 SELECT * FROM view1 WHERE name= 'Alice';
 
 -- ham view ko multiple table se 
 -- bhi creaate kar sakate hai
 -- and join se bhi create kar sakate hai 
 
 CREATE VIEW view1 AS
 SELECT * 
 FROM customers c
 INNER JOIN orders o
 ON c.customer_id = o.order_id;
 /*
 error- duplicate columns name 'customer_id'
 kyoki customers aur orders table me same column hai 
 customer_id name se isliye hame select karna padega
 
 ham view ko drop bhi kar sakate hai
 #DROP VIEW view1;
 */
 CREATE VIEW view2 AS
 SELECT c.customer_id, c.name, o.order_id
 FROM customers c
 INNER JOIN orders o
 ON c.customer_id = o.customer_id;
 /*yaha ham usi customers ka data chahate 
 hai jinka order value available hai*/
 
 
 
 SELECT * FROM view2;
 
 -- VIEWS IN SQL
 /*-- No data stored physically
 matalab View ke andar actual rows/database
 data save nahi hota.
 Sirf SQL query save hoti hai.
 -- can include columns from one or more tables
 -- can be used in SELECT,JOIN,or even WHERE clauses like a normal table
 -- helps with security by exposing only certain columns to users
 */
 
 
 
 
 
 
 
 
 