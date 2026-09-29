#DATABASE QUERIES/COMMANDS

CREATE DATABASE college;

CREATE DATABASE IF NOT EXISTS college;
/*ye tabhi create hoga jab hamara college nam
ka database exist nhi karega agar exist karega to warning aayega na ki error*/

DROP DATABASE college;

DROP DATABASE IF EXISTS college;
/*ye tabhi delete karega jab college nam
 ka database exists karega*/
 
 SHOW DATABASES;
 /*Iska use karake ham database ko search
 kar sakte hai like college...*/
 
 #IF I NEED TO CHECK DATABSE TABLES THEN
 
 USE college;
 SHOW TABLES;
 /*AGAR TABLE HOGA KOI COLLEGE KE ADAR TO DIKHEGA*/