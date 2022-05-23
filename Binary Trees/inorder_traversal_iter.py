class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    @staticmethod
    def inorder_traversal_iter(root):
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            print(root.val, end=" -> ")
            root = root.right
        print("None")

        return stack


#                1
#              /   \
#             2     3
#            /  \  /  \
#           4    5 6   7
#                 \     \
#                  8     9

# inorder traversal: left, root, right
# [4, 2, 5, 8, 1, 6, 3, 7, 9]

def build_tree():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)
    tree.left.right.right = TreeNode(8)
    tree.right.right.right = TreeNode(9)

    tree.inorder_traversal_iter(tree)


if __name__ == "__main__":
    build_tree()
