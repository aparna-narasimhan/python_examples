#Heap Sort
import heapq
def heap_sort( nums ):
    heap = []
    for num in nums:
        heapq.heappush( heap, num )
    return [ heapq.heappop( heap ) for i in range( len( heap ) ) ]

#Assertion Error when the output is different
assert heap_sort( [ 5,4,3,2,1 ] ) == [ 1,2,3,4,5 ]
result = heap_sort( [ 5,4,3,2,1 ] )
print(result)