Big O Notation (DSA Notes)
Definition

Big O Notation is a mathematical way to describe how the time or memory required by an algorithm grows as the input size (n) increases.

It measures the worst-case performance of an algorithm.

Simple Definition:
Big O tells us how efficient an algorithm is when the amount of data becomes very large.

Why Do We Need Big O?

Suppose you have two algorithms:

Algorithm A

Takes 10 seconds for 1,000 items

Algorithm B

Takes 1 second for 1,000 items

Does this mean B is always better?

Not necessarily.

As data grows to 1 million items, Algorithm B might become slower than A depending on how its runtime grows.

Big O focuses on growth rate, not exact execution time.

Input Size

The variable

n

represents the size of the input.

Examples

Array of 5 elements
n = 5

Array of 100 elements
n = 100

Array of 1,000,000 elements
n = 1,000,000
Time Complexity

Time Complexity tells us how the number of operations increases as n increases.

It does not measure actual seconds.

Instead, it counts operations.

Example

for i in range(n):
    print(i)

If n = 5

Operations

5

If

n = 1000

Operations

1000

Time Complexity

O(n)
Space Complexity

Space Complexity tells us how much extra memory an algorithm uses.

Example

numbers = [1,2,3,4,5]

Memory increases with input size.

O(n)
Common     Big O Complexities
Big O	   Name	Performance
O(1)	   Constant	      ⭐ Fastest
O(log n)   Logarithmic	  ⭐ Very Fast
O(n)	   Linear	      ✅ Good
O(n log n) Linearithmic	  ✅ Efficient
O(n²)	   Quadratic	  ⚠ Slow
O(n³)	   Cubic	      ❌ Very Slow
O(2ⁿ)	   Exponential	  🚫 Extremely Slow
O(n!)	   Factorial	  🚫 Worst
1. O(1) —  Constant Time

Execution time never changes.

Example

arr = [10,20,30]

print(arr[1])

No matter how large the array becomes,

1 operation

Complexity

O(1)
2. O(log n) — Logarithmic Time

The problem size is repeatedly cut in half.

Example

Binary Search

100 elements

↓

50

↓

25

↓

12

↓

6

↓

3

↓

1

Python Example

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

Complexity

O(log n)
3. O(n) — Linear Time

Work grows directly with input.

Example

for item in arr:
    print(item)

If n = 5

Operations

5

If n = 100

Operations

100

Complexity

O(n)
4. O(n log n)

Usually found in efficient sorting algorithms.

Examples

Merge Sort
Heap Sort
Average-case Quick Sort
O(n log n)
5. O(n²) — Quadratic Time

Nested loops.

Example

for i in arr:
    for j in arr:
        print(i, j)

If

n = 5

Operations

25

If

n = 100

Operations

10000

Complexity

O(n²)
6. O(n³)

Three nested loops.

Example

for i in arr:
    for j in arr:
        for k in arr:
            print(i, j, k)

Complexity

O(n³)
7. O(2ⁿ)

Every element creates two possibilities.

Common in recursion.

Example

Include

Exclude

Example Problems

Subsets
Backtracking

Complexity

O(2ⁿ)
8. O(n!)

Every possible arrangement.

Example

Finding all permutations.

ABC

ACB

BAC

BCA

CAB

CBA

Complexity

O(n!)
Growth Comparison
Best
│
O(1)
│
O(log n)
│
O(n)
│
O(n log n)
│
O(n²)
│
O(n³)
│
O(2ⁿ)
│
O(n!)
│
Worst
Rules for Finding Big O
Rule 1 — Ignore Constants
for i in range(2 * n):
    print(i)

Operations

2n

Big O

O(n)
Rule 2 — Drop Smaller Terms
n² + n + 10

Largest term dominates.

O(n²)
Rule 3 — Consecutive Loops Add
for i in range(n):
    print(i)

for j in range(n):
    print(j)

Operations

n + n = 2n

Big O

O(n)
Rule 4 — Nested Loops Multiply
for i in range(n):
    for j in range(n):
        print(i, j)

Operations

n × n

Big O

O(n²)
Rule 5 — Different Inputs Use Different Variables
for i in range(n):
    print(i)

for j in range(m):
    print(j)

Big O

O(n + m)

Nested version

for i in range(n):
    for j in range(m):
        print(i, j)

Big O

O(n × m)
Time Complexity of Common Operations
Operation	Big O
Access array by index	O(1)
Update array element	O(1)
Traverse array	O(n)
Linear Search	O(n)
Binary Search (sorted array)	O(log n)
Insert at end of Python list (average)	O(1)
Insert at beginning of list	O(n)
Delete at end (average)	O(1)
Delete at beginning	O(n)
Bubble Sort	O(n²)
Selection Sort	O(n²)
Insertion Sort (average/worst)	O(n²)
Merge Sort	O(n log n)
Heap Sort	O(n log n)
Quick Sort (average)	O(n log n)
Quick Sort (worst)	O(n²)
Key Interview Points
Big O measures growth rate, not exact execution time.
It usually refers to the worst-case time complexity.
Constants and lower-order terms are ignored.
Nested loops usually multiply complexities.
Consecutive loops usually add complexities.
Binary Search is O(log n) because it halves the search space each step.
Efficient sorting algorithms generally run in O(n log n).
As n becomes very large, algorithms with lower Big O scale much better.
Summary
Complexity	Meaning	Example
O(1)	Constant	Array indexing
O(log n)	Halves input each step	Binary Search
O(n)	One pass through data	Linear Search
O(n log n)	Efficient divide-and-conquer	Merge Sort
O(n²)	Two nested loops	Bubble Sort
O(n³)	Three nested loops	3D matrix operations
O(2ⁿ)	Exponential growth	Generating subsets
O(n!)	Factorial growth	Generating permutations

Memory Tip:
O(1) → O(log n) → O(n) → O(n log n) → O(n²) → O(n³) → O(2ⁿ) → O(n!)
From fastest to slowest as the input size grows.