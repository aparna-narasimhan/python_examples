


Desktop Preview



Portrait Phone Preview




Landscape Phone Preview




Portrait Pad Preview




Landscape Pad Preview






Coding Ground
Execute Python Online (Python v2.7.13)

 Login   Setting  Edit  Project  Fork





Result






$python main.py
2














main.py
STDIN


Loading...
  Execute  | Share


  
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47









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

            return len(path) - 1

        if start not in self.graph.keys():

            return 0

        #shortest = None

        shortest_len = 0

        for node in self.graph[start]:

            if node not in path:

                new_path = self.find_min_num_edges(node, end, path)

                if new_path:

                    if not shortest_len or new_path < shortest_len:

                        shortest_len = new_path



        return(shortest_len)





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

print(shortest_path)




































































































































































































































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
            return len(path) - 1
        if start not in self.graph.keys():
            return 0
        shortest_len = 0
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_min_num_edges(node, end, path)
                if new_path:
                    if not shortest_len or new_path < shortest_len:
                        shortest_len = new_path

        return(shortest_len)


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
print(shortest_path)




























