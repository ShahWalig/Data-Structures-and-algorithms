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
n31 = Node(3)
n4 = Node(4)
n5 = Node(4)
n51 = Node(4)
n52 = Node(5)
n6 = Node(6)
n61 = Node(6)
n62 = Node(6)

linkedlist.insert(n1)
linkedlist.insert(n2)
linkedlist.insert(n3)
linkedlist.insert(n31)
linkedlist.insert(n4)
linkedlist.insert(n5)
linkedlist.insert(n51)
linkedlist.insert(n52)
linkedlist.insert(n6)
linkedlist.insert(n61)
linkedlist.insert(n62)
linkedlist.delete_duplicate()
linkedlist.print_data()
