graph=  [#a,b,c,d,e,f,g,h,i,j
     [0,1,1,1,1,0,0,0,0,0],  #a
     [1,0,0,1,0,0,1,0,0,0],  #b
     [1,0,0,1,0,0,0,0,0,0],  #c
     [1,1,1,0,0,0,0,1,0,0],  #d
     [1,0,0,0,0,1,0,1,1,0],  #e
     [0,0,0,0,1,0,0,1,1,0],  #f
     [0,1,0,0,0,0,0,1,1,1],  #g
     [0,0,0,1,1,1,1,0,1,0],  #h
     [0,0,0,0,1,1,1,1,0,1],  #i
     [0,0,0,0,0,0,1,0,1,0],  #j
    ]

def find_path(graph, start, end, path=[],nodes='ABCDEFGHIJ'):
        path = path + [start]
        #print(path)
        if start == end:
            return [path]
        paths = []
        for i in range(len(nodes)):
            if graph[nodes.index(start)][i] and nodes[i] not in path:
                newpath = find_path(graph, nodes[i], end, path, nodes)
                if newpath:
                    paths.append(newpath)
        return paths

path = find_path(graph, 'A', 'D')
print(path)