# Given a singly linked list, determine if it is a palindrome.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_tail(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return
    last_node = head
    while last_node.next is not None:
        last_node = last_node.next
    last_node.next = new_node


def print_list(head):
    if head is None:
        print('The list is empty')
        return
    curr_node = head
    while curr_node is not None:
        print(curr_node.data, end=' -> ')
        curr_node = curr_node.next
    print()


class Solution:
    def is_palindrome(self, head):
        slow = head
        fast = head
        while (fast is not None) and (slow is not None):
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse_list(slow)
        fast = head
        while slow is not None:
            if slow.data != fast.data:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def reverse_list(self, head):
        curr_node = head
        prev_node = None
        while curr_node is not None:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        return prev_node

arr = [1,2,3,3,2,1]
node = Node(arr[0])
for i in range(1, len(arr)):
    insert_tail(node, arr[i])
print(node)

test = Solution()
print(test.is_palindrome(node))