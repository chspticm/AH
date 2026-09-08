# Python Fundamentals

## Topics Covered

1. **Variables and Data Types**
   - Integers, Floats, Strings
   - Lists, Tuples, Dictionaries
   - Type Conversion

2. **Control Flow**
   - If/Else Statements
   - Loops (for, while)
   - Break and Continue

3. **Functions**
   - Function Definition
   - Parameters and Return Values
   - Variable Scope

4. **Input/Output**
   - User Input
   - Print Statements
   - String Formatting

## Files in This Section

- `01_variables.py` - Working with variables and data types
- `02_operators.py` - Arithmetic, comparison, and logical operators
- `03_control_flow.py` - If statements and loops
- `04_functions.py` - Function definition and usage
- `05_exercises.py` - Practice problems

## Key Concepts

### Variables and Data Types
```python
# Integers
age = 18

# Floats
height = 5.9

# Strings
name = "John"

# Lists
numbers = [1, 2, 3, 4, 5]

# Dictionaries
student = {"name": "John", "age": 18, "grade": "A"}
```

### Control Flow
```python
# If statements
if age >= 18:
    print("Adult")
else:
    print("Minor")

# Loops
for i in range(5):
    print(i)

while condition:
    # do something
    pass
```

### Functions
```python
def greet(name):
    return f"Hello, {name}!"

result = greet("John")
```

## Exercises

1. Create a program that calculates the sum of numbers in a list
2. Write a function that checks if a number is prime
3. Implement a program that converts Celsius to Fahrenheit
4. Create a simple calculator with basic operations

## Assessment Criteria

- Understanding of Python syntax and semantics
- Correct use of variables and data types
- Implementation of control flow statements
- Function definition and calling conventions
- Code readability and comments
