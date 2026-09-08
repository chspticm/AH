# PHP Development

## Topics Covered

1. **PHP Fundamentals**
   - Syntax and Data Types
   - Variables and Constants
   - Operators and Control Structures

2. **Functions and Arrays**
   - Function Definition
   - Built-in Functions
   - Arrays and Array Functions

3. **Form Processing**
   - GET and POST Methods
   - Form Validation
   - File Uploads

4. **Database Connectivity**
   - MySQLi Extension
   - Prepared Statements
   - CRUD Operations

5. **Session Management**
   - Sessions and Cookies
   - User Authentication
   - Login/Logout Systems

6. **Security Best Practices**
   - SQL Injection Prevention
   - XSS Prevention
   - Password Hashing
   - CSRF Protection

## Files in This Section

- `01_basics.php` - PHP fundamentals
- `02_functions_arrays.php` - Functions and array operations
- `03_form_processing.php` - Handling form submissions
- `04_database_crud.php` - Database operations
- `05_sessions.php` - Session management
- `06_security.php` - Security practices
- `07_projects/` - Full-stack project examples

## Key Concepts

### PHP Basics
```php
<?php
// Variables
$name = "John";
$age = 18;

// Data Types
$integer = 42;
$float = 3.14;
$string = "Hello";
$bool = true;
$array = [1, 2, 3];

// Control Structures
if ($age >= 18) {
    echo "Adult";
} else {
    echo "Minor";
}

for ($i = 0; $i < 10; $i++) {
    echo $i;
}
?>
```

### Functions
```php
<?php
function greet($name) {
    return "Hello, $name!";
}

$message = greet("John");
echo $message;
?>
```

### Form Processing
```php
<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = htmlspecialchars($_POST['name']);
    $email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
    
    if ($name && $email) {
        // Process form
    } else {
        echo "Invalid input";
    }
}
?>
```

### Database Connection
```php
<?php
// Create connection
$conn = new mysqli("localhost", "user", "password", "database");

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Prepared statement
$stmt = $conn->prepare("SELECT * FROM students WHERE id = ?");
$stmt->bind_param("i", $id);
$stmt->execute();
$result = $stmt->get_result();
$row = $result->fetch_assoc();

$stmt->close();
$conn->close();
?>
```

### Sessions
```php
<?php
session_start();

// Set session variable
$_SESSION['user_id'] = 1;
$_SESSION['username'] = "john";

// Check if logged in
if (isset($_SESSION['user_id'])) {
    echo "Welcome, " . $_SESSION['username'];
}

// Logout
session_destroy();
?>
```

### Security
```php
<?php
// Escape output
echo htmlspecialchars($user_input);

// Validate email
$email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);

// Hash password
$hashed = password_hash($password, PASSWORD_DEFAULT);
$verified = password_verify($password, $hashed);

// Prevent SQL injection - use prepared statements
$stmt = $conn->prepare("SELECT * FROM users WHERE email = ?");
$stmt->bind_param("s", $email);
?>
```

## Exercises

1. Create a contact form with validation
2. Build a user registration system
3. Create a login authentication system
4. Develop a product listing page with database
5. Implement user profile management

## Assessment Criteria

- Correct PHP syntax
- Proper form validation and sanitization
- Secure database operations
- Session management implementation
- Security best practices
- Code organization and comments
