# Implementing Stack class using linked list:

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def print_stack(self):
        if self.bottom is None:
            print('The list is empty')
            return

        curr_node = self.bottom
        while curr_node is not None:
            print(curr_node.val, end=' -> ')
            curr_node = curr_node.next
        print()

    def push(self, data):
        new_node = Node(data)
        if self.bottom is None:
            self.bottom = new_node
            self.top = self.bottom
            self.length = 1
        else:
            self.top.next = new_node
            self.top = self.top.next
            self.length += 1

    # Get the length of the stack list:
    def size(self):
        return f'This list contains: {self.length} elements'

    # Get the top most element of the stack:
    def peek(self):
        return f'The top most element of this stack is: {self.top.val}'

    def pop(self):
        i = 1
        curr_node = self.bottom
        while i != self.length - 1:
            curr_node = curr_node.next
            i += 1
        popped_value = curr_node.next
        curr_node.next = None
        self.top = curr_node
        self.length -= 1
        return popped_value.val

stack = Stack()

# stack.print_stack() # Prints empty list
stack.push(1)
stack.push('A')
stack.push(True)
stack.push(1)
stack.push('B')
stack.print_stack() # Prints my stack object
print(stack.size()) # It gives me 5 coz my list contains 5 items
stack.print_stack()
stack.pop() # It will print: 1 -> A -> True -> 1 -> 
print(stack.peek()) # # It will gets us B coz it's the top most element of the stack
stack.print_stack() # Prints my stack object

