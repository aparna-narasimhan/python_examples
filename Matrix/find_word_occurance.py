class Solution:
  def find_word_count(self,matrix, word):
      self.matrix = matrix
      self.word = word
      if len(matrix) == 0:
          return 0
      self.row_len = len(matrix)
      self.col_len = len(matrix[0])
      count = 0
      for row in range(self.row_len):
          for col in range(self.col_len):
              if self.matrix[row][col] == word[0]:
                  rem_row_len = self.col_len - col
                  rem_col_len = self.row_len - row
                  if rem_row_len >= len(word):
                      if self.row_matches(row, col):
                          count += 1
                  if rem_col_len >= len(word):
                      if self.col_matches(row, col):
                          count += 1
      return(count)

  def row_matches(self,row, col):
      i = -1
      for c in range(col, self.col_len):
          i += 1
          if i < len(self.word):
           if self.matrix[row][c] != self.word[i]:
              return(False)
      return(True)

  def col_matches(self,row, col):
      i = -1
      for r in range(row, self.row_len):
          i += 1
          if i < len(self.word):
           if self.matrix[r][col] != self.word[i]:
              return(False)
      return(True)

m = [ ['S','F','O','P'],
      ['F','I','V','E'],
      ['O','V','E','C'],
      ['A','E','R','M']
    ]
s = Solution()
print(s.find_word_count(m, 'FIVE'))