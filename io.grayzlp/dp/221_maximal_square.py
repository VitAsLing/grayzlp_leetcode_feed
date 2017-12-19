"""
https://leetcode.com/problems/maximal-square/description/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        size = [[0 for i in range(n)] for j in range(m)]
        maximal = 0
        for i in range(0, m):
            if matrix[i][0] == '1':
                size[i][0] = 1
            maximal = max(maximal, size[i][0])
        for j in range(1, n):
            if matrix[0][j] == '1':
                size[0][j] = 1
            maximal = max(maximal, size[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue
                size[i][j] = min(size[i - 1][j], size[i - 1][j - 1], size[i][j - 1]) + 1
                maximal = max(maximal, size[i][j])
        return maximal * maximal


# Test code
mat = [['1', '1', '1', '0', '0'],
       ['1', '0', '1', '0', '0'],
       ['1', '0', '1', '1', '0'],
       ['1', '0', '1', '1', '0'],
       ['1', '1', '1', '0', '0']]

mat2 = [["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]]

print Solution().maximalSquare(mat2)
