# program to check if there is exist a path between two vertices
# of a graph

from collections import defaultdict

#This class represents a directed graph using adjacency list representation
class Graph:

    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

     # Use BFS to check path between s and d
    def isReachable(self, s, d):

        # Store all paths
        paths=[]

        # Create a queue for BFS and enqueue the source node
        path=[[s]]

        while path:

            #Dequeue a vertex from queue
            x = path.pop(0)
            j = x[-1]

            # If this adjacent node is the destination node,
            # then return true
            if j == d:
               paths.append(x)

            #  Else, continue to do BFS
            for i in self.graph[j]:
                if i not in x:
                    path.append(x+[i])

         # If BFS is complete without visited d
        print(paths)

# Create a graph given in the above diagram
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

u =1; v = 3

g.isReachable(2, 3)