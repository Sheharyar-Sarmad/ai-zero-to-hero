# Linked List (DSA Notes)
;
## Definition

A Linked List is a linear data structure made up of **nodes**.

Each node contains:

1. Data (Value)
2. Pointer (Reference) to the next node

Unlike arrays, linked list elements are **not stored in contiguous memory**.

---

## Structure of a Node

+------+------+
| Data | Next |
+------+------+

Example:

+------+---------+
| 298  | Address |
+------+---------+

Data = 298

Next = Address of next node

---

## Linked List Visualization

Head
 ↓
+------+------+
| 10   |  •---|---->
+------+------+
                 +------+------+
                 | 20   |  •---|---->
                 +------+------+
                                  +------+------+
                                  | 30   | None |
                                  +------+------+

None (Null) means the linked list ends here.

---

## Components

Head
- First node of the linked list.

Node
- Stores data and reference to next node.

Next
- Points to the next node.

Null (None)
- Indicates end of linked list.

---

## Memory Representation

Array

Address
1000
1004
1008
1012

Data

10
20
30
40

Memory is contiguous.

---------------------------------------

Linked List

Node1 (Address 5000)
Data = 10
Next = 8200

↓

Node2 (Address 8200)
Data = 20
Next = 3000

↓

Node3 (Address 3000)
Data = 30
Next = None

Nodes can exist anywhere in memory.

---

## Characteristics

✔ Dynamic size

✔ Nodes are connected using pointers (references)

✔ Efficient insertion and deletion

✔ No direct indexing

---

## Advantages

- Dynamic size
- Easy insertion
- Easy deletion
- Memory allocated when needed

---

## Disadvantages

- No random access
- Extra memory required for pointers
- Traversal is slower than arrays

---

## Array vs Linked List

Array

- Contiguous memory
- Index based
- Fast random access
- Insertion at beginning is slow

Linked List

- Non-contiguous memory
- Pointer based
- Sequential access
- Fast insertion and deletion

---

## Time Complexity

Operation                    Array      Linked List

Access by index              O(1)       O(n)

Search                       O(n)       O(n)

Insert at beginning          O(n)       O(1)

Insert at end                O(1)*      O(n)

Delete at beginning          O(n)       O(1)

Delete at end                O(1)*      O(n)

Traversal                    O(n)       O(n)

*Amortized for dynamic arrays.

---

## Python Node

```python
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
```

Example

```python
node1 = Node(10)
node2 = Node(20)

node1.next = node2
```

Visualization

10 → 20 → None

---

## Types of Linked List

1. Singly Linked List

10 → 20 → 30 → None

Each node points only to the next node.

---

2. Doubly Linked List

None ← 10 ⇄ 20 ⇄ 30 → None

Each node stores

- Previous pointer
- Next pointer

---

3. Circular Linked List

10 → 20 → 30
↑           ↓
└───────────┘

Last node points back to the head.

---

## Important Interview Questions

- What is a linked list?
- Difference between array and linked list?
- Why is insertion O(1)?
- Why is searching O(n)?
- Why can't we access index 5 directly?
- What is Head?
- What is Null?
- Difference between singly and doubly linked list?
- When should we use a linked list instead of an array?

---

## Key Points

- A linked list is made of nodes.
- Each node stores data and the address of the next node.
- Nodes are not stored contiguously.
- Access is sequential.
- Random indexing is not possible.
- Insertion and deletion are efficient.
- Traversal always starts from the head node.