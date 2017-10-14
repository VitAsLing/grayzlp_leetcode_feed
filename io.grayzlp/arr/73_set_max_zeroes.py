"""
https://leetcode.com/problems/set-matrix-zeroes/description/

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix
        m = [False] * len(matrix)
        n = [False] * len(matrix[0])
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    m[i] = True
                    n[j] = True
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if m[i] or n[j]:
                    matrix[i][j] = 0


# Test code
mtx = [[1, 2, 3, 4],
       [2, 3, 0, 7],
       [3, 2, 1, 3]]
Solution().setZeroes(mtx)
print mtx
