"""
https://leetcode.com/problems/unique-paths/description/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Solution : 2D dp
"""


class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0 for x in range(n + 1)] for y in range(m + 1)]
        dp[1][1] = 1
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] += dp[i][j + 1] + dp[i + 1][j]

        return dp[m][n]


# Test code
sol = Solution()
print sol.uniquePaths(1, 1)
