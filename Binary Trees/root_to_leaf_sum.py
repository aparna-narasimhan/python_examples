class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

def root_to_leaf_sum(root, num,sum=0):
  global found
  if sum == 0:
      found = False
  if root == None:
      return
  sum += root.val
  print(sum)
  if root.left is None and root.right is None and sum == num:
      found = True
  root_to_leaf_sum(root.left, num,sum)
  root_to_leaf_sum(root.right, num,sum)
  sum -= root.val

root = Node(10)
root.left = Node(8)
root.left.left = Node(3)
root.left.right = Node(5)
root.right = Node(2)
root.right.left = Node(2)
root_to_leaf_sum(root,23)
print(found)
root_to_leaf_sum(root,21)
print(found)