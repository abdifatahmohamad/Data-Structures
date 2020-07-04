
# Linked List is a collection/sequence of elements/nodes
# where each element links/points to the next element which links/points the next element

# Implementing the Node class(Sub-class of LikedList class):
class Node:
    # Constructor of this class:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Define a LikedList class:
class Linked_list:
    def __init__(self):
        # The head node isn't gonna contain any data (None)
        self.head = Node()

    # Create a helper func that displays the current content in the node list:
    def display(self):
        # Create an empty of list of elements we've seen:
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    # Create a method that inserts node at the beginning/head of the current list(append):
    def insertAtHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Create a method that inserts node at the end/tail of the current list(append):
    # When the ll 1st created, there is no gonna be any list, so append is gonna be first:
    def insertAtTail(self, data):
        # Create new node:
        new_node = Node(data)
        
        # Check if the list is empty:
        # If the list isn't contains a node:
        if self.head is None:
            self.head = new_node
            return

        # If the list contain a node:
        last_node = self.head
        # While current node is not None(empty):
        while last_node.next:
            last_node = last_node.next
        # While next_node is not None, insert new_node:
        # Append the node to the tail/end of the list:
        last_node.next = new_node

    # Create a function the calculates the length of the node:
    def length(self):
        cur = self.head
        total_seen = 0
        while cur.next != None:
            total_seen += 1
            # Traversing to the next node:
            cur = cur.next
        return total_seen

    # Create a func that gets the certain index in the node:
    def get(self, index):
        # Check if the index is not out of the range of the Linked_list:
        if index >= self.length() or index < 0:
            print('ERROR: "Get" Index out of the range!')
            return None

        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1



# Create an instance of out Liked_list:
llist = Linked_list()
llist.display()  # Prints the list is empty
llist.insertAtTail(1)
llist.insertAtTail(2)
llist.insertAtTail(3)
llist.insertAtTail(4)
llist.insertAtTail(5)
llist.display()  # Prints [2, 3, 4, 5]
print(f'The length of this node is: {llist.length()}')  # Prints 'The length of this node is: 4'
print(f'Element at Nth index is: {llist.get(0)}')

####################################################################################################################################




