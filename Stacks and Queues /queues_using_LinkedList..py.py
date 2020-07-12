# Implementing Queue class using linked list:
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def print_queue(self):
        curr_node = self.first
        while curr_node is not None:
            print(curr_node.val, end=' <- ')
            curr_node = curr_node.next
        print()

    def enqueue(self, val):
        new_node = Node(val)
        if self.first is None:
            self.first = new_node
            self.last = self.first
            self.length += 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1

    # Get the length of the queue list:
    def size(self):
        return f'This list contains: {self.length} elements'

    # Get the top most element of the stack:
    def peek(self):
        return f'The top most element of this queue is: {self.first.val}'

    def dequeue(self):
        temp = self.first.next
        # dequeued_element = self.first
        if temp == None:
            self.first = None
            self.length -= 1
            return
        self.first.next = None
        self.first = temp
        self.length -= 1


queue = Queue()

# queue.print_stack() # Prints empty list
queue.enqueue(1)
queue.enqueue('A')
queue.enqueue(True)
queue.enqueue(2)
queue.enqueue('B')
queue.print_queue() # Prints my queue object
print(queue.size()) # It gives me 5 coz my list contains 5 items
queue.print_queue()
queue.dequeue() # It will print: A <- True <- 2 <- B <-
print(queue.peek()) # # It will gets us A coz it's the top most element of the queue
queue.print_queue()  # Prints my queue object
