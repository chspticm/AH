# Object-Oriented Programming (OOP)

## Topics Covered

1. **Classes and Objects**
   - Class Definition
   - Instance Variables
   - Instance Methods

2. **Inheritance**
   - Parent and Child Classes
   - Method Overriding
   - Super() Function

3. **Encapsulation**
   - Access Modifiers (Public, Private)
   - Getters and Setters
   - Data Protection

4. **Polymorphism**
   - Method Overloading
   - Method Overriding
   - Abstract Classes

5. **Composition**
   - Relationships Between Classes
   - Has-A Relationships

## Files in This Section

- `01_classes_objects.py` - Basic class definition and objects
- `02_inheritance.py` - Inheritance and method overriding
- `03_encapsulation.py` - Private attributes and methods
- `04_polymorphism.py` - Polymorphic behavior
- `05_exercises.py` - Practice problems

## Key Concepts

### Classes and Objects
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object
student = Student("John", 18)
student.display_info()
```

### Inheritance
```python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}"

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
```

### Encapsulation
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount > 0:
            self.__balance = amount
```

## Exercises

1. Create a `Person` class with name, age, and email attributes
2. Extend the `Person` class to create a `Student` class with student ID
3. Implement a `BankAccount` class with deposit and withdraw methods
4. Create a `Library` system with `Book` and `Member` classes

## Assessment Criteria

- Correct class and object design
- Proper use of inheritance
- Encapsulation and data protection
- Polymorphic design patterns
- Code organization and structure
