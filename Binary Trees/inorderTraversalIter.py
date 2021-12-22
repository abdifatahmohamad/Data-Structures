# Leetcode class base solution
from typing import List, Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        while stack or root:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                tempNode = stack.pop()
                result.append(tempNode.val)
                root = tempNode.right

        return result


#                1
#              /   \
#             2     3
#            /  \  /  \
#           4    5 6   7
#                 \     \
#                  8     9

# inorder traversal: left, root, right
# [4, 2, 5, 8, 1, 6, 3, 7, 9]

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)
tree.left.right.right = TreeNode(8)
tree.right.right.right = TreeNode(9)


print(Solution().inorderTraversal(tree))
