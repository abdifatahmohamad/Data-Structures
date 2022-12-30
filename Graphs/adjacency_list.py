from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.adjacency = defaultdict(list)

    # Directional graph
    def directional_graph(self, grid):
        for src, des in grid:
            self.adjacency[src].append(des)

    # Bidirectional graph
    def bidirectional_graph(self, grid):
        for src, des in grid:
            self.adjacency[src].append(des)
            self.adjacency[des].append(src)

    def print_graph(self) -> None:
        for node in self.adjacency:
            print(f'{node} -> {self.adjacency[node]}')


courses = [['cs102', 'cs301'], ['cs301', 'cs101'], ['cs301', 'cs406']]

'''
    Bidirectional Graph --> arrows coming from both ways
    Directional Graph --> arrows going/coming form one way

'''

g = Graph()
g.bidirectional_graph(courses)
g.directional_graph(courses)
print("Bidirectional graph: ", end=" ")
g.bidirectional_graph('cs102')
print("\n---------------------------")
print("Directional Graph: ", end=" ")
g.directional_graph('cs102')
