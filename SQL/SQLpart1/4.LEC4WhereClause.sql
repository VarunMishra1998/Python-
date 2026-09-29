
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


SELECT * FROM users
WHERE
followers >= 200;

SELECT name , followers FROM users
WHERE
followers >= 200;

SELECT name, age FROM users
WHERE
age < 16;

/*where clause
OPERATORS
1.arithmatic operators(+,-,*,/,%)
2.comparision operators(=,!=,>,>=,<,<=)
3.logical opereators operators(AND,OR,NOT,IN,BETWEENM,ALL,LIKE,ANY)
4.Bitwise operators(&-->(Bitwise AND),|-->(Bitwise OR))
*/

/*yaha par batana hai kaun sa user hai
jisaki age 1 sal bad 18 ho jayegi*/
SELECT  name,age FROM users
WHERE
age + 1 = 18;


/*hame aise users ki information chahiye jinki age
15 se upar ho aur followers 200 ke upar ho*/
##AND operators
#(in and operators both conditions should be true)
SELECT  name,age ,followers FROM users
WHERE
age > 15 AND followers > 200;

##OR operators
#(any one condition should be true)
SELECT name,age,followers FROM users
WHERE 
age > 15 OR followers > 200;
/*is case donald ka age 15 se upar
but followers 200 se upar nhi hai phir bhi
data print hoga kyoki ek condition true hai
 */
 
 ##BETWEEN operators(select for a given range)
 /*ham chahate hai ki unhi ka data print hi
 jinka age 15 aur 17 ke bich me ho*/
 
SELECT name,age,followers FROM users
WHERE 
age BETWEEN 15 AND 17;

#IN operators(mathes any value in the range)
/*man lo hamare pas ek list hai jisame user ka email id hai
ham apne naye list ko existing list se match karenge ki kya 
hamare list me vo email hai jo pahale vale list me diya hai
agar nhi bhi diya rahega to koi error nhi aayega example like*/
SELECT name,age,followers FROM users
WHERE 
email IN ("donald@yahoo.in", "bob@yahoo.in" , "abc@yahoo.in");

#agar ham chahe to aur data add kar sakte hai like 
INSERT INTO users
(id, age, name, email, followers, following)
VALUES
(5, 14, "eve", "eve@yahoo.in", 400, 145),
(6, 16, "farah", "farah@yahoo.in", 10000, 1000);

/*hame us users ki data chahiye jinka age 14 ya 16 hai*/
SELECT name,age,followers FROM users
WHERE 
age IN (14,16);

##NOT operator (to negate the given condition)
/*hame us users ki data chahiye jinka age 14 ya 16 nhi hai*/
SELECT name,age,followers FROM users
WHERE 
age NOT IN (14,16);

#LIMIT CLAUSE
/*Sets an upper limit on number 
of (tuples) rows to be returned

SELECT col1,col2 FROM table_name
LIMIT number;
*/
SELECT name,age,followers FROM users
WHERE 
age > 14
LIMIT 2;
/*YAHA par 14 sal se bade bahut log hai but hame keval
2 logo ka data chahiye isiliye limit 2 laga diya */

#ORDER BY CLAUSE
#TO short in ascending (ASC) or descending order(DESC)
/*SELECT col1,col2 FROM table_name
ORDER BY col_name(s) ASC;*/

SELECT name, age, followers
FROM users
ORDER BY followers ASC;
#OR
SELECT name, age, followers
FROM users
ORDER BY followers;
/*ASC nhi likhenge phir bhi followers ka
order ascending me hoga*/

SELECT name, age, followers
FROM users
ORDER BY followers DESC;

#AGREEGATE FUNCTIONS
/*AGGREGATE fumctions pirfotm a calculation 
on a set of values , and return a single
value.
1.COUNT()
2.MAX()
3.MIN()
4.SUM()
5.AVG()
EXAMPLE:
SELECT max(marks)
FROM users;
*/
SELECT max(followers)
FROM users;
SELECT max(age)
FROM users;
/*yah ham ye find karenge ki 
aise kitane log hai 
jinka age 14 hai*/
SELECT count(age)
FROM users
WHERE age = 14;
SELECT avg(followers)
FROM users;
SELECT sum(followers)
FROM users;
SELECT avg(age)
FROM users;

#GROUP BY CLAUSE
/*Group rows that have the same
 values into summary rows
it collects deata from multiple records and
 groups the tesult by one or more column
 SELECT colq,col2
 FROM table_name
 GROUP BY col_names(s);*/
 #generally we use group by with some aggregate
 #function
SELECT  count(id)
FROM users
GROUP BY age;
/*Table ko age ke according groups me divide karo
👉 Har age group me kitne id (users) hain wo count karo
Simple words me:
Har age ke kitne users hain — ye bata raha hai.*/
SELECT age, count(id)
FROM users
GROUP BY age;

/*kis age vale ke maximum followers hai 
usko print karega*/
SELECT age, max(followers)
FROM users
GROUP BY age;

SELECT name,age, max(followers)
FROM users
GROUP BY name,age;

SELECT name , count(age)
FROM users
WHERE age=14
GROUP BY name,age;

#HAVING CLAUSE
/*Similar to where clause i.e 
applies some condition on rows.
But it is used when we want to
 apply any condition after grouping.
 
SELECT col1,col1
FROM table_name
GROUP BY col_name(s)
HAVING condition;*/
/*WHERE is for the table ,HAVING is for a group
Grouping is necessary for HAVING*/

SELECT age, max(followers)
FROM users
GROUP BY age
HAVING max(followers) > 200;
#ham having group by ke bad hi laga sakate hai

#GENERAL ORDER 
/*SELECT colums(s)
FROM table_name
WHERE condition
HAVING condition
ORDER BY column(s) ASC*/

SELECT age, max(followers)
FROM users
GROUP BY age
HAVING max(followers) > 200
ORDER BY age  ASC;

SELECT age, max(followers)
FROM users
GROUP BY age
HAVING max(followers) > 200
ORDER BY age  DESC;











 
 




CREATE TABLE post(
 id INT PRIMARY KEY,
 content VARCHAR (100),
 user_id INT,
 FOREIGN KEY (user_id) REFERENCES users (id)
);




