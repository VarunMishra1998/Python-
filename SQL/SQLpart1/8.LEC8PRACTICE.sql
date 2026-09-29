CREATE DATABASE IF NOT EXISTS college;

USE college;

CREATE TABLE teacher (

 id INT PRIMARY KEY,
 name VARCHAR (50),
 subject VARCHAR (50),
 salary INT 
 
 );
 
 INSERT INTO teacher
 (id, name, subject, salary)
 VALUES
 (23, "ajay", "math", 50000),
 (47, "bharat", "english", 60000),
 (18, "chetan", "chemistry", 45000),
 (9, "divya", "physics", 75000);
 
 #select the teacher whose salary is above 55k
 SELECT * FROM teacher
 WHERE 
 salary > 55000;
 
 #rename the salary column of teacher table to ctc
 ALTER TABLE teacher
 CHANGE COLUMN salary ctc INT;
 
 #Update salary of all teachers by giving them an increment of 25%
 UPDATE teacher
 SET ctc = ctc + ctc * 0.25;
 
 
 /*#add a new column for teachers called city.
 the default city should be "Gurgaon"*/
 ALTER TABLE teacher
 ADD COLUMN city VARCHAR (50) DEFAULT "Gurgaon";
 
 
 #Delete the salary for teacher table
 ALTER TABLE teacher
 DROP COLUMN ctc;
 
 SELECT * FROM teacher;
 