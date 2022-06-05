class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class TreeNode:
    def preOrder(self, root):
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(str(node.val) + " ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print("".join(res))


tree = Node(1)
tree.right = Node(2)
tree.right.right = Node(5)
tree.right.right.left = Node(3)
tree.right.right.right = Node(6)
tree.right.right.left.right = Node(4)

TreeNode().preOrder(tree)
