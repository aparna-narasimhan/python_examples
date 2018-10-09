sum=0
count=0
def find_sum_of_kth_largest(root,k):
  if(root == None):
    return
  global count
  global sum
  find_sum_of_kth_largest(root.right,k)
  count += 1
  #print(root.data)
  if(count<=3):
   sum = sum + root.data
  find_sum_of_kth_largest(root.left,k)
  return(sum)

class Node:
  def __init__(self,data):
    self.data = data
    self.left=None
    self.right=None

root = Node(8)
root.left = Node(7)
root.right = Node(10)
root.left.left = Node(2)
root.right.left = Node(9)
root.right.right = Node(13)
sum = find_sum_of_kth_largest(root, 3)
print(sum)