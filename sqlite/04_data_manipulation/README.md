# SQLite Data Manipulation

## Topics Covered

1. **INSERT Operations**
   - Single and multiple row inserts
   - `INSERT INTO ... SELECT`
   - Default values

2. **UPDATE Operations**
   - Updates with `WHERE`
   - Updates using subqueries
   - `UPDATE FROM` (SQLite 3.33.0 and later)

3. **DELETE Operations**
   - Deleting one or more rows with `WHERE`
   - Deleting rows selected by a subquery
   - Foreign-key actions

4. **Transactions**
   - `BEGIN`, `COMMIT`, and `ROLLBACK`

5. **Backup and Recovery**
   - SQLite database-file backups
   - SQLite CLI `.backup` and `.restore`

## Key Concepts

### Insert Rows

```sql
INSERT INTO students (name, email, age)
VALUES ('John', 'john@example.com', 18);

INSERT INTO students (name, email, age)
VALUES
    ('Jane', 'jane@example.com', 19),
    ('Bob', 'bob@example.com', 18);
```

### Update and Delete

```sql
UPDATE students
SET age = 20
WHERE name = 'John';

DELETE FROM students
WHERE age < 18;
```

For joins in updates or deletes, use a subquery where appropriate. SQLite's `UPDATE FROM` is available from version 3.33.0; support for other vendor-specific joined DML syntax differs.

### Transactions

```sql
BEGIN TRANSACTION;

INSERT INTO accounts (account_id, owner, balance)
VALUES (1, 'John', 1000), (2, 'Jane', 500);

COMMIT;
-- Use ROLLBACK instead of COMMIT if the operation should be undone.
```

Enable `PRAGMA foreign_keys = ON` on each connection if foreign-key constraints must be enforced. For backups, use the SQLite CLI's `.backup` command or a suitable SQLite backup API; copying a database while it is being written can produce an inconsistent backup.

## Exercises

1. Insert sample records into tables.
2. Update records using conditions and subqueries.
3. Delete selected rows and test foreign-key actions.
4. Use a transaction and verify both `COMMIT` and `ROLLBACK` behaviour.
5. Create a backup using an SQLite-supported method and restore it.
