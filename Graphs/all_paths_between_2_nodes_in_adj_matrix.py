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
nodes='ABCDEFGHIJ'
a='F'
b='C'
p=[[a]]
paths=[]
while p:                          # evaluates to true if p not empty
    x = p.pop(0)
    j = nodes.index(x[-1])        # use [-1] to get last element
    if nodes[j] == b:             # by moving this check out of the loop...
        #print("Path found:", x)    # (don't forget to print the path)
        paths.append(x)
                        # ...you can use break and don't need flag
    for i, e in enumerate(nodes): # enumerate gives (index, element)
        if graph[j][i] and e not in x: # a bit more concise
            p.append(x + [e])     # this way, we don't need temp at all
            #print(p)
print(paths)