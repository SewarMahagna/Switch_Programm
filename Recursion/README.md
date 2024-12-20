# Recursion Practice

This folder contains practice exercises focused on recursive functions. Recursion is a powerful technique in programming where a function calls itself to solve smaller instances of the same problem. The exercises here help practice and understand recursion through common problems.

## Exercises

### Ex 1: Fibonacci Sequence

- **Problem**: Write a recursive function that returns the nth number in the Fibonacci sequence.
- **Description**: The Fibonacci sequence is defined as:
  - `fibonacci(0) = 0`
  - `fibonacci(1) = 1`
  - `fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)` for `n > 1`

- **Example**:
  - **Input**: `fibonacci(6)`
  - **Expected Output**: `8`
  
  **Explanation**: The Fibonacci sequence for `n = 6` is:
  `0, 1, 1, 2, 3, 5, 8`


### Ex 2: Find All Subsets of a Set

- **Problem**: Write a recursive function `find_subsets(lst)` that returns all possible subsets of a given list of unique elements.
- **Description**: Given a list, the function should generate every possible subset, including the empty set and the set itself.

- **Example**:
  - **Input**: `find_subsets([1, 2])`
  - **Expected Output**: `[[], [1], [2], [1, 2]]`
