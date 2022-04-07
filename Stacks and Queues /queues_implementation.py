from collections import deque


# Queue is FIFO (first in first out)
class Queue(object):
    def __init__(self):
        # 1. Queue using a list
        # self.items = []

        # 2. Queue using double ended queue using deque built-in
        self.items = deque()

    def is_empty(self):
        # return self.items == [] If we were to use list implementation method

        return len(self.items) == 0

    # Insert/append items to the list
    def enqueue(self, val):
        # 1. Queue using a list -> Insert takes index and the item you wanna insert:
        # self.my_queue.insert(0, val)

        # 2. Queue using double ended queue using deque built-in
        self.items.appendleft(val)

    # Pop item from the list:
    def dequeue(self):
        if len(self.items) == 0:
            print("Queue is empty")
            return

        return self.items.pop()

    # Return the front element of the queue:
    def front(self):
        if not self.is_empty():
            # return self.items[-1]

            return self.items[len(self.items) - 1]

    # Get the length of the queue list:
    def size(self):
        return len(self.items)

    # Print queue using string representation
    def __str__(self):
        return f"My queue: {self.items}"


# Define our queue object:
queue = Queue()

print(queue.is_empty())  # True

# Push different data types of items
queue.enqueue(1)
queue.enqueue('A')
queue.enqueue(True)
queue.enqueue(2)
queue.enqueue('B')  # Output: ['B', 2, True, 'A', 1]

print(queue.size())  # It gives me 5 coz my list contains 5 items

# It will return False coz I push it some items in the queue
print(queue.is_empty())

# Pop an item from the queue:
queue.dequeue()  # it will remove 1 from the queue

print(queue.peek())  # It will return A coz it's the top most element of the queue

print(queue)
