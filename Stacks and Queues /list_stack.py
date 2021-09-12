class Stack:
    def __init__(self, capacity):
        self.__arr = [0] * capacity
        self.__capacity = capacity
        self.__top = -1

    def is_empty(self):
        """
        :return: if the stack is empty or not
        """
        if self.__top == -1:
            return True
        return False

    def push(self, item):
        """
        :param item: element to be inserted into stack
        """
        self.__top += 1
        if self.__top == self.__capacity:
            raise IndexError("Stack Overflow")
        else:
            self.__arr[self.__top] = item

    def pop(self):
        """
        :return: element that is removed from stack otherwise raise exception
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            stack_top = self.__arr[self.__top]
            self.__arr[self.__top] = 0
            self.__top -= 1
            return stack_top

    def peek(self):
        """
        :return: get the last element on the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.__arr[self.__top]

    def view(self):
        for item in self.__arr:
            print(item, end=" ")
        print()


stack = Stack(10)

stack.push(5)
stack.push(9)
stack.push(11)

stack.view()

print(stack.peek())

stack.pop()
stack.pop()
stack.pop()

stack.view()
