
## Stack - Concise Theoretical Guide

## 1. What is a Stack?

Definition: Linear data structure following LIFO (Last In, First Out) principle.

Key Idea: The most recently added element is removed first.

Real-World Analogies:

Stack of plates (take top plate)

Browser back button (go to most recent page)

Undo operation (reverse last action)

Pringles can (last chip in, first out)

Visual:

text
Top → [5] ← Most recent (First Out)
      [4]
      [3]
      [2]
Bottom→ [1] ← Oldest (Last Out)

## 2. LIFO Explained

LIFO = Last In, First Out

## How It Works:

push(1) → [1]        
push(2) → [1,2]      
push(3) → [1,2,3]    
pop()   → [1,2]      (removes 3 - Last In)
pop()   → [1]        (removes 2)
pop()   → []         (removes 1 - First In)

Key Insight: Elements are removed in reverse order of insertion.

## Why LIFO?

Natural for nested/recursive operations

Simple: Only top element accessible

Efficient: All operations at one end

## 3. Core Operations

## Operation	What It Does	             Complexity
   push(x)	    Add x to top	             O(1)
   pop()	    Remove & return top	         O(1)
   peek()	    View top without removing	 O(1)
   isEmpty()	Check if empty	             O(1)
   size()	    Get number of elements	     O(1)

## Important:

Can only access the top element

No random access to middle elements

## 4. Implementation Types

Array-Based Stack
Uses contiguous memory

Fixed or dynamic capacity

Fast access (cache-friendly)

May need resizing

Linked List Stack

Uses scattered memory

Dynamic size (no resizing)

Extra pointer overhead

No overflow risk

## Comparison:
## Aspect	    Array	      Linked List
   Memory	    Contiguous	  Scattered
   Size	        Fixed/Dynamic Always Dynamic
   Overflow	    Possible	  No
   Cache	    Friendly	  Unfriendly

## 5. Stack vs Other Structures

Stack vs Queue
Aspect	Stack	Queue
Principle	LIFO	FIFO
Access	Top only	Front & Back
Analogy	Plate stack	Line of people
Stack vs Array
Stack: Restricted access (top only)

Array: Full random access

## 6. Common Applications

1. Function Call Stack
text
main() → A() → B() → C() (executes)
C() returns → B() returns → A() returns → main() returns

LIFO ensures inner functions complete before outer!

2. Parenthesis Matching

Expression: { [ ( ) ] }

Process:
{ → push
[ → push
( → push
) → pop (matches '(')
] → pop (matches '[')
} → pop (matches '{')
→ Valid (empty stack)

3. Expression Evaluation

Postfix: 2 3 * 4 +
1. push(2), push(3)
2. * → pop(3,2), compute 6, push(6)
3. push(4)
4. + → pop(4,6), compute 10
Result: 10
************************************
4. Undo/Redo

Undo: Pop from undo stack → Push to redo stack

Redo: Pop from redo stack → Push to undo stack

5. Backtracking (DFS)
6. 
Push starting point

Pop to explore

Push next possibilities

LIFO ensures depth-first exploration

## . Advanced Concepts

Monotonic Stack
Definition: Stack that maintains sorted order (increasing or decreasing).

Types:

Increasing: [1, 3, 5, 7] (each > previous)

Decreasing: [9, 6, 4, 2] (each < previous)

Used For:

Next Greater Element

Stock Span

Largest Rectangle in Histogram

Mechanism:

When pushing x:
1. Pop while condition violated
2. Push x
3. Stack maintains monotonic property
Amortized Analysis
Operations are O(1) on average

Dynamic resizing occasional O(n) cost

Over many operations: average O(1)

## Stack Overflow vs Underflow

Condition	What Happens	Prevention
Overflow	Push when full	Check isFull()
Underflow	Pop when empty	Check isEmpty()

## 8. Problems Solved by Stacks

## Problem	Why Stack Works

Function calls	LIFO matches nested calls
Balanced parentheses	Last opening matches first closing
Expression evaluation	Handles operator precedence
Undo/Redo	Last action undone first
DFS traversal	Explores depth-first naturally
Recursive algorithms	Mirrors recursion stack

## 9. Complexity Summary

## Time Complexity
Operation	Complexity
push	O(1)*
pop	O(1)
peek	O(1)
isEmpty	O(1)
size	O(1)
search	O(n)
*O(1) amortized for dynamic array

Space Complexity
Per element: O(1)

Total: O(n)

## When to Use a Stack 

## Use Stack For:

Nested structures processing

Undo/Redo operations

Expression parsing

Depth-first search

Recursive algorithm simulation

Reversing sequences

## Don't Use Stack For:

Random access needs

Frequent middle insertions/deletions

FIFO processing (use queue)

Frequent searching

## 11. Key Theoretical Insights

## Why LIFO is Powerful:

Recursion: Natural match for nested calls

Nesting: Processes inside-out

Reversal: Last processed first

State Saving: Easy to restore previous state

## The Stack Philosophy:

Restricted access = Simplicity

Operations at one end = Efficiency

LIFO principle = Natural for many problems

## Three Golden Rules:

Only top is accessible

Last In = First Out (always)

All operations at one end

## Quick Comparison

## Feature	    Stack	       Queue	        Array
  Principle	    LIFO	       FIFO	            Indexed
  Insert	    Top only	   Back only	    Anywhere
  Delete	    Top only	   Front only	    Anywhere
  Access	    Only top	   Front/Back	    Any index
  Analogy	    Plate stack	   Line of people	Shelves

## Final Takeaway

A stack is elegantly simple: restricted access, LIFO behavior, O(1) operations. Yet it's one of the most powerful tools in computing because recursion, parsing, backtracking, and undo all naturally follow the LIFO principle. Master the stack, and you master fundamental computer science.