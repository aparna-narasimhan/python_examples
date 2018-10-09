class Node:
  def __init__(self,val):
    self.val = val
    self.left=None
    self.right=None

def kthSmallestElement(root, k, counter):
    if root is None:
        return None
    lres = kthSmallestElement(root.left, k, counter)

    counter[0] = counter[0] +1
    if counter[0] == k: return root

    rres = kthSmallestElement(root.right, k, counter)

    return lres if lres else rres

def kthSmallest(root, k):
    counter=[0]
    res = kthSmallestElement(root, k, counter)
    return res.val

root = Node(8)
root.left = Node(7)
root.right = Node(10)
root.left.left = Node(2)
root.right.left = Node(9)
root.right.right = Node(13)
print(kthSmallest(root, 4))
print(kthSmallest(root, 2))