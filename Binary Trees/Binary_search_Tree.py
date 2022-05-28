from typing import List


class BST(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add_child(self, data):
        # BST can't have a duplicates
        if data == self.val:
            return
            # print("Element is duplicate.")

        if self.val < data:
            # Add data in left sub_tree
            if self.left is not None:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            # Add data in right sub_tree
            if self.right is not None:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    @staticmethod
    def inorder_traversal(root) -> None:
        result = []
        inorder_traversal_util(root, result)
        print(result)


def inorder_traversal_util(root, result):
    # Base case
    if root is None:
        return

    inorder_traversal_util(root.left, result)
    result.append(root.val)
    inorder_traversal_util(root.right, result)


#                 15
#              /     \
#             12      27
#            /  \    / \
#           7   14  20  88
#                     \
#                     23

# inorder traversal: left, root, right
# [7, 12, 14, 15, 20, 23, 27, 88]

# pre-order traversal: root, left, right
# [15, 12, 7, 14, 27, 20, 23, 88]

# post-order traversal: left, right, root
# [7, 14, 12, 23, 20, 88, 27, 15]

def build_tree():
    tree = BST(15)
    tree.left = BST(12)
    tree.right = BST(27)
    tree.left.left = BST(7)
    tree.left.right = BST(14)
    tree.right.left = BST(20)
    tree.right.right = BST(88)
    tree.right.left.right = BST(23)
    # tree.right.left.right = BST(88)
    # tree.add_child(20)

    tree.inorder_traversal(tree)


if __name__ == "__main__":
    build_tree()
