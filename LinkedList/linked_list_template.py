# Create linked list class:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()


def insert(nums):
    head = ListNode(nums[0])
    for node in nums[1:]:
        insert_helper(head, node)
    return head


def insert_helper(head, node):
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = ListNode(node)


def likedlist_cycle(head: ListNode) -> bool:
    slow, fast = head, head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True


nums = [3, 2, 0, -4]
head = insert(nums)
print_list(head)

three = ListNode(3)
two = ListNode(2)
zero = ListNode(0)
n_four = ListNode(-4)

three.next = two
two.next = zero
zero.next = n_four
n_four.next = two

print(likedlist_cycle(head))