# Data Structures

## Topics Covered

1. **Lists**
   - List Creation and Manipulation
   - List Methods (append, insert, remove, pop)
   - List Comprehensions
   - Slicing and Indexing

2. **Tuples**
   - Immutable Sequences
   - Tuple Packing and Unpacking
   - Tuple Methods

3. **Dictionaries**
   - Key-Value Pairs
   - Dictionary Methods
   - Dictionary Comprehensions
   - Nested Dictionaries

4. **Sets**
   - Unique Collections
   - Set Operations (union, intersection, difference)
   - Set Methods

5. **Strings**
   - String Manipulation
   - String Methods
   - String Formatting
   - Regular Expressions (Intro)

## Files in This Section

- `01_lists.py` - Working with lists and list operations
- `02_tuples.py` - Tuple operations and use cases
- `03_dictionaries.py` - Dictionary creation and manipulation
- `04_sets.py` - Set operations and applications
- `05_strings.py` - Advanced string operations
- `06_exercises.py` - Data structure practice problems

## Key Concepts

### Lists
```python
# Creating a list
fruits = ["apple", "banana", "orange"]

# List methods
fruits.append("grape")
fruits.insert(1, "mango")
fruits.remove("banana")

# List comprehension
squares = [x**2 for x in range(1, 6)]

# Slicing
first_three = fruits[:3]
```

### Dictionaries
```python
# Creating a dictionary
student = {
    "name": "John",
    "age": 18,
    "grade": "A",
    "courses": ["Python", "SQL"]
}

# Accessing values
print(student["name"])
print(student.get("email", "Not provided"))

# Dictionary methods
for key, value in student.items():
    print(f"{key}: {value}")
```

### Sets
```python
# Creating sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Set operations
union = set1 | set2
intersection = set1 & set2
difference = set1 - set2
```

## Exercises

1. Create a program that manages a to-do list using lists
2. Build a contact management system using dictionaries
3. Implement a grade averaging program with dictionaries
4. Create a duplicate remover using sets
5. Build a word frequency counter

## Assessment Criteria

- Correct selection of data structures for problems
- Proper use of data structure methods
- List and dictionary comprehensions
- Understanding of mutable vs immutable types
- Efficient data structure usage
