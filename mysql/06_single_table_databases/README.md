# Single-Table Database Practice

These five independent SQL scripts each create one database, one table, and no more than ten sample records. They are intended for practising single-table queries and data manipulation, not joins or relational database design.

Run each script once in MySQL Workbench or another MySQL client. Each script uses a distinct database name; running it again will attempt to insert the same primary keys.

| Script | Topic | Database | Table | Sample rows |
| --- | --- | --- | --- | ---: |
| `01_books.sql` | Library books | `ah_books` | `books` | 8 |
| `02_weather.sql` | Weather observations | `ah_weather` | `weather_readings` | 8 |
| `03_shop_products.sql` | Shop inventory | `ah_shop` | `products` | 8 |
| `04_sports_results.sql` | Sports fixtures | `ah_sports` | `match_results` | 8 |
| `05_music_tracks.sql` | Music collection | `ah_music` | `tracks` | 8 |

After creating a database, practise selecting columns, filtering with `WHERE`, sorting with `ORDER BY`, using aggregate functions, and trying `INSERT`, `UPDATE`, and `DELETE` on your own copy. The official course specification and current assessment task define assessed SQL requirements.
