# Stack in Data Structures (DSA)

## Definition

A **Stack** is a **linear data structure** that follows the **LIFO (Last In, First Out)** principle.

This means the **last element inserted is the first one to be removed**.

**Example:**

```
Stack of Plates

   ┌───────┐
   │ Plate │ ← Top
   ├───────┤
   │ Plate │
   ├───────┤
   │ Plate │
   └───────┘

Remove → Top Plate First
```

---

# LIFO Principle

**LIFO = Last In, First Out**

Example:

```
Push 10
Push 20
Push 30

Stack

Top
 ↓
30
20
10

Pop →

30 removed first
```

---

# Basic Operations

## 1. Push

Adds an element to the top of the stack.

Example:

```
Before

Top
 ↓
20
10

Push(30)

Top
 ↓
30
20
10
```

Time Complexity

```
O(1)
```

---

## 2. Pop

Removes the top element.

Example

```
Before

Top
 ↓
30
20
10

Pop()

Top
 ↓
20
10
```

Time Complexity

```
O(1)
```

---

## 3. Peek (Top)

Returns the top element without removing it.

Example

```
Top
 ↓
30
20
10

Peek()

Returns 30
```

Time Complexity

```
O(1)
```

---

## 4. isEmpty()

Checks whether the stack contains any elements.

Returns

```
True
```

if empty, otherwise

```
False
```

Time Complexity

```
O(1)
```

---

## 5. Size

Returns the number of elements.

Example

```
Stack

30
20
10

Size = 3
```

Time Complexity

```
O(1)
```

---

# Stack Overflow

Occurs when trying to insert into a full stack (mostly in fixed-size implementations).

Example

```
Capacity = 3

Push(10)
Push(20)
Push(30)
Push(40)

Overflow
```

---

# Stack Underflow

Occurs when trying to remove an element from an empty stack.

Example

```
Empty Stack

Pop()

Underflow
```

---

# Stack Implementation

Stacks can be implemented using:

- Arrays (Python List)
- Linked Lists

Python commonly uses lists because append() and pop() from the end are O(1).

---

# Time Complexity

| Operation | Complexity |
|-----------|------------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| isEmpty | O(1) |
| Size | O(1) |
| Search | O(n) |

---

# Applications of Stack

## Function Calls

Programming languages use stacks to manage function calls.

```
main()

↓

login()

↓

validate()

↓

database()
```

When a function finishes, it is removed from the stack.

---

## Undo Feature

Applications like:

- Microsoft Word
- VS Code
- Photoshop

store previous actions in a stack.

```
Type A
Type B
Type C

Undo

Removes C first.
```

---

## Browser History

```
Google

↓

YouTube

↓

GitHub

Back Button

Returns to YouTube
```

---

## Parentheses Matching

Used to check expressions like:

```
()

{}

[]

({[]})
```

---

## Expression Evaluation

Stacks are used for:

- Prefix expressions
- Infix expressions
- Postfix expressions

---

## DFS (Depth First Search)

Graph traversal uses stacks.

---

## Backtracking

Algorithms such as:

- Maze solving
- Sudoku solver
- N Queens

use stacks (explicitly or through recursion).

---

# Advantages

- Very simple to implement.
- Fast insertion and deletion.
- Constant-time push and pop.
- Used in many algorithms.

---

# Disadvantages

- Can only access the top element directly.
- Searching takes O(n).
- Fixed-size stacks may overflow.

---

# Real-Life Examples

- Stack of plates
- Browser Back button
- Undo/Redo
- Function call stack
- Recursive functions

---

# Python Stack Example

```python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

print(stack.pop())

print(stack[-1])

print(len(stack))
```

Output

```
[10, 20, 30]
30
20
2
```

---

# Interview Questions

### What is a stack?

A linear data structure that follows the LIFO (Last In, First Out) principle.

---

### What is LIFO?

The last element inserted is the first one removed.

---

### Difference between Stack and Queue

| Stack | Queue |
|--------|--------|
| LIFO | FIFO |
| Push | Enqueue |
| Pop | Dequeue |
| One end | Two ends |

---

### Time Complexities

```
Push      O(1)

Pop       O(1)

Peek      O(1)

Size      O(1)

Search    O(n)
```

---

# Summary

- Linear Data Structure
- Follows LIFO
- Push → Insert
- Pop → Remove
- Peek → View Top
- Used in recursion, DFS, browser history, undo, expression evaluation, and backtracking.