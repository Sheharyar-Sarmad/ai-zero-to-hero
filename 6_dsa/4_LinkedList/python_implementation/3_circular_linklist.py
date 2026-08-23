class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert at beginning - O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if not self.head:  # Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

        self.size += 1

    # Insert at end - O(1)
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:  # Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.size += 1

    # Delete from beginning - O(1)
    def delete_from_beginning(self):
        if not self.head:
            print("List is empty")
            return None

        deleted_data = self.head.data

        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

        self.size -= 1
        return deleted_data

    # Delete from end - O(1)
    def delete_from_end(self):
        if not self.tail:
            print("List is empty")
            return None

        deleted_data = self.tail.data

        if self.head == self.tail:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

        self.size -= 1
        return deleted_data

    # Display forward - O(n)
    def display_forward(self):
        if not self.head:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print(f"(back to head: {self.head.data})")

    # Display backward - O(n)
    def display_backward(self):
        if not self.tail:
            print("Empty list")
            return

        current = self.tail
        while True:
            print(current.data, end=" <-> ")
            current = current.prev
            if current == self.tail:
                break
        print(f"(back to tail: {self.tail.data})")


# TESTING
if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()

    print("=== Circular Doubly Linked List Tests ===")
    cdll.insert_at_end(10)
    cdll.insert_at_end(20)
    cdll.insert_at_end(30)
    cdll.insert_at_beginning(5)

    print("Forward traversal:")
    cdll.display_forward()  # 5 <-> 10 <-> 20 <-> 30 <-> (back to head: 5)

    print("\nBackward traversal:")
    cdll.display_backward()  # 30 <-> 20 <-> 10 <-> 5 <-> (back to tail: 30)

    print("\nDeletion tests:")
    cdll.delete_from_beginning()
    print("After deleting from beginning:")
    cdll.display_forward()

    cdll.delete_from_end()
    print("After deleting from end:")
    cdll.display_forward()