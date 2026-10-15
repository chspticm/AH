# SQLite Database Design

## Topics Covered

1. **Database Concepts**
   - Tables, rows, and columns
   - Primary keys and foreign keys
   - SQLite type affinity and constraints

2. **Normalization**
   - First Normal Form (1NF)
   - Second Normal Form (2NF)
   - Third Normal Form (3NF)

3. **Entity-Relationship Diagrams (ERD)**
   - Entities and attributes
   - One-to-one, one-to-many, and many-to-many relationships
   - Cardinality and participation

4. **Integrity and File Security**
   - `NOT NULL`, `UNIQUE`, `CHECK`, and `DEFAULT`
   - Foreign-key enforcement
   - Protecting database files with operating-system permissions

## SQLite Database Files

SQLite opens or creates a database file when you connect to it. There are no `CREATE DATABASE` or `USE` statements. For example, open `school.db` in your SQLite client, then create its tables.

## Key Concepts

### Creating Tables

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    date_of_birth TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

In SQLite, `INTEGER PRIMARY KEY` aliases the rowid and is automatically assigned when omitted. `AUTOINCREMENT` is usually unnecessary; use it only when rowids must never be reused.

### Relationships

Enable foreign-key enforcement for each connection:

```sql
PRAGMA foreign_keys = ON;
```

```sql
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(student_id),
    course_id INTEGER NOT NULL REFERENCES courses(course_id),
    enrollment_date TEXT
);
```

A junction table such as `enrollments` represents a many-to-many relationship.

### Type Affinity

SQLite uses type affinity rather than enforcing the declared type for every value. Common declarations are `INTEGER`, `REAL`, `TEXT`, `BLOB`, and `NUMERIC`. Store ISO-8601 dates as `TEXT`; represent booleans as `INTEGER` values `0` and `1`. Use `CHECK` constraints when a column needs a restricted set of values.

## Exercises

1. Design a school database with students, teachers, courses, and enrollments.
2. Create an online-store schema with products, categories, and orders.
3. Design a social-media schema with users, posts, and comments.
4. Create a library-management schema.

## Practice Goals

- Choose suitable SQLite declarations and constraints.
- Implement primary and foreign keys.
- Normalize a database and explain the relationships.
- Enable and test foreign-key enforcement.
