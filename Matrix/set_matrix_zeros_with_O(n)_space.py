#Leetcode problem

from collections import defaultdict
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #Option1: 1.Use a dictionary with keys as rows and columns
                 #2. iterate through the matrix and add the row and col of the element which is 0(if not added already.
                  #3. Reset all the elements in corresponding row and col to 0

        #matrix_dict = {'rows': [], 'cols': []}
        if len(matrix)==0 or len(matrix[0]) == 0:
            return
        matrix_dict = defaultdict(list)
        row_len = len(matrix)
        col_len = len(matrix[0])
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    if row not in matrix_dict['rows']:
                        matrix_dict['rows'].append(row)
                    if col not in matrix_dict['cols']:
                        matrix_dict['cols'].append(col)

        for row in matrix_dict['rows']:
            for col in range(col_len):
                matrix[row][col] = 0

        for col in matrix_dict['cols']:
            for row in range(row_len):
                matrix[row][col] = 0

