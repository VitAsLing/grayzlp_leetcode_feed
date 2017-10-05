"""
https://leetcode.com/problems/sudoku-solver/description/

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.

"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    for c in "123456789":
                        if self.isValid(board, i, j, c):
                            board[i][j] = c

                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, column, c):
        for i in range(0, 9):
            if board[row][i] == c:
                return False
            if board[i][column] == c:
                return False
            if board[(row / 3) * 3 + i / 3][(column / 3) * 3 + i % 3] == c:
                return False
        return True


# Test code
n = ["978654321",
     ".........",
     ".........",
     ".........",
     ".........",
     ".........",
     ".........",
     ".........",
     "........."]

board = []
for str in n:
    board.append(list(str))

Solution().solve(board)
print board



