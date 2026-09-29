-- JOINs
/*joins are used to combine rows from two or
 more tables based on arelated column between them
 1.inner joine 
 2.left join   }
 3.right join  } --->ye tino outer joins hote hai
 4.full join   }     
 */-- 
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
 
 -- INNER JOIN
 SELECT *
 FROM customers c 
 INNER JOIN orders o
 ON c.customer_id = o.customer_id; 
 
 -- if we want specific column then 
 SELECT c.customer_id, o.order_id, c.name
 FROM customers c
 INNER JOIN orders o
 ON c.customer_id = o.customer_id;
 
 -- LEFT JOIN / LEFT OUTER JOIN
 /*left table(B) ki sari value lega aur right 
 table(A) ki keval matching value lega*/
 
 SELECT *
 FROM customers c
 LEFT JOIN orders o
 ON c.customer_id = o.customer_id;
 
 -- right join
 /*B table ka sara value aayega aur A 
 table ka matching value aayega*/
 SELECT * 
 FROM customers c
 RIGHT JOIN orders o
 ON c.customer_id = o.customer_id;
 
 -- OUTER JOIN (left join UNION right join)
 
 SELECT *
 FROM customers c
 LEFT JOIN orders o
 ON c.customer_id = o.customer_id
 UNION
 SELECT *
 FROM customers c
 right JOIN orders o
 ON c.customer_id = o.customer_id;
 
 -- CROSS JOIN
 /*Every row of the first table 
   is combined with
   Every row of the second table.*/
   
 SELECT *
 FROM customers 
 CROSS JOIN orders;
 
 -- SELF JOIN
 
 /*It is aregular join
 but the table is join 
 with itself
 🔸 Simple example:

Maan lo ek Employees table hai:

emp_id	name	manager_id
1	Rahul	3
2	Amit	3
3	Suresh	NULL

Yahan:
Rahul aur Amit ka manager Suresh hai
Manager bhi isi table me ek employee hai
o/p-
| employee | manager |
| -------- | ------- |
| Rahul    | Suresh  |
| Amit     | Suresh  |
*/
 
 SELECT *
 FROM customers as A
 JOIN customers as B
 ON A.customer_id = B.customer_id;
 
 
 
 SELECT * FROM customers;
 SELECT * FROM orders;
 
 
