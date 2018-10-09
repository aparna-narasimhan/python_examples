class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def search(self, data):
        pos = -1
        temp=self.head
        while(temp is not None and temp.data is not data):
            pos+=1
            temp=temp.next
        if(temp):
            print("Element found at position {}".format(pos+1))
        else:
            print("Element not found in the list")

    def remove(self, data):
        if(self.head.data == data):
            self.head = self.head.next
            return
        temp = self.head
        while(temp and temp.next and temp.next.data != data):
            temp=temp.next
        if(temp and temp.next):
            temp.next = temp.next.next
        else:
            print("Item not found")

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp=temp.next

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.print_list()
l.search(3)
l.remove(10)
l.print_list()