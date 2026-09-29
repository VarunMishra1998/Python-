#table queries

/*CREATE TABLE table_name(
column_name1 datatypes constraints
column_name2 datatypes contraints,
);

name-->INT
AGE--->VARCHAR(20)
EMAIL-->VARCHAR(30)
FOLLOWERS-->INT
FOLLOWING--->INT
*/

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
 #age_check contraint name
 #aur isko ham aise bhi likh sakate hai...
 -- CONSTRAINT CHECK (age >= 13)
);

#USE CONSTRAINTS

/*RULES FOR DATA IN TABLE
NOT NULL   columns can not have a null values
UNIQUE     all values in column are different
DEFAULT    sets the default value of a column
CHECK      it can limit the values allowed in a column

salary INT DEFAULT 250000

CONTRAINTS age_check CHECK (age >= 18 AND city = "Delhi")

#CONSTRAINT 

PRIMARY KEY -->  make a column unique and not null but osed only for one
CREATE TABLE temp(
id int not null,
PRIMARY KEY (id)
);

FOREIGN KEY --> prevent action that would destroy links between tables
CREATE TABLE temp (
cust_id int,
FOREIGN KEY (cust_id) references customer(id)
);
*/

CREATE TABLE post(
 id INT PRIMARY KEY,
 content VARCHAR (100),
 user_id INT,
 FOREIGN KEY (user_id) REFERENCES users (id)
);

##ham ise reverseengineering karake visualize bhi  kar sakate hai

/*WHAT ARE KEYS
keys are special columns in the table

PRIMARY KEY-->
It is acolumn(or set of columns) in a table 
that uniquely identifies each row .(unique id)
There is only one PK & it should be NOT null.alter

FOREIGN KEY-->
A foreign key is a column (or ser of columns) in a table
 that refers to the primary key in another table. 
 There can be multiple FKs.

*/

#data insert into table
/* INSERT INTO table_name
(column1,column2.....)
VALUES
(col1_v1,col2_v1)
(col1_v1,col2_v1)
if column1 name is id and column2 name is age 
then in VALUES first should come Id no. and second 
age because order is important here
*/

INSERT INTO users
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob@yahoo.in", 200, 200),
(3, 16, "casey", "casey@yahoo.in", 300, 306),
(4, 17, "donald", "donald@yahoo.in", 200, 105);

/*ham yaha par ek aur data same id ka 
insert karana chahenge to hame error batayega 
ki dublicate entry hai example like */

INSERT INTO users
(id, age, name)
VALUES
#yaha par id same hai
(1, 20, "random");

/*agar ham yha par name nhi lete hai but hamare
table user me name ka contraint NOT NULL likha hai
to jab nhi ham run karenge command ko without name 
to error aayega vaha likhega fild name does't have a
default value example like*/
INSERT INTO users
(id, age)
VALUES
#yaha par id same hai
(1, 20);

/*agar yha par same email age bhi lenge to error dega*/

/*SELECT COMMANDS 
selects and show data from DB
syntax
SELECT col1,col2 FROM table_name;

to show all table
SELECT * FROM table_name;
*/

SELECT id , age FROM users;
SELECT * FROM users;

#for UNIQUE DATA access
#keval id print hoga age lenge to
#keval age print hoga column ka

SELECT DISTINCT id FROM users;


