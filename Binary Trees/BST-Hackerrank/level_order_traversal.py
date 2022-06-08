import collections

# https://www.youtube.com/watch?v=568Jr8Fs6jQ&list=PLPdtS77PaSutvrLxZJT5gmASGSed0dO_T&index=10


class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class TreeNode:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(data)
                        break
                if data > curr.val:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(data)
                        break

    def level_order(self, root):
        queue = collections.deque()
        queue.append(root)
        while len(queue) != 0:
            root = queue.popleft()
            print(root.val, end=" ")

            if root.left:
                queue.append(root.left)

            if root.right:
                queue.append(root.right)

    '''
             5
            / \
           3   9
          / \ /  \
         2  4 7   10
                        
                        
        [5, 3, 9, 2, 4, 7, 10] for level order BFS

    '''


tree = Node(5)
tree.left = Node(3)
tree.right = Node(9)
tree.left.left = Node(2)
tree.left.right = Node(4)
tree.right.left = Node(7)
tree.right.right = Node(10)


TreeNode().level_order(tree)
