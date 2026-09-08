# SQL Fundamentals

## Topics Covered

1. **SELECT Statements**
   - Basic SELECT
   - WHERE Clause
   - DISTINCT
   - ORDER BY

2. **JOIN Operations**
   - INNER JOIN
   - LEFT JOIN
   - RIGHT JOIN
   - FULL OUTER JOIN

3. **Aggregation**
   - COUNT, SUM, AVG, MAX, MIN
   - GROUP BY
   - HAVING Clause

4. **Subqueries**
   - Scalar Subqueries
   - Correlated Subqueries
   - IN, EXISTS Operators

## Files in This Section

- `01_select_basics.sql` - Basic SELECT queries
- `02_where_conditions.sql` - WHERE clause and conditions
- `03_joins.sql` - Different types of joins
- `04_aggregation.sql` - Aggregation and grouping
- `05_subqueries.sql` - Subquery examples
- `06_practice_queries.sql` - Practice exercises

## Key Concepts

### Basic SELECT
```sql
-- Select all columns
SELECT * FROM students;

-- Select specific columns
SELECT name, email FROM students;

-- Select with WHERE clause
SELECT * FROM students WHERE age > 18;

-- Select with ORDER BY
SELECT * FROM students ORDER BY name ASC;

-- Select with DISTINCT
SELECT DISTINCT city FROM students;
```

### JOIN Operations
```sql
-- INNER JOIN
SELECT s.name, c.course_name
FROM students s
INNER JOIN enrollments e ON s.student_id = e.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

-- LEFT JOIN
SELECT s.name, COUNT(e.enrollment_id) as course_count
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id;
```

### Aggregation
```sql
-- COUNT
SELECT COUNT(*) as total_students FROM students;

-- SUM and AVG
SELECT AVG(score) as average_score FROM grades;

-- GROUP BY
SELECT department, COUNT(*) as employee_count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;
```

### Subqueries
```sql
-- Scalar Subquery
SELECT name FROM students
WHERE student_id = (
    SELECT student_id FROM grades
    WHERE score = (SELECT MAX(score) FROM grades)
);

-- Subquery with IN
SELECT * FROM courses
WHERE course_id IN (
    SELECT course_id FROM enrollments
    WHERE student_id = 1
);
```

## Exercises

1. Write queries to retrieve data with various WHERE conditions
2. Practice different types of JOIN operations
3. Use aggregation functions to analyze data
4. Create complex queries using subqueries
5. Combine multiple concepts in a single query

## Assessment Criteria

- Correct SQL syntax
- Appropriate use of WHERE clauses
- Proper JOIN implementations
- Correct aggregation and grouping
- Query optimization and readability
