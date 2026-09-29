-- Stored procedures
/*
Predefined set of SQL statements that you can say in 
the database and execute whenever needed.
syntax(Create)
CREATE PROCEDURE procedure_name (parameter)
BEGIN
 -- SQL statements
 IND;
*/

CREATE DATABASE prime;

USE prime;


CREATE TABLE accounts (
account_id INT PRIMARY KEY,
name VARCHAR (50),
balance DECIMAL(10, 2),
branch VARCHAR (50)
);

INSERT INTO accounts 
VALUES
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 5300.00, 'Delhi'),
(3, 'Charlie', 700.00, 'Bangalore'),
(4, 'David', 1000.00, 'Noida');

/*
CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
SELECT balance
FROM accounts
WHERE account_id = acc_id;
END;
/*This code gives an error because MySQL treats ';' as the end of the statement.
Inside a stored procedure there are multiple ';' symbols,
 so we need to change the delimiter before creating the procedure.*/
 
 -- delimiter
 /*(//) place of this we can alse use ($$)*/
-- // or $$ is used as a temporary delimiter (separator) in MySQL

-- account_id se balance ko batana hai
 DELIMITER //

CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
    SELECT balance
    FROM accounts
    WHERE account_id = acc_id;
END //

DELIMITER ;

-- CALL
CALL check_balance(2);

/*
-- IN = input parameter
-- acc_id = parameter/variable name
-- INT = datatype of parameter

-- CALL check_balance(101);
-- Here 101 gets stored in acc_id

-- WHERE account_id = acc_id;
-- means:
-- WHERE account_id = 101;
to ban jayega UR 5000 RETURN HO JAYEGA
*/

-- OUT THE VLAUE means output/result from procedure

DELIMITER //

CREATE PROCEDURE check_balance1(IN acc_id INT , OUT bal DECIMAL(10 , 2))
BEGIN
    SELECT balance INTO bal
    FROM accounts
    WHERE account_id = acc_id;
END //

DELIMITER ;

-- CALL
CALL check_balance1(1 , @balance);
SELECT @balance;
/*
OUT bal DECIMAL(10,2) = output variable 
(balance return karega)
phir balance ki value uthakar out variable 'bal'
me store karate hai
@balance ke andar bal ki value store hoti hai

---
bal aur @balance same cheez nahi hain.

1) bal
- Ye stored procedure ka OUT parameter hai
- Procedure ke andar use hota hai
- Temporary variable jaisa kaam karta hai (inside procedure)

2) @balance
- Ye user-defined session variable hai (MySQL variable)
- Procedure ke bahar use hota hai
- CALL karte time output ko store karne ke liye use hota hai

Simple flow:
procedure ke andar value → bal me store hoti hai
procedure ke bahar value → @balance me aati hai
*/
-- to drop procedure
#drop procedure if exist check_balance

SELECT * FROM accounts;