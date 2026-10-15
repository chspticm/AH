CREATE DATABASE IF NOT EXISTS ah_music;
USE ah_music;

CREATE TABLE IF NOT EXISTS tracks (
    track_id INT PRIMARY KEY,
    track_title VARCHAR(100) NOT NULL,
    artist VARCHAR(80) NOT NULL,
    album VARCHAR(100) NOT NULL,
    genre VARCHAR(40) NOT NULL,
    duration_seconds INT NOT NULL,
    release_year SMALLINT NOT NULL
);

INSERT INTO tracks (track_id, track_title, artist, album, genre, duration_seconds, release_year) VALUES
(1, 'Morning Train', 'The Paper Kites', 'Open Roads', 'Indie', 214, 2020),
(2, 'Blue Harbour', 'Northbound', 'Tide Lines', 'Rock', 198, 2018),
(3, 'Quiet Machines', 'Mina Vale', 'Small Signals', 'Electronic', 242, 2022),
(4, 'June Again', 'The Paper Kites', 'Open Roads', 'Indie', 186, 2020),
(5, 'Long Way Home', 'Arlo Finch', 'Night Maps', 'Folk', 231, 2019),
(6, 'Soft Current', 'Mina Vale', 'Small Signals', 'Electronic', 205, 2022),
(7, 'Window Seat', 'Luca Grey', 'Passing Towns', 'Pop', 173, 2023),
(8, 'After the Rain', 'Northbound', 'Tide Lines', 'Rock', 227, 2018);

SELECT * FROM tracks;
