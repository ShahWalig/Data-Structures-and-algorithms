class Node:
    def __init__(self, data):
        # Initialize a node with the given data and set the next pointer to None
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        # Initialize an empty linked list with head set to None
        self.head = None

    def insert(self, new_node):
        # Insert a new node at the end of the linked list
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            # Traverse to the end of the list
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            # Append the new node at the end
            current_node.next = new_node

    def print_data(self):
        # Print the data values of all nodes in the linked list
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()  # Print a new line after listing all node data

    def append_k_node(self):
        # Traverse the list and append new nodes with GCD of adjacent node values
        prev = None
        curr = self.head

        # Traverse the list while there are at least two nodes
        while curr and curr.next:
            # Update previous and current pointers
            prev = curr
            curr = curr.next

            # Calculate the Greatest Common Divisor (GCD) of prev and curr node values
            a = prev.data
            b = curr.data
            while b != 0:
                remainder = a % b
                a = b
                b = remainder

            # Create a new node with the GCD value
            new_node = Node(a)

            # Insert the new node between prev and curr
            prev.next = new_node
            new_node.next = curr

            # Update pointers for the next iteration
            prev = new_node
            curr = new_node.next


# Create nodes with specified values
f1 = Node(18)
f2 = Node(6)
f3 = Node(10)
f4 = Node(3)

# Create and populate the linked list
linklist = LinkedList()
linklist.insert(f1)
linklist.insert(f2)
linklist.insert(f3)
linklist.insert(f4)

# Append new nodes with GCD values between original nodes
linklist.append_k_node()

# Print the resulting linked list to verify the output
linklist.print_data()

# Expected Output: [18, 6, 6, 2, 10, 1, 3]
