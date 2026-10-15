# SQLite SQL Fundamentals

## Topics Covered

1. **SELECT Statements**
   - Select all or specific columns
   - `WHERE` conditions
   - `DISTINCT`
   - `ORDER BY` and `LIMIT`

2. **JOIN Operations**
   - `INNER JOIN`
   - `LEFT JOIN`
   - `RIGHT JOIN` and `FULL OUTER JOIN` (SQLite 3.39.0 and later)

3. **Aggregation**
   - `COUNT`, `SUM`, `AVG`, `MAX`, and `MIN`
   - `GROUP BY` and `HAVING`

4. **Subqueries**
   - Scalar subqueries
   - Correlated subqueries
   - `IN` and `EXISTS`

## Key Concepts

### Basic SELECT

```sql
SELECT * FROM students;

SELECT name, email
FROM students
WHERE age > 18
ORDER BY name ASC
LIMIT 10;

SELECT DISTINCT city FROM students;
```

### JOIN Operations

```sql
SELECT s.name, c.course_name
FROM students AS s
INNER JOIN enrollments AS e ON e.student_id = s.student_id
INNER JOIN courses AS c ON c.course_id = e.course_id;

SELECT s.name, COUNT(e.enrollment_id) AS course_count
FROM students AS s
LEFT JOIN enrollments AS e ON e.student_id = s.student_id
GROUP BY s.student_id, s.name;
```

SQLite supports `RIGHT JOIN` and `FULL OUTER JOIN` from version 3.39.0. Check the SQLite library version used by your application before using those joins.

### Aggregation

```sql
SELECT COUNT(*) AS total_students FROM students;

SELECT AVG(score) AS average_score FROM grades;

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

### Subqueries

```sql
SELECT name
FROM students
WHERE student_id = (
    SELECT student_id
    FROM grades
    WHERE score = (SELECT MAX(score) FROM grades)
);

SELECT *
FROM courses
WHERE course_id IN (
    SELECT course_id
    FROM enrollments
    WHERE student_id = 1
);
```

## Exercises

1. Retrieve records using a range of `WHERE` conditions.
2. Practise inner and left joins; try right and full joins if your SQLite version supports them.
3. Use aggregate functions to summarize data.
4. Create subqueries using `IN`, `EXISTS`, and scalar results.
5. Combine filtering, grouping, and sorting in one query.

## Practice Goals

- Write valid SQLite query syntax.
- Choose appropriate filters and joins.
- Group and aggregate results correctly.
- Make queries readable and check their results.
