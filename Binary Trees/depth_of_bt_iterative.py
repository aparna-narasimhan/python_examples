# Definition for a binary tree node.
class Node(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    depth = 0
    currLevel = [root]

    while currLevel:
        depth += 1
        nextLevel = []
        for node in currLevel:
            if node.left:
                nextLevel.append( node.left )
            if node.right:
                nextLevel.append( node.right )

        currLevel = nextLevel

    return depth

# Let us construct the BST shown in the figure
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
print(levelOrder(root))