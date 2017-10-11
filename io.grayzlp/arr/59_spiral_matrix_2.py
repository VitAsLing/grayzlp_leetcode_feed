"""
https://leetcode.com/problems/spiral-matrix-ii/description/

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(0, n)]
        cur = 1
        for level in range(0, (n + 1) / 2):
            i, j = level, level
            while j < n - level:
                res[i][j] = cur
                cur += 1
                j += 1
            j -= 1
            i += 1
            while i < n - level:
                res[i][j] = cur
                cur += 1
                i += 1
            i -= 1
            j -= 1
            while j >= level:
                res[i][j] = cur
                cur += 1
                j -= 1
            j += 1
            i -= 1
            while i > level:
                res[i][j] = cur
                cur += 1
                i -= 1
        return res


# Test code
print Solution().generateMatrix(0)

