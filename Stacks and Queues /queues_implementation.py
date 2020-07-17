# Implementing Queue class:

class Queue(object):
    def __init__(self):
        self.items = []

    # Insert items to the list
    def enqueue(self, item):
        # Insert takes index and the item you wanna insert:
        self.items.insert(0, item)

    # Check if the queue is empty:
    def isEmpty(self):
        return self.items == []

    # Pop item from the list:
    def dequeue(self):
        return self.items.pop()

    # Return the top most element of the queue:
    def peek(self):
        if not self.isEmpty():
            # # return self.items[-1]
            return self.items[len(self.items) - 1]


    # Print queue list in Stack object:
    def get_stack(self):
        return self.items

    # Get the length of the queue list:
    def size(self):
        return len(self.items)


# Define our queue object:
queue = Queue()

print(queue.isEmpty()) # True

# Push different data types of items
queue.enqueue(1)
queue.enqueue('A')
queue.enqueue(True)
queue.enqueue(2)
queue.enqueue('B') # Output: ['B', 2, True, 'A', 1]

print(queue.size()) # It gives me 5 coz my list contains 5 items

print(queue.isEmpty()) # It will return False coz I push it some items in the queue

# Pop an item from the stack:
queue.dequeue() # it will remove 1 from the stack

print(queue.peek()) # It will return A coz it's the top most element of the queue

print(queue.get_stack()) # Prints my queue object
