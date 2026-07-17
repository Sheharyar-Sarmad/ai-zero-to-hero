class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def show(self):
        if self.head is None:
            print("Link List is empty!")
            return

        itr = self.head
        llstr = ""

        while itr:
            llstr += "--" + str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        # If the linked list is empty
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        # Move to the last node
        while itr.next:
            itr = itr.next

        # Connect the last node to the new node
        itr.next = Node(data, None)
        
    def insert_values(self , data_list):
        self.head = None
        
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        if self.head == None:
            print("Link List is empty!")
        
        count = 0
        itr = self.head
        
        while itr:
            itr = itr.next
            count += 1
        
        return count

if __name__ == "__main__":
    ll = LinkList()

    ll.insert_at_begining(12)
    ll.insert_at_begining(10)
    ll.insert_at_begining(5)

    ll.insert_at_end(34)
    ll.insert_at_end(45)

    ll.insert_values([1,2,3,4,5,6,7,8,9,10])
    length = ll.get_length()
    print(length)
    ll.show()