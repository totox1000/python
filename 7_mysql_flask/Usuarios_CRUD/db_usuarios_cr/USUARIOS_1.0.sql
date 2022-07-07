INSERT INTO users (first_name, last_name, email)
VALUES ("Andres", "Dion","andresbcrr@gmail.com"),
("Mr. Nibbles", "Pancakes","totox1000@gmail.com"),
("Benny Bob", "McBob","pericopalotes@gmail.com");

SELECT * FROM users;

SELECT * FROM users
WHERE email = "andresbcrr@gmail.com";

SELECT * FROM users
WHERE id = 3;

UPDATE users SET last_name = "Pancakes"
WHERE users.id = 3;

DELETE FROM users
WHERE users.id = 2;

SELECT * FROM users
ORDER BY first_name DESC;

