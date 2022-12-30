from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.adjacency = defaultdict(list)

    def create_graph(self, grid):
        for src, des in grid:
            self.adjacency[src].append(des)
            self.adjacency[des].append(src)

    def print_graph(self):
        for node in self.adjacency:
            print(f'{node} -> {self.adjacency[node]}')

    # DFS recursive
    def DFS_recursive(self, start):
        visited = set()
        res = []
        self.helper(start, visited, res)
        # return " ".join(res)
        print(res)

    def helper(self, node, visited, res) -> None:
        visited.add(node)
        res.append(node)
        for neighbor in self.adjacency[node]:
            if neighbor not in visited:
                self.helper(neighbor, visited, res)

    # DFS iterative
    def DFS_iterative(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            print(node, end=" ")
            for neighbor in self.adjacency[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


board = [
    [0, 1],
    [1, 2],
    [2, 0]
]

# grid = [['A', 'B'], ['A', 'D'],
#         ['B', 'F'], ['B', 'G'],
#         ['C', 'F'], ['C', 'E'],
#         ['D', 'C'], ['D', 'E']
#         ]

grid = [['A', 'B'], ['A', 'E'],
        ['B', 'C'], ['B', 'D'],
        ]

g = Graph()
g.create_graph(grid)
g.create_graph(board)
# g.print_graph()
print("DFS iterative: ", end=" ")
g.DFS_iterative('A')
print()
g.DFS_iterative(0)
print("\n-------------------------------")
print("DFS recursive: ", end=" ")
g.DFS_recursive('A')
g.DFS_recursive(0)
