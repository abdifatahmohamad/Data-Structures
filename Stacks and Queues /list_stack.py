# https://stackoverflow.com/questions/18279775/implementing-stack-with-python/64601545#64601545
# https://www.codesdope.com/course/data-structures-stacks/

# https://stackoverflow.com/questions/18279775/implementing-stack-with-python/64601545#64601545
# https://www.codesdope.com/course/data-structures-stacks/

class Stack:
    def __init__(self, length):
        # Three ways to create an empty list:
        # One:
        self.__length = length
        self.__S = [0] * self.__length

        # Two:
        # self.__length = length
        # self.__S = [0 for _ in range(self.__length)]

        # Three:
        # self.__length = length
        # self.__S = [0] * self.__length
        # for i in range(len(self.__S)):
        #     self.__S[i] = 0

        self.__top = -1

    def is_empty(self) -> bool:
        """
        :return: if the stack is empty or not
        """
        return self.__top == -1

    def push(self, x) -> None:
        """
        :return: element that is removed from stack otherwise raise exception
        """
        self.__top += 1
        if self.__top == self.__length:
            raise IndexError("Stack Overflow!")
        else:
            self.__S[self.__top] = x

    # Print stack using string representation
    def __str__(self) -> str:
        print("Printing stack.")
        # Without list comprehension
        # res = []
        # for item in self.__arr:
        #     res.append(str(item))
        # return " ".join(res)

        # Using list comprehension
        return " ".join(str(x) for x in self.__S)

    # Print stack by creating print function/method
    # def print_list(self) -> None:
    #     print("Printing stack.")
    #     for item in self.__arr:
    #         print(item, end=" ")
    #     print()

    def pop(self) -> None:
        """
        :return: element that is removed from stack otherwise raise exception
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            self.__S[self.__top] = 0
            self.__top -= 1
            return self.__S[self.__top]

    def peek(self) -> str:
        """
        :return: get the last element on the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return f"The top element of the stack is: {self.__S[self.__top]}"


if __name__ == '__main__':
    stack = Stack(10)
    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(7)

    print(stack)
    stack.pop()
    stack.pop()

    print(stack)
    print(stack.peek())

    # stack.print_lilength

##########################################################


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
