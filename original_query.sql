DROP TABLE IF EXISTS movie_rented_by CASCADE;
DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS salutations CASCADE;
DROP TABLE IF EXISTS movies CASCADE;
CREATE TABLE salutations(
    salutation_id SERIAL PRIMARY KEY,
    salutation TEXT
);
INSERT INTO salutations (salutation)
VALUES ('Ms'),
    ('Mr');
CREATE TABLE customers(
    cust_id SERIAL,
    full_name TEXT,
    physical_address TEXT,
    PRIMARY KEY(cust_id),
    salutation_id INTEGER,
    FOREIGN KEY (salutation_id) REFERENCES salutations (salutation_id)
);
INSERT INTO customers (full_name, physical_address, salutation_id)
VALUES ('Janet Jones', 'First Street Plot No 4', 1),
    ('Robert Phil', '3rd Street 34', 2),
    ('Robert Phil', '5th Avenue', 2);
CREATE TABLE movies(
    movie_id SERIAL PRIMARY KEY,
    title TEXT
);
INSERT INTO movies (title)
VALUES ('Pirates of the Caribbean'),
    ('Clash of the Titan'),
    ('Forgetting Sarah Marshal'),
    ('Daddys Little Girls');
CREATE TABLE movie_rented_by(
    rent_id SERIAL PRIMARY KEY,
    cust_id INT,
    FOREIGN KEY (cust_id) REFERENCES customers (cust_id),
    movie_id INT,
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);
INSERT INTO movie_rented_by (cust_id, movie_id)
VALUES (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 2);