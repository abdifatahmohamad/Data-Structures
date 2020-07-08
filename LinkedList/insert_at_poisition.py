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

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node        


    def insertAtPosition(self, position, data):
        if position == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        i = 1
        curr_node = self.head
        while (curr_node is not None) and (i < position - 1):
            curr_node = curr_node.next
            i += 1
        if curr_node is None:
            print("Index out of bound")
        else:
            new_node = Node(data)
            new_node.next = curr_node.next
            curr_node.next = new_node




llist = Linked_list()

llist.insert_tail(1)
llist.insert_tail(2)
llist.insert_tail(4)
llist.insert_tail(5)
llist.insert_tail(6)

llist.insertAtPosition(2, 3)
llist.print_list() # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 