# Advanced Queries

## Topics Covered

1. **Complex JOINs**
   - Self Joins
   - Cross Joins
   - Multiple Joins
   - Join Optimization

2. **Window Functions**
   - ROW_NUMBER()
   - RANK() and DENSE_RANK()
   - LAG() and LEAD()
   - Aggregate Window Functions

3. **Common Table Expressions (CTEs)**
   - WITH Clause
   - Recursive CTEs
   - Multiple CTEs

4. **Query Optimization**
   - Indexing Strategies
   - Query Execution Plans
   - Performance Analysis
   - Avoiding Common Pitfalls

## Files in This Section

- `01_complex_joins.sql` - Advanced join techniques
- `02_window_functions.sql` - Window function examples
- `03_ctes.sql` - Common Table Expression examples
- `04_optimization.sql` - Query optimization techniques
- `05_exercises.sql` - Advanced query practice problems

## Key Concepts

### Self Join
```sql
-- Find employees and their managers
SELECT e.name as employee, m.name as manager
FROM employees e
JOIN employees m ON e.manager_id = m.id;
```

### Window Functions
```sql
-- Rank students by score
SELECT 
    name,
    score,
    RANK() OVER (ORDER BY score DESC) as rank,
    ROW_NUMBER() OVER (ORDER BY score DESC) as row_num
FROM students;
```

### CTEs
```sql
WITH high_earners AS (
    SELECT * FROM employees
    WHERE salary > 50000
)
SELECT * FROM high_earners
WHERE department = 'Sales';
```

## Exercises

1. Write queries using self joins to find relationships
2. Use window functions to rank data
3. Create CTEs to simplify complex queries
4. Analyze query execution plans
5. Optimize slow-running queries

## Assessment Criteria

- Correct use of advanced SQL features
- Query optimization
- Understanding of execution plans
- Proper indexing strategy
- Performance improvements
