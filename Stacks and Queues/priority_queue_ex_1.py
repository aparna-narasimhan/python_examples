import queue as Q
q = Q.PriorityQueue()
q.put(10)
q.put(1)
q.put(5)
while(not q.empty()):
    print(q.get())

q = Q.PriorityQueue()
q.put((10,'ten'))
q.put((1,'one'))
q.put((5,'five'))
while not q.empty():
    print q.get(),