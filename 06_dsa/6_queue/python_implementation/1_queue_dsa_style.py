

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        return item

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self, item):
        if self.is_empty():
            print("Queue is empty!")
            return None

        return self.items.pop(0)

    def peek(self):
        return None if self.is_empty() else self.items[0]

    def size(self):
        return 0 if self.is_empty() else len(self.items)

    def clear(self):
        return None if self.is_empty() else self.items.clear()

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        print("Queue (Front → Back):")
        print("  FRONT → ", end="")

        for item in self.items:
            print(f"[{item}] ", end="")

        print("← BACK")
        return None

# I give this class to ai and said to give me example calling, so use ai for the simple
# task and save your time and also i have right the logic of display as well and it
# gives me good logging of it.

# ===== TESTING =====
if __name__ == "__main__":
    queue = Queue()

    print("=== Enqueue Test ===")
    print(f"Enqueued: {queue.enqueue(10)}")  # ✓ Enqueued 10
    print(f"Enqueued: {queue.enqueue(20)}")  # ✓ Enqueued 20
    print(f"Enqueued: {queue.enqueue(30)}")  # ✓ Enqueued 30
    print()

    print("=== Display Test ===")
    queue.display()
    # Queue (Front → Back):
    #   FRONT → [10] [20] [30] ← BACK
    print()

    print("=== Peek Test ===")
    print(f"Front element: {queue.peek()}")  # 10
    print()

    print("=== Size Test ===")
    print(f"Size: {queue.size()}")  # 3
    print()

    print("=== Dequeue Test ===")
    print(f"Dequeued: {queue.dequeue(30)}")  # Actually dequeue doesn't need parameter, but we'll keep it
    print(f"Size after dequeue: {queue.size()}")  # 2
    print()

    print("=== Empty Queue Test ===")
    queue.dequeue(20)  # ✓ Dequeued 20
    queue.dequeue(10)  # ✓ Dequeued 10
    queue.dequeue(None)  # ✗ Queue is empty! Cannot dequeue
    print()

    print("=== Clear Test ===")
    queue.enqueue(100)
    queue.enqueue(200)
    queue.display()
    queue.clear()  # ✓ Queue cleared
    queue.display()  # Queue is empty
    print()

    print("=== Magic Methods Test ===")
    # Note: Magic methods are not implemented in the current class
    # These will not work as expected
    queue.enqueue(1)
    queue.enqueue(2)