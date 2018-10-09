from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(dict)
        
    def add_edge_with_weights(self, u, v, w):
        self.graph[u][v]=w
        
    def print_graph(self):
        print(self.graph[0][2])
        
    
g = Graph(7)
g.add_edge_with_weights(0,1,10)
g.add_edge_with_weights(0,2,3)
g.add_edge_with_weights(0,3,2)
g.add_edge_with_weights(1,3,7)
g.add_edge_with_weights(2,3,6)
g.print_graph()