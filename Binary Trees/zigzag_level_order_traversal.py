class Solution(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        ret = []
        currLevel = [root]
        lvl = 0

        while currLevel:
            lvl += 1
            temp = [ node.val for node in currLevel ]
            if lvl % 2 == 0:
                ret.append(temp)
            else:
                ret.append( temp[::-1] )

            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append( node.left )
                if node.right:
                    nextLevel.append( node.right )

            currLevel = nextLevel

        return (sum(ret,[]))

root = Solution(10)
root.left = Solution(8)
root.right = Solution(12)
root.left.left = Solution(6)
root.left.right = Solution(9)
root.right.left = Solution(11)
root.right.right = Solution(14)
print(root.levelOrder(root))