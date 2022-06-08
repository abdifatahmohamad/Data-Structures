import collections


# https://www.youtube.com/watch?v=fAAZixBzIAI
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

    # def __repr__(self):
    #     return str(self.val)


def dfs_iter(root):
    if not root:
        return []
    stack, res = [root], []
    while stack:
        curr = stack.pop()
        res.append(curr.val)

        if curr.right:
            stack.append(curr.right)

        if curr.left:
            stack.append(curr.left)

    return res


def dfs_rec(root):
    if not root:
        return []

    left_values = dfs_rec(root.left)
    right_values = dfs_rec(root.right)
    return [*root.val, *left_values, *right_values]


def bfs(root):
    if not root:
        return []

    queue = collections.deque([root])
    res = []
    while queue:
        # size = len(queue)
        # for _ in range(size):
        node = queue.popleft()
        res.append(node.val)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return res


def tree_includes_dfs_rec(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    return tree_includes_dfs_rec(root.left, target) \
        or tree_includes_dfs_rec(root.right, target)


def tree_includes_dfs_iter(root, target):
    if not root:
        return False

    stack = [root]
    while stack:
        curr = stack.pop()

        if curr.val == target:
            return True

        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)

    return False


def tree_includes_bfs(root, target):
    if not root:
        return False

    queue = collections.deque([root])
    while queue:
        curr = queue.popleft()
        if curr.val == target:
            return True

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

    return False


def tree_sum_dfs_rec(root):
    if not root:
        return 0

    return root.val + tree_sum_dfs_rec(root.left) \
        + tree_sum_dfs_rec(root.right)


def tree_sum_dfs_iter(root):
    if not root:
        return 0

    stack, res = [root], 0
    while stack:
        curr = stack.pop()

        res += curr.val

        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)
    return res


def tree_sum_bfs(root):
    if not root:
        return 0

    queue = collections.deque([root])
    res = 0
    while queue:
        curr = queue.popleft()
        res += curr.val

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)
    return res


def tree_min_value_dfs_rec(root):
    if not root:
        return float("Inf")

    left_min = tree_min_value_dfs_rec(root.left)
    right_min = tree_min_value_dfs_rec(root.right)
    return min(root.val, left_min, right_min)


def tree_min_value_dfs_iter(root):
    if not root:
        return float("Inf")

    minimum = float("Inf")
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.val < minimum:
            minimum = curr.val

        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)
    return minimum


def tree_min_value_bfs(root):
    if not root:
        return float("Inf")

    minimum = float("Inf")
    queue = collections.deque([root])
    while queue:
        curr = queue.pop()
        if curr.val < minimum:
            minimum = curr.val

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)
    return minimum


tree = Node("a")
tree.left = Node("b")
tree.right = Node("c")
tree.left.left = Node("d")
tree.left.right = Node("e")
tree.right.right = Node("f")

# print(bfs(tree)) # ['a', 'b', 'c', 'd', 'e', 'f']

# print(dfs_iter(tree))  # ['a', 'b', 'd', 'e', 'c', 'f']
# print(dfs_rec(tree)) # ['a', 'b', 'd', 'e', 'c', 'f']

# print(tree_includes_bfs(tree, "y")) # False

# print(tree_includes_dfs_rec(tree, "e")) # True

# print(tree_includes_dfs_iter(tree, "j")) # False

tree = Node(3)
tree.left = Node(11)
tree.right = Node(4)
tree.left.left = Node(4)
tree.left.right = Node(2)
tree.right.right = Node(1)

'''
        3
       /  \
      11   4
     /  \   \
    4    2   1
'''

# print(tree_includes_dfs_rec(tree))
# print(tree_includes_dfs_iter(tree))
# print(tree_sum_bfs(tree)) # 25
# print(tree_sum_dfs_rec(tree)) # 25
# print(tree_sum_dfs_iter(tree)) # 25

# print(tree_min_value_dfs_iter(tree))
print(tree_min_value_dfs_rec(tree))
# print(tree_min_value_bfs(tree))

# a = Node("a")
# b = Node("b")
# c = Node("c")
# d = Node("d")
# e = Node("e")
# f = Node("f")
#
# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.right = f

# a.bfs(a)
