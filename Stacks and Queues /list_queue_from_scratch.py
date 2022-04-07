# https://www.youtube.com/watch?v=86QY8mBX7Ks&list=PLJfcKimCUDGvxl_qotoPo9yHr5cPkbX54&index=5
# http://www2.hawaii.edu/~suthers/courses/ics311f20/Notes/Topic-04.html

class Queue:
    def __init__(self, length):
        self.__length = length
        self.__Q = [0] * length
        self.__head = 0
        self.__tail = 0

    # Implement push()
    def enqueue(self, x) -> None:
        if self.is_full():
            raise IndexError('Queue Overflow')
        else:
            self.__Q[self.__tail] = x

            if self.__tail == self.__length:
                self.__tail = 1
            else:
                self.__tail += 1

            # Another way using mod operator
            # self.__Q[self.__tail] = x
            # self.__tail = (self.__tail + 1) % self.__length

    # Implement pop()
    def dequeue(self) -> int:
        if self.is_empty():
            raise Exception('Underflow')
        else:
            x = self.__Q[self.__head]
            self.__Q[self.__head] = 0
            if self.__head == self.__length:
                self.__head = 1
            else:
                self.__head += 1
            return x

            # Another way using mod operator
            # x = self.__Q[self.__head]
            # self.__Q[self.__head] = 0
            # self.__head = (self.__head + 1) % self.__length
            # return x

    # Check if the queue is empty
    def is_empty(self) -> bool:
        return self.__head == self.__tail

    # Check if queue is full
    def is_full(self) -> bool:
        return self.__head == self.__tail + 1

    def size(self) -> str:
        """
        :return: The number of objects in the queue.
        """
        return f"The number of objects in the queue are: {self.__length} objects"

    def front(self) -> str:
        """
        :return: The front (least recently queued) object in the queue, without
        removing it. Error occurs if the queue is empty.
        """
        if self.is_empty():
            raise Exception("The queue is empty!")
        else:
            return f"The least recently queued is: {self.__Q[self.__head]}"

    # Display the queue
    def __str__(self) -> str:
        return ' '.join(str(item) for item in self.__Q)


if __name__ == '__main__':
    queue = Queue(10)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    queue.enqueue(9)

    print("Enqueue the queue: ")
    print(queue)

    print(queue.size())
    print(queue.front())

    queue.dequeue()
    queue.dequeue()

    print("After dequeue: ")
    print(queue)
