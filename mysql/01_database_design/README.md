# MySQL Database Design

## Topics Covered

1. **Database Concepts**
   - Tables, Rows, and Columns
   - Primary Keys and Foreign Keys
   - Data Types and Constraints

2. **Normalization**
   - First Normal Form (1NF)
   - Second Normal Form (2NF)
   - Third Normal Form (3NF)

3. **Entity-Relationship Diagrams (ERD)**
   - Entities and Attributes
   - Relationships (One-to-One, One-to-Many, Many-to-Many)
   - Cardinality and Participation

4. **Database Security**
   - User Accounts and Privileges
   - Password Security
   - Data Validation

## Files in This Section

- `01_database_creation.sql` - Creating databases and tables
- `02_data_types.sql` - MySQL data types and constraints
- `03_relationships.sql` - Setting up relationships between tables
- `04_normalization.sql` - Examples of normalized database designs
- `05_design_exercises.sql` - Practice database designs

## Key Concepts

### Creating a Database
```sql
CREATE DATABASE school;
USE school;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Relationships
```sql
-- One-to-Many Relationship
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Many-to-Many Relationship
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

### Data Types
- **Numeric**: INT, FLOAT, DECIMAL
- **String**: VARCHAR, TEXT, CHAR
- **Date/Time**: DATE, TIME, DATETIME, TIMESTAMP
- **Boolean**: BOOLEAN/TINYINT

### Constraints
- PRIMARY KEY: Uniquely identifies each row
- FOREIGN KEY: Maintains referential integrity
- NOT NULL: Field must have a value
- UNIQUE: Values must be unique
- DEFAULT: Default value if not specified
- CHECK: Validates data based on condition

## Exercises

1. Design a database for a school with students, teachers, courses, and enrollments
2. Create a database for an online store with products, categories, and orders
3. Design a social media database with users, posts, and comments
4. Create a library management system database

## Assessment Criteria

- Appropriate use of data types
- Correct primary and foreign key implementation
- Normalized database design
- Clear entity relationships
- Proper constraint implementation
