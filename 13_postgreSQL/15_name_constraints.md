 
Named Constraint :

A named constraint is a database constraint that you explicitly give a name to, instead of letting the database generate one automatically. Its usefull for debugging and when postgreSQL logging an error, this saves a lot of time and easy to handle edge cases.

SELECT * FROM person;

ALTER TABLE person
ADD CONSTRAINT mob_no_less_than_10dig 
CHECK(LENGTH(mob) >= 10);

INSERT INTO person(mob) 
VALUES(123); <!-- command> 