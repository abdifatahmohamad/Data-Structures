class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    # left root right
    def inorder_traversal(self, root):
        # Base case:
        if not root:
            return

        self.inorder_traversal(root.left)
        print(root.val, end=" -> ")
        self.inorder_traversal(root.right)

# In-order traversal putting all nodes in an array
#     @staticmethod
#     def inorder_traversal(root):
#         res = []
#         inorder_traversal_util(root, res)
#         print(res)
#
#
# def inorder_traversal_util(root, res):
#     if root is None:
#         return
#
#     inorder_traversal_util(root.left, res)
#     res.append(root.val)
#     inorder_traversal_util(root.right, res)


def build_tree():
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(11)
    tree.right.left = TreeNode(13)
    tree.left.left.left = TreeNode(7)
    tree.left.left.right = TreeNode(2)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)

    tree.inorder_traversal(tree)


if __name__ == "__main__":
    build_tree()
