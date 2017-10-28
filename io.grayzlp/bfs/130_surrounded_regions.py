"""
https://leetcode.com/problems/surrounded-regions/description/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if not row:
            return
        col = len(board[0])

        for i in range(0, row):
            self.check(board, i, 0, row, col)
            if col > 1:
                self.check(board, i, col - 1, row, col)
        for j in range(1, col - 1):
            self.check(board, 0, j, row, col)
            if row > 1:
                self.check(board, row - 1, j, row, col)
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == '1':
                    board[i][j] = 'O'

    def check(self, board, i, j, row, col):
        if board[i][j] == 'O':
            board[i][j] = '1'
            if i > 0:
                self.check(board, i - 1, j, row, col)
            if i < row - 1:
                self.check(board, i + 1, j, row, col)
            if j > 0:
                self.check(board, i, j - 1, row, col)
            if j < col - 1:
                self.check(board, i, j + 1, row, col)


# Test code
board = [['X', 'X', 'X'],
         ['X', 'O', 'X'],
         ['X', 'O', 'X']]
Solution().solve(board)
print board
