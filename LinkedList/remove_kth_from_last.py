count=0
def remove_kth_to_last(head, k,c=0):
    global count
    if(head==None):
        return
    if c==0:
        count=0
    remove_kth_to_last(head.next,k,c)
    count+=1
    c+=1
	#If the element to remove is the last element, just point this node to next node
    if(k == 1 and count == k + 1):
        head.next = head.next.next
	#else assign the next node's data to current node and then delete the current node
	#we do this because, the previous method will not work if element to be deleted is the head
    elif(k != 1 and count == k):
        head.data = head.next.data
        head.next = head.next.next

def print_list(head):
    while head:
        print(head.data)
        head = head.next

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

head=Node(3)
head.next=Node(1)
head.next.next=Node(4)
head.next.next.next=Node(5)
head.next.next.next.next=Node(2)

remove_kth_to_last(head,5)
print_list(head)