"""
https://leetcode.com/problems/spiral-matrix/description/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        self.helper(matrix, res, 0)
        return res

    def helper(self, matrix, res, level):
        row = len(matrix)
        if row == 0:
            return
        col = len(matrix[0])
        left_row = row - level * 2
        left_col = col - level * 2
        if left_row <= 0 or left_col <= 0:
            return
        if left_row == 1:
            for i in range(0, left_col):
                res.append(matrix[level][level + i])
            return
        if left_col == 1:
            for i in range(0, left_row):
                res.append(matrix[level + i][level])
            return
        else:
            for i in range(0, left_col):
                res.append(matrix[level][level + i])
            for i in range(1, left_row - 1):
                res.append(matrix[level + i][level + left_col - 1])
            for i in reversed(range(0, left_col)):
                res.append(matrix[level + left_row - 1][level + i])
            for i in reversed(range(1, left_row - 1)):
                res.append(matrix[level + i][level])
            self.helper(matrix, res, level + 1)


# Test code
mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
print Solution().spiralOrder(mtx)
