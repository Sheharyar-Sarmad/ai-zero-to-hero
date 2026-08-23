

## Arrays 

## What is it?

Contiguous block of memory storing elements of the same type.

Each element accessed by an index (0‑based in most languages).

## Why use it?

Fast random access – get any element instantly via index.

Cache‑friendly – data stored together, so CPU loads it fast.

Simple – the most basic and widely supported structure.

## When to use?

When you know the size in advance (or can accept resizing overhead).

When you need frequent reads by position.

When iteration over all elements is common.

Complexity (Time)
Operation	Complexity
Access by index	O(1)
Search (unsorted)	O(n)
Search (sorted)	O(log n) – binary search
Insert at end	O(1)*
Insert at start/middle	O(n)
Delete at end	O(1)
Delete at start/middle	O(n)
*Amortized O(1) for dynamic arrays (e.g., Python list, Java ArrayList).

## Key Variations

Static array – fixed size (C‑style).

Dynamic array – auto‑resizes when full (e.g., list in Python, ArrayList in Java, vector in C++).

Multi‑dimensional – matrix, grid (e.g., int[rows][cols]).

## What problems does it solve?

Storing and quickly accessing sequential data (e.g., list of users, sensor readings).

Implementing other data structures (e.g., stacks, queues, hash tables).

Matrix operations (images, tables).

Two‑pointer / sliding window algorithms.

## When NOT to use?

Frequent insertions/deletions at the beginning – use linked list instead.

Unknown / wildly fluctuating size – use dynamic list or linked structure.

## Bottom line

Use arrays when you need fast indexed reads and occasional writes at the end. Avoid when you constantly shift elements.