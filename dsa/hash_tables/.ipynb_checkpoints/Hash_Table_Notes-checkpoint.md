# Hash Tables (DSA Notes)

## Definition

A **Hash Table** is a data structure that stores data as **key-value
pairs**. It provides very fast insertion, deletion, and lookup on
average.

## Why Use Hash Tables?

-   Fast searching
-   Fast insertion
-   Fast deletion
-   Store unique keys

## Real-Life Examples

-   Python `dict`
-   Phone contacts
-   Student ID -\> Student Record
-   DNS (Domain -\> IP)

## Hash Function

A hash function converts a key into an array index.

Example:

``` text
hash("apple") -> 3
hash("banana") -> 7
```

## Operations

  Operation   Average   Worst
  ----------- --------- -------
  Search      O(1)      O(n)
  Insert      O(1)      O(n)
  Delete      O(1)      O(n)

## Collision

A collision happens when two keys map to the same index.

### Collision Handling

1.  Chaining
2.  Open Addressing
    -   Linear Probing
    -   Quadratic Probing
    -   Double Hashing

## Python Dictionary

``` python
student = {
    "name": "Ali",
    "age": 20
}
print(student["name"])
student["city"] = "Lahore"
del student["age"]
```

## Advantages

-   Very fast average performance
-   Easy key-value access
-   Dynamic

## Disadvantages

-   Collisions
-   More memory
-   Worst-case O(n)

## Interview Questions

1.  What is a hash table?
2.  What is a hash function?
3.  What is a collision?
4.  Explain chaining.
5.  Explain linear probing.
6.  Why is average lookup O(1)?

## Summary

-   Key-value data structure
-   Uses hashing
-   Average operations: O(1)
-   Worst case: O(n)
-   Python `dict` is implemented using a hash table.
