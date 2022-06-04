import collections
from typing import List


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class Solution:
    @staticmethod
    def inorder_traversal(root) -> List:
        res = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res

    @staticmethod
    def preorder_traversal(root) -> List:
        res = []

        def preorder(root):
            if not root:
                return

            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return res

    @staticmethod
    def postorder_traversal(root) -> List:
        res = []

        def postorder(root):
            if not root:
                return

            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
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
    # build_tree()
