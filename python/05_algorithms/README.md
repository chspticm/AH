# Algorithms

## Topics Covered

1. **Sorting Algorithms**
   - Bubble Sort
   - Selection Sort
   - Insertion Sort
   - Quick Sort
   - Merge Sort

2. **Searching Algorithms**
   - Linear Search
   - Binary Search

3. **Time Complexity**
   - Big O Notation
   - Best, Average, and Worst Cases
   - Space Complexity

4. **Common Algorithms**
   - Factorial
   - Fibonacci
   - Prime Numbers
   - String Manipulation

## Files in This Section

- `01_sorting.py` - Sorting algorithm implementations
- `02_searching.py` - Searching algorithm implementations
- `03_complexity.py` - Time and space complexity analysis
- `04_recursion.py` - Recursive algorithm examples
- `05_dynamic_programming.py` - Dynamic programming concepts
- `06_exercises.py` - Algorithm practice problems

## Key Concepts

### Linear Search
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### Bubble Sort
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
```

### Time Complexity Examples
- **O(1)**: Constant time (array access)
- **O(log n)**: Logarithmic (binary search)
- **O(n)**: Linear (linear search)
- **O(n log n)**: Linear-logarithmic (merge sort, quick sort)
- **O(n²)**: Quadratic (bubble sort, insertion sort)
- **O(2^n)**: Exponential (recursive fibonacci)

## Exercises

1. Implement and compare different sorting algorithms
2. Analyze time complexity of custom algorithms
3. Create a program that searches for patterns in data
4. Build a recursive solution for a classic problem
5. Implement a dynamic programming solution

## Assessment Criteria

- Correct algorithm implementation
- Understanding of time complexity
- Optimization techniques
- Code efficiency
- Clear explanation of algorithm choice
