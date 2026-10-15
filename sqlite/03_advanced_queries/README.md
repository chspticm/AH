# SQLite Advanced Queries

These topics are optional SQL enrichment. Check the SQLite library version used by your application before relying on version-specific features.

## Topics Covered

1. **Complex JOINs**
   - Self joins
   - Cross joins
   - Multiple joins

2. **Window Functions** (SQLite 3.25.0 and later)
   - `ROW_NUMBER()`
   - `RANK()` and `DENSE_RANK()`
   - `LAG()` and `LEAD()`
   - Aggregate window functions

3. **Common Table Expressions**
   - `WITH` clause
   - Recursive CTEs
   - Multiple CTEs

4. **Query Planning**
   - Indexes
   - `EXPLAIN QUERY PLAN`
   - Query performance

## Key Concepts

### Self Join

```sql
SELECT employee.name AS employee, manager.name AS manager
FROM employees AS employee
JOIN employees AS manager ON employee.manager_id = manager.id;
```

### Window Functions

```sql
SELECT
    name,
    score,
    RANK() OVER (ORDER BY score DESC) AS score_rank,
    ROW_NUMBER() OVER (ORDER BY score DESC) AS row_number
FROM students;
```

### Common Table Expressions

```sql
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 50000
)
SELECT *
FROM high_earners
WHERE department = 'Sales';
```

### Query Planning

```sql
EXPLAIN QUERY PLAN
SELECT name FROM students WHERE city = 'Dunedin';
```

SQLite does not provide MySQL-style stored procedures. Use application code, views, or triggers when appropriate. Do not add indexes without checking whether they improve the actual query workload.

## Exercises

1. Write self joins for a table with hierarchical records.
2. Rank data with window functions if available in your SQLite version.
3. Use a CTE to make a multi-step query easier to read.
4. Inspect a query with `EXPLAIN QUERY PLAN`.
5. Compare a query plan before and after adding an index.
