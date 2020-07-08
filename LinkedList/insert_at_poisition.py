class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print('List is empty')
            return

        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=' -> ')
            curr_node = curr_node.next

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at this location (index) to this value(value) into the list:
    def insert(self, position, data):
        if position == 0:
            self.insert_head(data)

        i = 0
        curr_node = self.head
        while (curr_node is not None) and (i < position -1):
            curr_node = curr_node.next
            i += 1

        if curr_node is None:
            print('Invalid position')
        else:
            new_node = Node(data)
            new_node.next = curr_node.next
            curr_node.next = new_node




llist = Linked_list()

llist.insert_head(6)
llist.insert_head(5)
llist.insert_head(4)
llist.insert_head(2)
llist.insert_head(1)

llist.insert(2, 3)
llist.print_list() # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 