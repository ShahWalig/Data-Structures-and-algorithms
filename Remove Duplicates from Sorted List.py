# Remove Duplicates from Sorted List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def print_data(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def delete_duplicate(self):
        current_node = self.head
        while current_node and current_node.next:
            while current_node.next and current_node.data == current_node.next.data:
                current_node.next = current_node.next.next
            current_node = current_node.next

linkedlist = Linkedlist()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(3)
n5 = Node(4)
n6 = Node(4)
n7 = Node(4)
n8 = Node(5)
n9 = Node(6)
n10 = Node(6)
n11 = Node(6)

linkedlist.insert(n1)
linkedlist.insert(n2)
linkedlist.insert(n3)
linkedlist.insert(n4)
linkedlist.insert(n5)
linkedlist.insert(n6)
linkedlist.insert(n7)
linkedlist.insert(n8)
linkedlist.insert(n9)
linkedlist.insert(n10)
linkedlist.insert(n1)
linkedlist.delete_duplicate()
linkedlist.print_data()
