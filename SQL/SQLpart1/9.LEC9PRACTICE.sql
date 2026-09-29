CREATE DATABASE college;

USE college;

CREATE TABLE student(
rollno INT PRIMARY KEY,
name VARCHAR (30),
city VARCHAR (30),
marks INT

);

INSERT INTO student
(rollno, name, city, marks )
VALUES
(110, "adam", "Delhi", 76),
(118, "bob", "Mumbai", 65),
(124, "casey", "Pune", 94),
(112, "duke", "Pune", 80);

#select all student who scored 75+
SELECT  * FROM student
WHERE 
marks > 75;

#find the names of all cities where students are from
SELECT DISTINCT city FROM student;
#OR
SELECT city
FROM student
GROUP BY city;

#find the maximum marks of students from each city
SELECT city , max(marks)
FROM student
GROUP BY city;

#find the average of the marks
SELECT avg(marks)
FROM student;


/* #add a new column grade,assign grade such that:
          marks > 80 , grade = O
          marks 70-80 , grade = A
          marks 60-70 , grade = B */

ALTER TABLE student
ADD COLUMN grade VARCHAR(2); 

UPDATE student
SET grade = "O"
WHERE marks >= 80;

UPDATE student
SET grade = "A"
WHERE marks > 70 AND marks < 80;         

UPDATE student
SET grade = "B"
WHERE  marks > 60 AND marks < 70; 

SET SQL_SAFE_UPDATES = 0;       



        
SELECT * FROM student;



