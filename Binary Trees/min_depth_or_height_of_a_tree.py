# Python program to find the maximum depth of tree

# A binary tree node
# NOTE: Here, height is min number of nodes at the longest path. If height is min number of edges in the longest path, then just return lDepth or rDepth whichever is smaller.
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Compute the "minDepth" of a tree -- the number of nodes
# along the shortest path from the root node down to the
# farthest leaf node
def minDepth(node):
    if node is None:
        return 0 ;

    else :

        # Compute the depth of each subtree
        lDepth = minDepth(node.left)
        rDepth = minDepth(node.right)

        # Use the smaller one
        if (lDepth < rDepth):
            return lDepth+1
        else:
            return rDepth+1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print "Height of tree is %d" %(minDepth(root))

