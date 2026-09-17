
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Points to next node
        self.prev = None  # Points to previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # First node
        self.tail = None  # Last node (optional but useful)
        self.size = 0  # Track size (optional)

    # INSERTION OPERATIONS

    # Insert at beginning - O(1)
    def insert_at_beginning(self, data):
        new_node = Node(data)

        if not self.head:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    # Insert at end - O(1) with tail pointer
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.tail:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    # Insert at specific position - O(n)
    def insert_at_position(self, data, position):
        if position < 0 or position > self.size:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        if position == self.size:
            self.insert_at_end(data)
            return

        new_node = Node(data)
        current = self.head

        # Traverse to position
        for _ in range(position - 1):
            current = current.next

        # Insert between current and current.next
        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node

        self.size += 1

    # Insert after a given node - O(1)
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node cannot be None")
            return

        new_node = Node(data)
        new_node.prev = prev_node
        new_node.next = prev_node.next

        if prev_node.next:
            prev_node.next.prev = new_node
        else:
            self.tail = new_node  # Inserting after last node

        prev_node.next = new_node
        self.size += 1

    # Insert before a given node - O(1)
    def insert_before_node(self, next_node, data):
        if not next_node:
            print("Next node cannot be None")
            return

        new_node = Node(data)
        new_node.next = next_node
        new_node.prev = next_node.prev

        if next_node.prev:
            next_node.prev.next = new_node
        else:
            self.head = new_node  # Inserting before first node

        next_node.prev = new_node
        self.size += 1

    # DELETION OPERATIONS

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
            self.head.prev = None

        self.size -= 1
        return deleted_data

    # Delete from end - O(1) with tail pointer
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
            self.tail.next = None

        self.size -= 1
        return deleted_data

    # Delete by value - O(n)
    def delete_by_value(self, key):
        if not self.head:
            print("List is empty")
            return False

        current = self.head

        # Search for the node
        while current and current.data != key:
            current = current.next

        if not current:  # Not found
            print(f"Value {key} not found")
            return False

        # Delete the node
        if current == self.head:
            self.delete_from_beginning()
        elif current == self.tail:
            self.delete_from_end()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1

        return True

    # Delete at specific position - O(n)
    def delete_at_position(self, position):
        if position < 0 or position >= self.size:
            print("Invalid position")
            return None

        if position == 0:
            return self.delete_from_beginning()

        if position == self.size - 1:
            return self.delete_from_end()

        current = self.head
        for _ in range(position):
            current = current.next

        deleted_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1

        return deleted_data

    # SEARCH OPERATIONS

    # Search by value - O(n)
    def search(self, key):
        current = self.head
        position = 0

        while current:
            if current.data == key:
                return position
            current = current.next
            position += 1

        return -1  # Not found

    # Search from end (backward) - O(n)
    def search_from_end(self, key):
        current = self.tail
        position = self.size - 1

        while current:
            if current.data == key:
                return position
            current = current.prev
            position -= 1

        return -1  # Not found

    # ACCESS OPERATIONS

    # Get node at position - O(n)
    def get_node(self, position):
        if position < 0 or position >= self.size:
            return None

        # Optimize: traverse from closer end
        if position < self.size // 2:
            current = self.head
            for _ in range(position):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - 1 - position):
                current = current.prev

        return current

    # Get data at position - O(n)
    def get_data(self, position):
        node = self.get_node(position)
        return node.data if node else None

    # TRAVERSAL OPERATIONS

    # Display forward - O(n)
    def display_forward(self):
        if not self.head:
            print("Empty list")
            return

        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Display backward - O(n)
    def display_backward(self):
        if not self.tail:
            print("Empty list")
            return

        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    # Display with details (shows prev and next pointers)
    def display_detailed(self):
        if not self.head:
            print("Empty list")
            return

        current = self.head
        position = 0
        while current:
            prev_data = current.prev.data if current.prev else "None"
            next_data = current.next.data if current.next else "None"
            print(f"Pos {position}: [prev={prev_data}] <- [{current.data}] -> [next={next_data}]")
            current = current.next
            position += 1

    # UTILITY OPERATIONS

    # Check if list is empty - O(1)
    def is_empty(self):
        return self.head is None

    # Get size - O(1)
    def get_size(self):
        return self.size

    # Reverse the list - O(n)
    def reverse(self):
        if not self.head or self.head == self.tail:
            return  # Empty or single node

        current = self.head
        self.tail = self.head  # Old head becomes new tail

        while current:
            # Swap prev and next pointers
            temp = current.prev
            current.prev = current.next
            current.next = temp

            # Move to next node (which is now prev)
            current = current.prev

        # Set new head (old tail)
        if temp:
            self.head = temp.prev

    # Clear the list - O(1)
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Convert to list - O(n)
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    # Convert from list - O(n)
    def from_list(self, lst):
        self.clear()
        for item in lst:
            self.insert_at_end(item)


# TESTING
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("=== Insertion Tests ===")
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_beginning(5)
    dll.insert_at_position(15, 2)
    dll.display_forward()  # 5 <-> 10 <-> 15 <-> 20 <-> 30 <-> None

    print("\n=== Display Backward ===")
    dll.display_backward()  # 30 <-> 20 <-> 15 <-> 10 <-> 5 <-> None

    print("\n=== Detailed Display ===")
    dll.display_detailed()

    print("\n=== Search Tests ===")
    print(f"Position of 15: {dll.search(15)}")
    print(f"Position of 25: {dll.search(25)}")
    print(f"Position of 20 from end: {dll.search_from_end(20)}")

    print("\n=== Access Tests ===")
    print(f"Data at position 2: {dll.get_data(2)}")
    print(f"Data at position 4: {dll.get_data(4)}")

    print("\n=== Deletion Tests ===")
    dll.delete_from_beginning()
    print("After deleting from beginning:")
    dll.display_forward()

    dll.delete_from_end()
    print("After deleting from end:")
    dll.display_forward()

    dll.delete_by_value(15)
    print("After deleting 15:")
    dll.display_forward()

    dll.delete_at_position(1)
    print("After deleting position 1:")
    dll.display_forward()

    print("\n=== Reverse Test ===")
    dll.insert_at_end(50)
    dll.insert_at_end(60)
    print("Before reverse:")
    dll.display_forward()
    dll.reverse()
    print("After reverse:")
    dll.display_forward()

    print("\n=== Utility Tests ===")
    print(f"Size: {dll.get_size()}")
    print(f"Is empty: {dll.is_empty()}")
    print(f"As list: {dll.to_list()}")

    print("\n=== Clear Test ===")
    dll.clear()
    print(f"After clear - Size: {dll.get_size()}")
    dll.display_forward()