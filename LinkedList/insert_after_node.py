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
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print()

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print('Previous node is not in the list')
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


llist = Linked_list()

llist.insert_tail('A')
llist.insert_tail('B')
llist.insert_tail('D')
llist.insert_tail('F')

# print(llist.head.data) # It gonna print A
# print(llist.head.next.data) # It gonna print B

llist.insert_after_node(llist.head.next, 'A') # It prints: A -> B -> C -> D -> F ->
llist.print_list()
