import pdb
def find_path(graph, start, end, path=[]):
        #pdb.set_trace()
        path = path + [start]
        if start == end:
            return path
        if start not in graph.keys():
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None
        
def find_all_paths(graph, start, end, path=[]):
        #pdb.set_trace()
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
        
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
        
def main():
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
    
    path = find_path(graph, 'A', 'D')
    print 'path:: %s' %path
    all_paths = find_all_paths(graph, 'A', 'D')
    print 'all paths::%s' %all_paths
    s_path=find_shortest_path(graph, 'A', 'D')
    print 'shortest path::%s' %s_path
    
main()