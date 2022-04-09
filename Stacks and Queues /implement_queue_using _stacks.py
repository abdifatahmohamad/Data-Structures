class MyQueue:
    # Push, Pop, and Peek Amortized time complexity O(1)
    # https://www.youtube.com/watch?v=RzT6YgrGTyg&t=174s

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        # Keeps trucks what are the front elements in the queue is
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # print("Printing Stack 2: ", self.stack2)
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]

        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2

    # Printing Queue using string representation:
    def __str__(self):
        return f"My queue... \nStack 1: {self.stack1} \nStack 2: {self.stack2}"


if __name__ == '__main__':
    queue = MyQueue()
    queue.push(9)
    queue.push(2)
    print(queue)
    print(
        f"Popped value: {queue.pop()}"
        f"\nPeeked value: {queue.peek()}"
        f"\nIs stack empty?: {queue.empty()}, we still have {queue.stack2} left in our stack."
    )
