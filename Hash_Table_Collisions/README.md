# Hash Table Collisions

This repository demonstrates different strategies to handle collisions in a hash table. Hash tables are widely used data structures for efficient key-value storage. When multiple keys hash to the same index, a collision occurs. This folder contains Python implementations of two popular collision resolution methods:

- **Open Addressing (Linear Probing)**
- **Separate Chaining**

## Files Overview

### 1. `hash-table-template.py`
- A template file to implement hash tables.
- This file provides a basic structure for building hash tables and can be used as a starting point for custom implementations.
  
### 2. `hash_table_open_addressing.py`
- Implements **Open Addressing** using the **Linear Probing** method.
- Collisions are resolved by finding the next available slot in the array and placing the key-value pair there.
- The file demonstrates how the table handles insertion and retrieval.

### 3. `hash_table_separate_chaining.py`
- Implements **Separate Chaining** for collision resolution.
- Each bucket in the hash table is a list that stores multiple key-value pairs that hash to the same index.
- This method uses linked lists (or lists) to handle collisions and allows multiple entries to share the same hash index.


