# Delete a Node Position
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

    def deleteNode(self, position):
        current_node = self.head
        current_position = 0
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return

        while current_node.next:
            current_position += 1
            if current_position == position:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next


linkedlist = Linkedlist()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

linkedlist.insert(n1)
linkedlist.insert(n2)
linkedlist.insert(n3)
linkedlist.insert(n4)
linkedlist.insert(n5)
linkedlist.insert(n6)

linkedlist.deleteNode(3)  # position number start from 0. from our list 4 is deleted

linkedlist.print_data()

