class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        firstRowHasZero = False
        firstColHasZero = False
        if len(matrix)==0 or len(matrix[0]) == 0:
            return
        for col in range(0,len(matrix[0])):
            if matrix[0][col]==0:
                firstRowHasZero = True
                break
        for row in range(0, len(matrix)):
            if matrix[row][0]==0:
                firstColHasZero = True
                break

        for row in range(1, len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for row in range(1, len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if firstRowHasZero:
            for col in range(0,len(matrix[0])):
                matrix[0][col] = 0

        if firstColHasZero:
            for row in range(0, len(matrix)):
                matrix[row][0] = 0