import pdb
start_end_same = 0
class graphs( object ):
    def __init__( self, graph, path_weight=0, shortest=None, weight={} ):
        self.path_weight = path_weight
        self.shortest = shortest
        self.weight = weight
        if( graph ):
            self.graph = graph
        else:
            self.graph = {}
            
    def find_path(self, start, end, path=[]):
        path = path + [start]
        if( start == end ):
            return path
        if( start not in self.graph.keys() ):
            return None
        for node in self.graph[start]:
            if( node not in path ):
                new_path = self.find_path(node,end,path)
                if( new_path ):
                    return new_path
        return None
        
    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if( start == end ):
            return [path]
        if( start not in self.graph.keys() ):
            return []
        paths = []
        for node in self.graph[start]:
            if( node not in path ):
                new_paths = self.find_all_paths(node,end,path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
        
    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if( start == end ):
            start_end_same = 1
            return path
        if( start not in self.graph.keys() ):
            return None
        shortest = None
        for node in self.graph[start]:
            if( node not in path ):
                new_path = self.find_shortest_path(node,end,path)
                if( new_path ):
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest
        
    def find_shortest_path_with_weights(self, start, end, path=[]):
        global start_end_same    
        path = path + [start]
        pdb.set_trace()
        if( start_end_same ):
            self.path_weight = 0
            start_end_same = 0
        if( start == end ):
            start_end_same = 1
            return path
        if( start not in self.graph.keys() ):
            return None
       
        for node in self.graph[start]:
            if( node not in path ):
                self.path_weight = self.path_weight + self.graph[start][node]
                new_path = self.find_shortest_path_with_weights(node,end,path)
            if( new_path ):
                self.weight[tuple(new_path)] = self.path_weight
                if not self.shortest or self.weight[tuple(new_path)] < self.weight[tuple(self.shortest)]:
                    self.shortest = new_path
        return self.shortest
        
def main():
    graph = {
            'A': ['B','C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']            
            }
            
    graph_with_weights = {'A': {'B':3, 'C':3},
     'B': {'C':2, 'D':2},
     'C': {'D':1},
     'D': {'C':3},
     'E': {'F':8},
     'F': {'C':2}}
     
    ob = graphs(graph)
    #pdb.set_trace()
    ret_path = ob.find_path('A','D')
    print 'find_path:: %s' %ret_path
    
    all_paths = ob.find_all_paths('A','C')
    print 'find_all_path:: %s' %all_paths
    
    shortest_path = ob.find_shortest_path('A','C')
    print 'find_s_path:: %s' %shortest_path
    
    ob_w_weights = graphs(graph_with_weights)
    s_path = ob_w_weights.find_shortest_path_with_weights('A','D')
    print 'shortest path with least weight:: %s' %s_path
    
main()
        
    
        
