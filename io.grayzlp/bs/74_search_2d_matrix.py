"""
https://leetcode.com/problems/search-a-2d-matrix/description/

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0 or len(matrix[0]) == 0:
            return False
        n = len(matrix[0])
        lo, hi = 0, m * n
        while lo < hi:
            mid = (lo + hi) / 2
            cur = matrix[mid / n][mid % n]
            if cur == target:
                return True
            elif cur < target:
                lo = mid + 1
            else:
                hi = mid
        return False


# Test code
mtx = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 13]]
print Solution().searchMatrix(mtx, 19)

