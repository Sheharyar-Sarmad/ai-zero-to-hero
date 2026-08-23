

## Time & Space Complexity 

## What is it?

Time complexity – how runtime grows with input size (n).

## Space complexity 
how memory usage grows with input size (n).

Measured in Big O (worst‑case), Ω (best), Θ (average). Usually we care about Big O.

Why ignore constants and lower terms?
O(2n) → O(n)

O(n² + n) → O(n²)

Only the dominant term matters as n → ∞.

## Common Complexities (fastest → slowest)

## Complexity	Name	       Typical scenario

O(1)	    Constant	    Array access, hash lookup
O(log n)	Logarithmic	    Binary search, balanced tree ops
O(n)	    Linear	        Single loop, linear search
O(n log n)	Linearithmic	Efficient sorts (merge, heap, quick – average)
O(n²)	    Quadratic	    Nested loops over all pairs
O(2ⁿ)	    Exponential	    Recursive Fibonacci (naive)
O(n!)	    Factorial	    Permutations generation

## How to calculate Time Complexity

Loops – multiply nested loops: O(n^depth).

Sequential steps – add, keep the largest.

Recursion – solve recurrence (e.g., T(n) = T(n-1) + O(1) → O(n)).

Binary splitting (halving input) → usually O(log n).

## Space Complexity components

Input space – size of data given (usually fixed, often not counted in auxiliary space).

Auxiliary space – extra memory used by the algorithm (variables, call stack, temporary arrays).

Total = input + auxiliary → often reported as auxiliary (e.g., "in‑place" = O(1) auxiliary).

## Common space pitfalls

Recursive call stack → O(depth) (e.g., recursion depth n → O(n) space).

Copying arrays → O(n) extra.

2D matrix → O(n²) if square.

## Rule of thumb

Time vs Space trade‑off, you can often speed up by using more memory (caching, DP) or save memory by recomputing (slower).

## Bottom line

Complexity tells you if your code will scale. Always aim for the lowest feasible complexity for your constraints.