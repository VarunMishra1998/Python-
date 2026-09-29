-- INDEx IN SQL
/*Indexes are special database objects 
that make 'data retrieval faster'.

syntax (single col & multi-col/composite index)

CREATE 	INDEX idx_name ON table(col);
CREATE INDEX idx ON table(col1,col2);

SHOW INDEX FROM table;
DROP INDEX idx_name ON table;

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
(3, 'Charlie', 700.00, 'Bangalore')]
(3, 'Charlie', 1000.00, 'Noida');

CREATE INDEX idx_branch ON accounts(branch);

SHOW INDEX FROM accounts;

SELECT *
FROM accounts
WHERE branch = 'Mumbai';

CREATE INDEX idx2 ON accounts (branch, balance);

SHOW INDEX FROM accounts;

DROP INDEX idx2 ON accounts;

SELECT * FROM accounts;





