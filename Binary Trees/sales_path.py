'''
Sales Path
The car manufacturer Honda holds their distribution system in the form of a tree (not necessarily binary). The root is the company itself, and every node in the tree represents a car distributor that receives cars from the parent node and ships them to its children nodes. The leaf nodes are car dealerships that sell cars direct to consumers. In addition, every node holds an integer that is the cost of shipping a car to it.

Take for example the tree below:

alt

A path from Honda’s factory to a car dealership, which is a path from the root to a leaf in the tree, is called a Sales Path. The cost of a Sales Path is the sum of the costs for every node in the path. For example, in the tree above one Sales Path is 0→3→0→10, and its cost is 13 (0+3+0+10).

Honda wishes to find the minimal Sales Path cost in its distribution tree. Given a node rootNode, write a function getCheapestCost that calculates the minimal Sales Path cost in the tree.

Implement your function in the most efficient manner and analyze its time and space complexities.

For example:

Given the rootNode of the tree in diagram above

Your function would return:

7 since it’s the minimal Sales Path cost (there are actually two Sales Paths in the tree whose cost is 7: 0→6→1 and 0→3→2→1→1)
'''
import sys
def get_cheapest_cost(rootNode, cost = 0, min_cost = float("inf")):
  if rootNode is None:
    return 0
  if not rootNode.children:
    return cost
  cost += rootNode.cost
  if rootNode and len(rootNode.children) > 0:
    for child in self.children:
      price = get_cheapest_cost(child, cost, min_cost)
      cost = 0
      if price > min_cost:
        min_cost = price
  return min_cost

  '''
  Iterative approach
  stack = [(rootNode, rootNode.cost)]
  res = sys.maxint
  while stack:
    node, cost = stack.pop()
    if not node.children:
        res = min(res, cost)
    else:
      for c in node.children():
        stack.append((c, c.cost + cost))
  return res
  '''



##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
