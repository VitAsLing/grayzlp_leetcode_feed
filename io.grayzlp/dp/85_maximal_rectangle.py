"""
https://leetcode.com/problems/maximal-rectangle/description/

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

2D dp
"""


class Solution(object):
    def maximalRectangle(self, matrix):
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

        left = [0 for x in range(n)]
        right = [n for y in range(n)]
        height = [0 for z in range(n)]
        ret = 0
        for i in range(m):
            cur_left = 0
            cur_right = n
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], cur_left)
                else:
                    # height will be 0
                    left[j] = 0
                    cur_left = j + 1
            for j in reversed(range(n)):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                ret = max(ret, (right[j] - left[j]) * height[j])

        return ret


# Test code

row = [] * 3
mat = [row] * 3

print mat

sol = Solution()
print sol.maximalRectangle(mat)
