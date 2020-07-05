
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_head(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            print("list is empty!")
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, '-> ', end='')
            curr_node = curr_node.next
        print()

    def insert_tail(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node





node = Linked_list()

# node.insert_head(7)
# node.insert_head(9)
# node.insert_head(1)
node.insert_tail(7)
node.insert_tail(1)
node.insert_tail(5)
node.insert_tail(8)
node.insert_tail(3)
node.insert_tail(9)
node.print_list()
