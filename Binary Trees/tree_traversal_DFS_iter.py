import collections
from typing import List


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    @staticmethod
    def inorder_traversal(root) -> List:
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res

    @staticmethod
    def preorder_traversal(root) -> List:
        # stack: to keep track of the nodes when traversing the tree
        # and we push the root to the stack
        stack, res = [root], []
        # Loop until the stack is empty
        while stack:
            node = stack.pop()
            res.append(node.val)
            # The right child is pushed first to the stack so that the left
            # child is processed first.
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return res

    @staticmethod
    def postorder_traversal(root) -> List:
        res = []
        if root is None:
            return res

        stack = []
        last_visited_node = None
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)  # offerLast
                curr = curr.left
            else:
                top = stack[-1]  # peekLast
                if top.right and top.right != last_visited_node:
                    curr = top.right
                else:
                    res.append(top.val)
                    stack.pop()  # pollLast
                    last_visited_node = top
        return res


# def build_tree() -> None:
#     tree = TreeNode(1)
#     tree.right = TreeNode(2)
#     tree.right.left = TreeNode(3)
#     print(Solution().inorder_traversal(tree))


def create_tree(arr):
    num_queue = collections.deque()
    for num in arr[1:]:
        num_queue.append(num)

    queue = collections.deque()
    root = TreeNode(arr[0])
    queue.append(root)

    while num_queue:
        left_val = None if not num_queue else num_queue.popleft()
        right_val = None if not num_queue else num_queue.popleft()
        current = queue.popleft()
        if left_val:
            left = TreeNode(left_val)
            current.left = left
            queue.append(left)
        if right_val:
            right = TreeNode(right_val)
            current.right = right
            queue.append(right)
    return root


""" 
Constructed binary tree is
            1
             \
              2
             / 
            3

"""

if __name__ == "__main__":
    tree = create_tree([1, None, 2, 3])
    print(Solution().inorder_traversal(tree))
    print(Solution().preorder_traversal(tree))
    print(Solution().postorder_traversal(tree))

    '''
    [1, 3, 2]
    [1, 2, 3]
    [3, 2, 1]
    '''
    # build_tree()
