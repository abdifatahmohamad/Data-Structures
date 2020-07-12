# Implementing Stack class:

class Stack(object):
    def __init__(self):
        self.items = []

    # Push items to the list
    def push(self, item):
        self.items.append(item)

    # Check if the stack is empty:
    def isEmpty(self):
        return self.items == []

    # Pop item from the list:
    def pop(self):
        return self.items.pop()

    # Return the top most element of the stack:
    def peek(self):
        if not self.isEmpty():
            # return self.items[-1]
            return self.items[len(self.items) - 1]

    # Print stack list in Stack object:
    def get_stack(self):
        return self.items

    # Get the length of the stack list:
    def size(self):
        return len(self.items)


# Define our stack object:
stack = Stack()

print(stack.isEmpty()) # True

# Push different data types of items
stack.push(1)
stack.push('A')
stack.push(True)
stack.push(2)
stack.push('B') # Output: [1, 'A', True, 2, 'B']

print(stack.size()) # It gives me 5 coz my list contains 5 items

print(stack.isEmpty()) # It will return False coz I push it some items in the stack

# Pop an item from the stack:
stack.pop() # it will remove ['B'] from the stack

print(stack.peek()) # It will return 2 coz it's the top most element of the stack

print(stack.get_stack()) # Prints my stack object 
