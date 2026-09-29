
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
( to define conditions )  
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

#ALTER
/*ALTER (to change the schema)*

#ADD Column

ALTER TABLE table_name
ADD COLUMN column_name datatype constraint;

#DROP Column

ALTER TABLE table_name
DROP  COLUMN column_name;

#RENAME Table

ALTER TABLE table_name
RENAME TO new_table_name;

#CHANGE Coloumn (rename)

ALTER TABLE table_name
CHANGE COLUMN old_name new_name_datatype new_constaint;

#MODIFY Column (modify datatype/constraint)
ALTER TABLE  table_name
MODIFY col_name new_datatypes new_constraint;

*/


#add column
ALTER TABLE users
ADD COLUMN city VARCHAR(25) DEFAULT "delhi";

#DROP COLUMN
ALTER TABLE users
DROP COLUMN age;

#RENAME TABLE
ALTER TABLE users
RENAME TO istausers;
/*is command se ab hamare table ka nam "users"
se "istausers ho gya hai"*/
ALTER TABLE istausers
RENAME TO users;

#CHANGE COLUMN NAME
ALTER TABLE users
CHANGE COLUMN followers subs INT DEFAULT 0;
/*yaha par followers column name change into subs
*/

#MODIFY 
/*modify ke liye ham ek aur new data enter karayenge aur 
yah par hame subs me default value 5 rakhana hai 
ham subs is liye likh rahe hai kyoki followers ka nam ab subs hai
AUR ham deta me age nhi lenge kyoki age ko delete kar diya hai
pahale hame default value 5 vala line run karan hai tab usake bad
select from users run karana phir insert value vala line run karake tab phir 
select from users karna hai*/

INSERT INTO users
(id, name, email, following)
VALUES
(8,  "gem", "gem@yahoo.in", 125);


ALTER TABLE users
MODIFY subs INT DEFAULT 5;

#TRUNCATE
#(to delete tables data)
/*JAB ham truncate command apply karenge to error aayega 
truncate nhi hoga kyoki isame post nam ka ek aur table hai jo users nam ke 
table se connect hai kyoki users table ka id as foreign key use hua hai post table me
to hane connection break karana padega to hame drop post table karana hoga phir
truncate karenge to ho jayega data delete table ka*/


/drop karane se pura table delete hota hai but truncate
command se keval table ka data delete hota hai/

SELECT * FROM users;






CREATE TABLE post(
 id INT PRIMARY KEY,
 content VARCHAR (100),
 user_id INT,
 FOREIGN KEY (user_id) REFERENCES users (id)
);









