'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Eg: For a 7 x 3 grid. How many possible unique paths are there?
'''
def uniquePaths(m, n): #m=4, n=4
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    #Initialize a matrix of m rows and n cols to 0
    grid = [[0] * n] * m

    #Set the 1st row and 1st col values to 1 as there is only 1 way to reach those elements
    for row in range(m):
        grid[row][0] = 1

    for col in range(n):
        grid[0][col] = 1

    #Each cell can either be reached from its top element([row-1][col]) or left element([row][col-1]), so add up the # of ways it can be reached by adding up the top and left element values
    for row in range(1,m):
        for col in range(1,n
            grid[row][col] = grid[row-1][col] + grid[row][col-1]

    #Get the #of ways the last element can be reached
    print(grid[m-1][n-1])

uniquePaths(4,4)