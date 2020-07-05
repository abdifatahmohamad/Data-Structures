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
            print(curr_node.data, end=" <- ")
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

    def reverse(self):
        curr, prev = self.head, None
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

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

# Reverse the whole list:
llist.reverse() # It will reverse when inserted from from like this: 1 -> 2 -> 3 -> 4 ->

# To display/print our LikedList
llist.print_list()

#######################################################################################
# Reverse linked list while using functions based Node class:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()

def reverse(head: ListNode) -> ListNode:
    curr, prev = head, None
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

print_list(node)

reversedNode = reverse(node)
print_list(reversedNode)
