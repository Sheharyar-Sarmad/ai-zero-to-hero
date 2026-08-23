
class Stack:
    """Enhanced stack with proper error handling"""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top - O(1)"""
        self.items.append(item)
        print(f"Pushed {item} onto stack")
        return self.items

    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")

        item = self.items.pop()
        print(f"Popped {item} from stack")
        return item

    def peek(self):
        """View top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Cannot peek empty stack")

        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items) == 0

    def size(self):
        """Get stack size - O(1)"""
        return len(self.items)

    def __str__(self):
        """String representation"""
        return f"Stack({self.items})"

    def __len__(self):
        """Length support"""
        return len(self.items)

    def __contains__(self, item):
        """Membership check"""
        return item in self.items

    def display(self):
        """Display stack visually"""
        if self.is_empty():
            print("Stack is empty")
            return

        print("\nStack (Top to Bottom):")
        print("  ┌─────┐")
        for i in range(len(self.items) - 1, -1, -1):
            print(f"  │ {self.items[i]:3} │")
        print("  └─────┘")


# Test enhanced version
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()
# Stack (Top to Bottom):
#   ┌─────┐
#   │  30 │
#   │  20 │
#   │  10 │
#   └─────┘

print(stack)  # Stack([10, 20, 30])
print(len(stack))  # 3
print(20 in stack)  # True