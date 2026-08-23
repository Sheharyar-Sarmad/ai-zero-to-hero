
## Linked List Notes

## Why Linked Lists?

## Problem Arrays Face:

Fixed size (static memory allocation)

Costly insertions/deletions (O(n) shifting)

Memory fragmentation issues

Wasted memory if overallocated

## What Linked Lists Solve:

Dynamic size (grows/shrinks on demand)

O(1) insertions/deletions at beginning

No shifting elements needed

Efficient memory usage

## Core Concept

Node-based structure:

[data | next] → [data | next] → [data | next] → NULL
Each node contains:

Data: Actual value

Pointer: Reference to next node

## Types & Comparisons

## 1. Singly Linked List

Head → [data|next] → [data|next] → [data|next] → NULL
Traversal: Forward only

Memory: Less (1 pointer/node)

Use when: Memory tight, forward traversal sufficient

## 2. Doubly Linked List

NULL ← [prev|data|next] ↔ [prev|data|next] ↔ [prev|data|next] → NULL
Traversal: Both directions

Memory: More (2 pointers/node)

Use when: Frequent bidirectional navigation

## 3. Circular Linked List

Head → [data|next] → [data|next] → [data|next] ─┐
         ↑                                        │
         └────────────────────────────────────────┘
Traversal: Infinite loop possible

Memory: Similar to singly

Use when: Circular buffering, round-robin scheduling

## Time Complexity Cheat Sheet

## Operation	      Singly	Doubly

Insert at head	  O(1)	    O(1)
Insert at tail	  O(n)*	    O(1)**
Delete at head	  O(1)	    O(1)
Delete at tail	  O(n)	    O(1)
Search	          O(n)	    O(n)
Access by index	  O(n)	    O(n)

*With tail pointer: O(1)
**With tail pointer: O(1)

## Key Advantages

Dynamic sizing - No predefined capacity

Efficient insertion/deletion - Just pointer manipulation

No memory waste - Allocates only what needed

Implementation of other structures - Stacks, queues, graphs

## Trade-offs

Memory overhead: Extra pointers (8 bytes each on 64-bit)
Cache unfriendly: Non-contiguous memory access
No random access: Must traverse from head

##  Common Use Cases

Undo/Redo (doubly linked)

Browser history (doubly linked)

Music playlist (circular)

Process scheduling (circular)

Hash table chaining (singly)

Adjacency lists (singly)

## Implementation Checklist

□ Node structure definition
□ Head pointer management
□ Insertion (beginning, end, position)
□ Deletion (by value, by position)
□ Traversal/Display
□ Search operation
□ Reverse linked list
□ Detect cycle (Floyd's algorithm)
□ Find middle node

## Memory Management

malloc()/new for creation

free()/delete for destruction

Prevent memory leaks by freeing all nodes

Handle NULL pointer checks

## Edge Cases

Empty list (head = NULL)

Single node operations

Insert/delete at boundaries

Circular reference detection

Tail pointer maintenance