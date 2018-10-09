'''
Sort elements of a linked list
Approach:
If element is greater than the next one, swap.
Repeat until all elements are in sorted order
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def sort_linked_list(head):
    
    #print(curr.data)
    #print(curr.next.data)
    swapped = True
    while swapped:
        swapped = False
        curr = head
        while curr != None and curr.next != None:
          if curr.data > curr.next.data:
            temp = curr.next.data
            curr.next.data = curr.data
            curr.data = temp
            swapped = True
          curr = curr.next    
    while head != None:
        print(head.data)
        head = head.next
        
head = Node(5)
#print(head.data)
head.next = Node(2)
#print(head.next.data)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(1)
sort_linked_list(head)
