
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning (O(1))
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end (O(n))
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert after a given node (O(1) if node is known)
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node cannot be None")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Delete by value (O(n))
    def delete_node(self, key):
        current = self.head

        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key not found
        if not current:
            print(f"Value {key} not found")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    # Search for a value (O(n))
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Print the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Usage example
ll = LinkedList()
ll.insert_at_beginning(30)
ll.insert_at_beginning(20)
ll.insert_at_beginning(10)
ll.insert_at_end(40)

ll.display()  # 10 -> 20 -> 30 -> 40 -> None

ll.delete_node(20)
ll.display()  # 10 -> 30 -> 40 -> None

print(ll.search(30))  # True
print(ll.search(50))  # False