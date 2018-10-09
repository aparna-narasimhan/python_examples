from collections import defaultdict
class Sample:
    def __init__(self, binaryMatrix):
        self.num_rows = len(binaryMatrix)
        self.num_cols = len(binaryMatrix[0])
        self.binaryMatrix = binaryMatrix
        self.visited = defaultdict(bool)

    def get_number_of_islands(self):
      count = 0
      for row in range(self.num_rows):
        for col in range(self.num_cols):
          if not self.visited[(row,col)] and self.binaryMatrix[row][col] == 1:
            self.visited[(row,col)] = True
            if not self.adj_ones_visited(row,col):
                count += 1
      return(count)

    def adj_ones_visited(self, row, col):
          #Check the next element is 1 and visited
          if col < self.num_cols-1 and self.binaryMatrix[row][col+1] == 1:
              if self.visited[(row,col+1)]:
                return(True)
          self. visited[(row,col+1)] = True

          #Check the prev element is 1 and visited
          if col > 0 and self.binaryMatrix[row][col-1] == 1:
              if self.visited[(row,col-1)]:
                return(True)
          self. visited[(row,col-1)] = True

          #Check the down element is 1 and visited
          if row < self.num_rows-1 and self.binaryMatrix[row+1][col] == 1:
              if self. visited[(row+1,col)]:
                return(True)
          self.visited[(row+1,col)] = True

          #Check the top element is 1and visited
          if row > 0 and self.binaryMatrix[row-1][col] == 1:
              if self.visited[(row-1,col)]:
                return(True)
          self.visited[(row-1,col)] = True

          return(False)

binaryMatrix = [ [0,    0,    0,    0,    0],
                 [0,    0,    0,    1,    0],
                 [0,    0,    1,    0,    0],
                 [0,    0,    0,    0,    0],
                 [0,    0,    0,    0,    0] ]
s = Sample(binaryMatrix)
print(s.get_number_of_islands())