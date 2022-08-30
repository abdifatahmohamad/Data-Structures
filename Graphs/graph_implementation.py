# Implementing Undirected, Unweighted cyclic Graph using Python class:
# Here is the Graph: https://visualgo.net/en/graphds

class Graph:
    def __init__(self, name=None):
        self.numberOfNodes = 0
        self.adjacentList = {}
        self.children = []
        self.name = name

    def __str__(self):
        return str(self.__dict__)

    def add_child(self, name=None):
        self.children.append(Graph(name))

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def dfs(self, arr):
        arr.append(self.name)
        for child in self.children:
            child.dfs(arr)
        return arr

    def showConnections(self):
        for x in self.adjacentList:
            print(x, end=' --> ')
            for i in self.adjacentList[x]:
                print(i, end=' ')
            print()

myGraph = Graph()
# myGraph.addVertex('0')
# myGraph.addVertex('1')
# myGraph.addVertex('2')
# myGraph.addVertex('3')
# myGraph.addVertex('4')
# myGraph.addVertex('5')
# myGraph.addVertex('6')
#
# myGraph.addEdge('3', '1')
# myGraph.addEdge('3', '4')
# myGraph.addEdge('4', '2')
# myGraph.addEdge('4', '5')
# myGraph.addEdge('1', '2')
# myGraph.addEdge('1', '0')
# myGraph.addEdge('0', '2')
# myGraph.addEdge('6', '5')

# myGraph.add_child("A")
arr =["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
print(myGraph.dfs(arr))
# print(myGraph)
myGraph.showConnections()


'''
            A
         /  |  \
        B   C   D
      /  \     /  \
     E    F   G    H
         /  \  \
        I    J  K

'''
