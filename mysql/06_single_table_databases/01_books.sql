CREATE DATABASE IF NOT EXISTS ah_books;
USE ah_books;

CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(80) NOT NULL,
    genre VARCHAR(40) NOT NULL,
    publication_year SMALLINT NOT NULL,
    copies_available INT NOT NULL
);

INSERT INTO books (book_id, title, author, genre, publication_year, copies_available) VALUES
(1, 'The Clockwork Garden', 'Mira Patel', 'Fantasy', 2019, 3),
(2, 'Signals from Mars', 'Evan Cole', 'Science fiction', 2021, 2),
(3, 'A River in Winter', 'Nadia Ross', 'Drama', 2017, 1),
(4, 'The Last Lighthouse', 'Jamie Reid', 'Mystery', 2020, 4),
(5, 'Small Worlds', 'Leah Grant', 'Science', 2022, 2),
(6, 'Paper Satellites', 'Owen Park', 'Adventure', 2018, 0),
(7, 'The Glass Violin', 'Amira Khan', 'Mystery', 2023, 5),
(8, 'Beneath the Old Oak', 'Callum Fraser', 'Fantasy', 2016, 1);

SELECT * FROM books;
