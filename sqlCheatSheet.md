-- CREATE: Make the table and add a record
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO users (name, email)
VALUES ('Alice', 'alice@example.com');

-- READ: Get all or specific records
SELECT * FROM users; -- all
SELECT * FROM users WHERE id = 1; -- specific

-- UPDATE: Modify a record
UPDATE users
SET email = 'alice.new@example.com'
WHERE id = 1;

-- DELETE: Remove a record
DELETE FROM users
WHERE id = 1;
