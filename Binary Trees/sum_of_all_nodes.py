class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

total = 0
def sum_of_all_nodes(root):
    global total
    if root is None:
        return
    total += root.val
    sum_of_all_nodes(root.left)
    sum_of_all_nodes(root.right)
    return total

root = Node(10)
root.left = Node(8)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(2)
root.right.left = Node(1)

print(sum_of_all_nodes(root))
total = 0
print(sum_of_all_nodes(root))