"""
https://leetcode.com/problems/n-queens/description/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a
queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.backtracking(res, [], n)
        return res

    def backtracking(self, res, temp, n):
        row = len(temp)
        if row == n:
            res.append(list(temp))
        else:
            for i in range(0, n):
                if not self.is_valid(temp, row, i, n):
                    continue
                else:
                    new_line = '.' * i + 'Q' + '.' * (n - 1 - i)
                    temp.append(new_line)
                    self.backtracking(res, temp, n)
                    temp.pop()

    def is_valid(self, temp, row, column, n):
        for i in range(0, row):
            if temp[i][column] == 'Q':
                return False
        i = 1
        while row - i >= 0 and column - i >= 0:
            if temp[row - i][column - i] == 'Q':
                return False
            i += 1
        i = 1
        while row - i >= 0 and column + i < n:
            if temp[row - i][column + i] == 'Q':
                return False
            i += 1
        return True


# Test code
print Solution().solveNQueens(8)
