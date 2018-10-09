class Solution:
    rep_list=[]
    def isValidNum(self, val):
        if val is not '.' and int(val) not in range(1,10):
            return False

    def isNum(self, val):
        if int(val) not in range(1,10):
            return False

    def isNotRepeated(self, val):
        if int(val) in rep_list:
            return False
        else:
            rep_list.append(int(val))
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for row in range(0,10):
            for col in range(0,10):
                if not isValidNum(board[row][col]):
                    return False

        for row in range(0,10):
            for col in range(0,10):
                if isValidNum and not isNotRepeated(board[row][col]):
                    return False
            rep_list.clear()

        rep_list.clear()
        for row in range(0,10):
            for col in range(0,10):
                if isValidNum and not isNotRepeated(board[col][row]):
                    return False
            rep_list.clear()