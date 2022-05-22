class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    # left root right
    def inorder_traversal(self, root):
        # Base case:
        if not root:
            return

        self.inorder_traversal(root.left)
        print(root.val, end=" ")
        self.inorder_traversal(root.right)

    # Function finds each path of the tree
    @staticmethod
    def path_finder(root):
        path_finder_helper(root, "")

    # Function sums up each path of the tree
    @staticmethod
    def sum_path(root):
        lst = []
        sum_path_helper(root, lst, 0)
        print(lst)


def path_finder_helper(root, cur_val):
    # Base case:
    if not root:
        return

    cur_val += str(root.val) + " -> "
    if root.left is None and root.right is None:
        print(cur_val, "None")

    path_finder_helper(root.left, cur_val)
    path_finder_helper(root.right, cur_val)


def sum_path_helper(root, lst, curSum):
    # Base case:
    if not root:
        return

    curSum += root.val
    if root.left is None and root.right is None:
        lst.append(curSum)

    sum_path_helper(root.left, lst, curSum)
    sum_path_helper(root.right, lst, curSum)


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

    tree.inorder_traversal(tree)
    print()
    print("Printing node paths: ")
    tree.path_finder(tree)
    print("Sum all paths of the tree:")
    tree.sum_path(tree)


#                1
#              /   \
#             2     3
#            /  \  /  \
#           4    5 6   7
#                 \     \
#                  8     9
if __name__ == "__main__":
    build_tree()
