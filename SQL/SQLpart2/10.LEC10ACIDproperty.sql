CREATE DATABASE prime;
 -- drop database prime;

USE prime;

CREATE TABLE accounts (
 id INT PRIMARY  KEY AUTO_INCREMENT,
 name VARCHAR(50),
 balance DECIMAL(10,2)
);

INSERT INTO accounts 
(name,balance)
VALUES
('adam',500.0),
('Bob', 300.00),
('Charlie', 1000.00);



-- transactions
SET autocommit = 0;

START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id = 1;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;

COMMIT;

SELECT * FROM accounts;

-- ROLLBACK

START TRANSACTION;

UPDATE accounts SET balance = balance - 50 WHERE id = 1;
COMMIT;
UPDATE accounts SET balance = balance + 50 WHERE id = 2;

ROLLBACK;

/*rollback sirf commit vale ko hi 
change karata hai uncommit vale ko nhi
abhi id1 me adam ke pas 450rs balance hai agr mai 
id1 ke bad commit likh ke run karaunga to 450 me se 400
bachega but uncommit vale me koi changes nhi hoga
EK bat aur iske pahale SET AUTOCOMIT=0; likhana hoga nhi 
uncommit vala bhi commit ho jayega means change ho jayega
agar ham chahate hai dono change ho commit likhane ke bad bhi 
to hame set autocommit = 1; likhana padega
tranction me whole data run karana hota hai*/

-- SAVEPOINTS
/*
🎯 Real Life Example (Wallet App)

Socho tum wallet app bana rahe ho.

Steps:

Wallet recharge ₹1000
Reward ₹10 add
Reward me error aa gaya

Ab kya karoge?

❌ Pura transaction cancel? (galat)
✅ Sirf reward wala step undo.

👉 Yahi SAVEPOINT karta hai.
*/
SET autocommit = 0;

START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;

UPDATE accounts SET balance = balance + 10 WHERE id = 1;
-- error (10rs cashback not came)

ROLLBACK TO after_wallet_topup;

COMMIT;
 


SELECT * FROM accounts;

