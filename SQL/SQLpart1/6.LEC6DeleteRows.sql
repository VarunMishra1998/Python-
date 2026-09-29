
CREATE DATABASE instagram ;


USE instagram;

CREATE TABLE users(
 id INT PRIMARY KEY,
 age INT,
 name VARCHAR(30) NOT NULL,
 email VARCHAR(50) UNIQUE,
 followers INT DEFAULT 0,
 following INT,
 CONSTRAINT age_check CHECK (age >= 13)
 );
 
 /*WHERE CLAUSE
 to definr conditions  
 SELECT col1,col2 FROM table_name
 WHERE codition
 */
 INSERT INTO users
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob@yahoo.in", 200, 200),
(3, 16, "casey", "casey@yahoo.in", 300, 306),
(4, 17, "donald", "donald@yahoo.in", 200, 105);


INSERT INTO users
(id, age, name, email, followers, following)
VALUES
(5, 14, "eve", "eve@yahoo.in", 400, 145),
(6, 16, "farah", "farah@yahoo.in", 10000, 1000);

#UPDATE
/*Tp update existing rows
SET col1=val1,col2=val2
WHERE condition
*/

UPDATE users
SET followers=600
WHERE age = 16;
/*jab ham ise try karenge update ke liye to error aayega
to hame ek aur command likhana padega like */
SET SQL_SAFE_UPDATES = 0;

#DELETE
#(delete existing rows)
/*DELETE FROM table_name
WHERE condition*/

DELETE FROM users
WHERE age = 14;
/*agar ham WHERE clause nhi likhange to 
hamra sara rows delete ho jayega*/

SELECT * FROM users;

CREATE TABLE post(
 id INT PRIMARY KEY,
 content VARCHAR (100),
 user_id INT,
 FOREIGN KEY (user_id) REFERENCES users (id)
);

