from collections import defaultdict
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_min_num_edges(self,start,end,path=[]):
        path = path + [start]
        if(start == end):
            return path
        if start not in self.graph.keys():
            return None
        shortest = None
        shortest_len = 0
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_min_num_edges(node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path

        return(shortest)


g = Graph(7)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(0,4)
g.add_edge(1,0)
g.add_edge(1,2)
g.add_edge(2,0)
g.add_edge(2,1)
g.add_edge(2,5)
g.add_edge(3,4)
g.add_edge(4,0)
g.add_edge(4,3)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(5,2)
g.add_edge(5,4)

shortest_path = g.find_min_num_edges(1,5)
print(len(shortest_path)-1)