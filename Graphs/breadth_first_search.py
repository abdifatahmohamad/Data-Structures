from collections import defaultdict, deque


class Graph:
    def __init__(self) -> None:
        self.adjacency = defaultdict(list)

    def create_graph(self, grid):
        for src, des in grid:
            self.adjacency[src].append(des)
            self.adjacency[des].append(src)

    def print_graph(self) -> None:
        for node in self.adjacency:
            print(f'{node} -> {self.adjacency[node]}')

    # Print using string representation
    # def __str__(self):
    #     return str(self.__dict__)

    def BFS(self, start):
        visited = {start}
        queue = deque([start])
        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.adjacency[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


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
g.create_graph(board)
g.create_graph(grid)
print("BFS: ", end=" ")
g.BFS('A')
print("\n---------------------------")
print("BFS: ", end=" ")
g.BFS(0)

