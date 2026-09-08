# Data Manipulation

## Topics Covered

1. **INSERT Operations**
   - Single Row Insert
   - Multiple Row Insert
   - INSERT INTO SELECT
   - Default Values

2. **UPDATE Operations**
   - Basic Updates
   - Updates with WHERE Clause
   - Updates with JOINs
   - Safe Update Mode

3. **DELETE Operations**
   - Single Row Deletion
   - Multiple Row Deletion
   - DELETE with JOINs
   - Cascading Deletes

4. **Transactions**
   - COMMIT and ROLLBACK
   - Transaction Control
   - Isolation Levels
   - ACID Properties

5. **Data Backup and Recovery**
   - Export Data
   - Import Data
   - Backup Strategies

## Files in This Section

- `01_insert_operations.sql` - INSERT statement examples
- `02_update_operations.sql` - UPDATE statement examples
- `03_delete_operations.sql` - DELETE statement examples
- `04_transactions.sql` - Transaction examples
- `05_exercises.sql` - Data manipulation practice problems

## Key Concepts

### Insert Single Row
```sql
INSERT INTO students (name, email, age)
VALUES ('John', 'john@example.com', 18);
```

### Insert Multiple Rows
```sql
INSERT INTO students (name, email, age)
VALUES 
    ('John', 'john@example.com', 18),
    ('Jane', 'jane@example.com', 19),
    ('Bob', 'bob@example.com', 18);
```

### Update with WHERE
```sql
UPDATE students
SET age = 20
WHERE name = 'John';
```

### Delete with WHERE
```sql
DELETE FROM students
WHERE age < 18;
```

### Transactions
```sql
START TRANSACTION;

INSERT INTO accounts VALUES (1, 'John', 1000);
INSERT INTO accounts VALUES (2, 'Jane', 500);

COMMIT;
-- or ROLLBACK if error occurs
```

## Exercises

1. Insert sample data into multiple tables
2. Update records with complex WHERE conditions
3. Delete records and handle referential integrity
4. Create and test transaction scenarios
5. Backup and restore database data

## Assessment Criteria

- Correct INSERT, UPDATE, DELETE syntax
- Proper use of WHERE clauses
- Transaction management
- Data integrity maintenance
- Referential integrity handling
