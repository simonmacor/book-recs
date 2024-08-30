CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    theme VARCHAR(100),
    period VARCHAR(100),
    style VARCHAR(100)
);

CREATE TABLE preferences (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    theme VARCHAR(100),
    period VARCHAR(100),
    style VARCHAR(100)
);
