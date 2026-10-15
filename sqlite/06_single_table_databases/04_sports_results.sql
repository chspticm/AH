CREATE TABLE IF NOT EXISTS match_results (
    result_id INTEGER PRIMARY KEY,
    played_on TEXT NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    home_score INTEGER NOT NULL CHECK (home_score >= 0),
    away_score INTEGER NOT NULL CHECK (away_score >= 0),
    venue TEXT NOT NULL
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
