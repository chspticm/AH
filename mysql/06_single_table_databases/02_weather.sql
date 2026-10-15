CREATE DATABASE IF NOT EXISTS ah_weather;
USE ah_weather;

CREATE TABLE IF NOT EXISTS weather_readings (
    reading_id INT PRIMARY KEY,
    station VARCHAR(50) NOT NULL,
    observed_on DATE NOT NULL,
    temperature_c DECIMAL(4,1) NOT NULL,
    rainfall_mm DECIMAL(5,1) NOT NULL,
    conditions VARCHAR(30) NOT NULL
);

INSERT INTO weather_readings (reading_id, station, observed_on, temperature_c, rainfall_mm, conditions) VALUES
(1, 'North Field', '2026-09-01', 14.2, 0.0, 'Clear'),
(2, 'North Field', '2026-09-02', 12.8, 2.4, 'Light rain'),
(3, 'Harbour', '2026-09-01', 16.1, 0.0, 'Sunny'),
(4, 'Harbour', '2026-09-02', 15.4, 1.2, 'Cloudy'),
(5, 'Hilltop', '2026-09-01', 10.7, 4.8, 'Rain'),
(6, 'Hilltop', '2026-09-02', 11.3, 0.6, 'Showers'),
(7, 'East Park', '2026-09-01', 13.9, 0.0, 'Clear'),
(8, 'East Park', '2026-09-02', 14.5, 0.3, 'Cloudy');

SELECT * FROM weather_readings;
