# SQLite Practice Materials

This folder mirrors the MySQL learning topics with SQLite-specific notes and examples. SQLite databases are files (for example, `school.db`), not server databases. Use the SQLite command-line shell, DB Browser for SQLite, or another SQLite-compatible client.

## Topics

- [Database design](./01_database_design/README.md)
- [SQL fundamentals](./02_sql_fundamentals/README.md)
- [Advanced queries](./03_advanced_queries/README.md)
- [Data manipulation](./04_data_manipulation/README.md)
- [Practice exercises](./05_practice_exercises/README.md)
- [Single-table database scripts](./06_single_table_databases/README.md)

The five single-table scripts create one table and eight sample rows each. Open a new database file and run one script at a time. From the `sqlite` directory, use a terminal with the SQLite CLI installed:

```text
sqlite3 ah_books.db
.read 06_single_table_databases/01_books.sql
```

The SQL examples target SQLite. Some optional advanced features depend on the SQLite library version; check the linked topic notes. These materials are supplementary practice, not an SQA specification.
