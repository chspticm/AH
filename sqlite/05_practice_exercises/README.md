# SQLite Practice Exercises

## Beginner

1. **Basic Queries**
   - Select columns and filter with `WHERE`.
   - Sort with `ORDER BY` and limit rows with `LIMIT`.
   - Insert, update, and delete records.

2. **Joins**
   - Join two related tables.
   - Use `LEFT JOIN` to retain rows without a match.
   - Try `RIGHT JOIN` or `FULL OUTER JOIN` with SQLite 3.39.0 or later.

3. **Aggregation**
   - Count and sum values.
   - Find minimum and maximum values.
   - Group rows by category.

## Intermediate

1. **Queries**
   - Join three tables.
   - Use subqueries in `WHERE` and `SELECT`.
   - Use `CASE` for conditional results.
   - Combine results with `UNION`.

2. **Aggregation**
   - Use `GROUP BY` with `HAVING`.
   - Combine aggregate functions.
   - Try window functions if SQLite 3.25.0 or later is available.

3. **Data Modification**
   - Use `UPDATE` with conditions or subqueries.
   - Insert rows selected from another table.
   - Delete rows selected by a subquery.
   - Use transactions.

## Advanced Enrichment

1. Inspect query plans and compare indexes.
2. Create views and triggers for appropriate use cases.
3. Work with related data while preserving integrity constraints.
4. Investigate SQLite's `ATTACH DATABASE` for a separate-database exercise.

SQLite does not support stored procedures. Advanced SQL features can vary by SQLite version; check your library version before using them.

## Sample Exercises

### Student Grades

Create tables for students, courses, and grades. Find top performers, calculate class averages, and generate a transcript query.

### Shop Inventory

Create tables for products, categories, and orders. Search products, summarize sales, and update stock levels.

### Library

Track books, members, and loans. Find overdue books and generate member reports.

## Practice Goals

- Write SQLite-compatible SQL.
- Design queries that answer a stated question.
- Preserve data integrity when changing records.
- Test queries with useful example data and edge cases.
