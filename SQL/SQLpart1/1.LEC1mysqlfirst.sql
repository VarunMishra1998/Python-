/*this is first command how to create databse,
table and how to add data into table*/

#create database

CREATE DATABASE college;

/*to delete database use 
"drop database college"*/

USE college;

#create table

CREATE TABLE student(
 rollno INT,
 name VARCHAR (30),
 age INT

);
 #enter data into table
 
 INSERT INTO student
 VALUES
 (101, "adam",12),
 (102, "bob", 14);
 
 SELECT * FROM student;