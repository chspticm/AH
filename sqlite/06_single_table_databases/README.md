# SQLite Single-Table Database Practice

These five scripts each create one table with eight sample rows. Unlike MySQL, SQLite does not create a named server database inside the SQL script: the database is the file you open before running the script.

From the `sqlite` directory, open the SQLite CLI with a separate file for each script, then use `.read`:

```text
sqlite3 ah_books.db
.read 06_single_table_databases/01_books.sql
```

Run each script once against a new, empty database file. Running the same insert statements again will report duplicate primary-key values.

| Script | Topic | Suggested database file | Table | Rows |
| --- | --- | --- | --- | ---: |
| `01_books.sql` | Library books | `ah_books.db` | `books` | 8 |
| `02_weather.sql` | Weather observations | `ah_weather.db` | `weather_readings` | 8 |
| `03_shop_products.sql` | Shop inventory | `ah_shop.db` | `products` | 8 |
| `04_sports_results.sql` | Sports fixtures | `ah_sports.db` | `match_results` | 8 |
| `05_music_tracks.sql` | Music collection | `ah_music.db` | `tracks` | 8 |

Practise selecting columns, filtering with `WHERE`, sorting with `ORDER BY`, aggregating, and changing rows with `INSERT`, `UPDATE`, and `DELETE`.
