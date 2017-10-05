"""
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.

"""

SET = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isVerticalValid(board) and self.isHorizontalValid(board) and self.isSquareValid(board)

    def isVerticalValid(self, board):
        for row in board:
            l_set = set(SET)
            for str in row:
                if str in l_set:
                    l_set.remove(str)
                else:
                    if str == '.':
                        continue
                    else:
                        return False
        return True

    def isHorizontalValid(self, board):
        for i in range(0, 9):
            l_set = set(SET)
            for j in range(0, 9):
                str = board[j][i]
                if str in l_set:
                    l_set.remove(str)
                else:
                    if str == '.':
                        continue
                    else:
                        return False
        return True

    def isSquareValid(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                l_set = set(SET)
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        str = board[m][n]
                        if str in l_set:
                            l_set.remove(str)
                        else:
                            if str == '.':
                                continue
                            else:
                                return False
        return True


# Test code
print Solution().isValidSudoku(
    ["..4...63.",
     ".4.......",
     "5......9.",
     "...26....",
     "4.3.....1",
     "...7.....",
     "...5.....",
     ".........",
     "........."])
