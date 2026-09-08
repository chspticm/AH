# File Handling & Serialization

## Topics Covered

1. **File Operations**
   - Opening and Closing Files
   - Reading Files (read, readline, readlines)
   - Writing Files
   - Appending to Files
   - Context Managers (with statement)

2. **File Types**
   - Text Files
   - Binary Files
   - CSV Files
   - JSON Files

3. **Serialization**
   - JSON Serialization
   - Pickle Module
   - Object Persistence

4. **Error Handling**
   - FileNotFoundError
   - PermissionError
   - Try-Except-Finally

## Files in This Section

- `01_file_operations.py` - Basic file reading and writing
- `02_csv_handling.py` - Working with CSV files
- `03_json_handling.py` - JSON serialization and deserialization
- `04_pickle_handling.py` - Object serialization with pickle
- `05_error_handling.py` - File handling error handling
- `06_exercises.py` - File handling practice problems

## Key Concepts

### Reading Files
```python
# Using context manager (recommended)
with open("file.txt", "r") as file:
    content = file.read()
    
# Reading line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

### Writing Files
```python
# Writing to a file
with open("output.txt", "w") as file:
    file.write("Hello, World!")
    
# Appending to a file
with open("output.txt", "a") as file:
    file.write("\nNew line")
```

### JSON Handling
```python
import json

# Writing JSON
data = {"name": "John", "age": 18}
with open("data.json", "w") as f:
    json.dump(data, f)

# Reading JSON
with open("data.json", "r") as f:
    data = json.load(f)
```

### CSV Handling
```python
import csv

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

# Writing CSV
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["John", 18])
```

## Exercises

1. Create a program that reads a text file and counts words
2. Build a CSV reader that filters data by criteria
3. Create a JSON-based configuration file manager
4. Implement a student record system with file persistence
5. Build a data backup system using serialization

## Assessment Criteria

- Correct file opening and closing procedures
- Proper use of context managers
- Correct file mode selection (r, w, a, b)
- Proper error handling
- Correct serialization/deserialization
