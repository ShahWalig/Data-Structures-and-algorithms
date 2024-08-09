class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    # def print_data(self):
    #     current_node = self.head
    #     while current_node is not None:
    #         print(current_node.data)
    #         current_node = current_node.next

    def reverse(self):
        current_node = self.head
        previous_node = None
        while current_node:
            next_of_current_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_of_current_node
        self.head = previous_node
        new_current_node = self.head
        while new_current_node:
            print(new_current_node.data)
            new_current_node = new_current_node.next


f1 = Node(1)
f2 = Node(2)
f3 = Node(3)
f4 = Node(4)
f5 = Node(5)
f6 = Node(6)
linklist = LinkedList()
linklist.insert(f1)
linklist.insert(f2)
linklist.insert(f3)
linklist.insert(f4)
linklist.insert(f5)
linklist.insert(f6)
linklist.reverse()
