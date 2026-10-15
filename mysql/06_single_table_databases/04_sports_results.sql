CREATE DATABASE IF NOT EXISTS ah_sports;
USE ah_sports;

CREATE TABLE IF NOT EXISTS match_results (
    result_id INT PRIMARY KEY,
    played_on DATE NOT NULL,
    home_team VARCHAR(50) NOT NULL,
    away_team VARCHAR(50) NOT NULL,
    home_score INT NOT NULL,
    away_score INT NOT NULL,
    venue VARCHAR(60) NOT NULL
);

INSERT INTO match_results (result_id, played_on, home_team, away_team, home_score, away_score, venue) VALUES
(1, '2026-08-12', 'Riverside', 'Hillview', 2, 1, 'Riverside Park'),
(2, '2026-08-19', 'Eastfield', 'Riverside', 0, 0, 'Eastfield Ground'),
(3, '2026-08-26', 'Hillview', 'Westport', 1, 3, 'Hillview Arena'),
(4, '2026-09-02', 'Westport', 'Eastfield', 2, 2, 'Westport Stadium'),
(5, '2026-09-09', 'Riverside', 'Westport', 1, 0, 'Riverside Park'),
(6, '2026-09-16', 'Eastfield', 'Hillview', 3, 1, 'Eastfield Ground'),
(7, '2026-09-23', 'Westport', 'Hillview', 0, 1, 'Westport Stadium'),
(8, '2026-09-30', 'Riverside', 'Eastfield', 2, 2, 'Riverside Park');

SELECT * FROM match_results;
