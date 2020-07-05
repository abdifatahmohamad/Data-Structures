# Implementing linked list class:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print('The list is empty')
            return

        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" -> ")  # The pointer goes right for insertion at the tail
            # print(curr_node.data, end=" <- ") # The pointer goes left for insertion at the head
            curr_node = curr_node.next
        print()

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

llist = Linked_list()

# Intersion at the front:
llist.insert_head(1)
llist.insert_head(2)
llist.insert_head(3)
llist.insert_head(4)

# Insertion at the end:
# llist.insert_tail(1)
# llist.insert_tail(2)
# llist.insert_tail(3)
# llist.insert_tail(6)

# To display/print our LikedList
llist.print_list()
