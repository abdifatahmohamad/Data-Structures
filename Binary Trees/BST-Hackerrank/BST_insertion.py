# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    def __str__(self):
        return str(self.val)


class Binary_search_tree:
    def __init__(self):
        self.root = None

    def create_node(self, data) -> Node:
        return Node(data)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            return

        root = self.root
        while True:
            if data < root.val:
                if root.left is None:
                    # Left side is None, create new node and assign to root.left side
                    root.left = Node(data)
                    # Since we inserted the node, we break out of the loop
                    break
                else:
                    # Left side is not None, keep traverse (go till last node)
                    root = root.left

            if data > root.val:
                if root.right is None:
                    # Right side is None, create new node and assign to root.right side
                    root.right = Node(data)
                    break
                else:
                    # Right side is not None, keep traverse (go till last node)
                    root = root.right

        return root

    def preorder_traversal(self, root):
        if not root:
            return

        print(root.val, end=" ")
        self.preorder_traversal(root.left)

        self.preorder_traversal(root.right)


if __name__ == "__main__":
    tree = Binary_search_tree()
    root = tree.create_node(4)
    tree.insert(2)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    tree.insert(6)

    '''     
                 4
               /   \
              2     7
             / \   /
            1   3 6
        [4, 2, 1, 3, 7, 6] for in order traversal

    '''
    tree.preorder_traversal(root)
