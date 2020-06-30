
# Linked List is a collection/sequence of elements/nodes
# where each element links/points to the next element which links/points the next element
# Create a node class in a singly linked list:
'''class SinglyLinkedListNode(object):

    def __init__(self, value):
        self.value = value
        # Since it's singly linked list we care about next node we pointing to:
        self.nextnode = None


# Now we can build out Linked List as a collection of nodes:
# Create instances of the node objects:
a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)

# we want to link the above nodes together:
# Assign what the next node are:
a.nextnode = b
b.nextnode = c

# Now we can check the value from it:
# Call the values:
print(a.value) # prints 1

# Now we can also check the node that is coming next:
print(a.nextnode.value) # prints 2
print(b.nextnode.value) # prints 3'''

########################################################
# Implementing Doubly Linked List Class Node:

class DoublyLinkedListNode(object):

    # Initialize the atrribute that we are gonna use it:
    def __init__(self, value):

        self.value = value
        self.next_node = None
        self.prev_node = None



# Create instance of the above node objects that can refernce next and previous values:

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

# Define the doubly linked list:
# Setting b after a
b.next_node = a
a.prev_node = b

# Setting c after a
b.next_node = c
c.prev_node = b

# Now we can check the value from it:
# Call the values:
# print(a.value) # prints 1

# Now we can also check the node that is coming next:
print(b.next_node.value) # prints 3
print(c.prev_node.value) # prints 2

########################################################


