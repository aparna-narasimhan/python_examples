#kth to last element in linked list

#3->1->4->5->2
#k=2 = print 5

count=0
def find_kth_to_last(head, k,c=0):
    global count
    if(head==None):
        return
    if c==0:
        count=0
    find_kth_to_last(head.next,k,c)
    count+=1
    c+=1
    if(count==k):
        print(head.data)

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

head=Node(3)
head.next=Node(1)
head.next.next=Node(4)
head.next.next.next=Node(5)
head.next.next.next.next=Node(2)
find_kth_to_last(head,2)
find_kth_to_last(head,3)
find_kth_to_last(head,4)