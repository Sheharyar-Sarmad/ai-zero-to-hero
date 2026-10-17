# Array Fundamentals in JavaScript

An **array** is a list-like object used to store multiple values in a single variable container.

## Core Concepts
1. **Zero-Based Indexing:** The first element is at index `0`, the second at `1`, and the last at `array.length - 1`.
2. **Ordered & Dynamic:** Insertion order is preserved, and arrays grow or shrink automatically.
3. **Heterogeneous:** JavaScript arrays can hold mixed data types (strings, numbers, booleans, objects, arrays).

## Basic Implementation & Operations
- **Creation:** `const arr = ["apple", "banana", "mango"];`
- **Mutating Methods (Modify original):** `push()`, `pop()`, `unshift()`, `shift()`, `splice()`
- **Non-Mutating Methods (Return new value/copy):** `slice()`, `concat()`, `includes()`, `indexOf()`, `join()`