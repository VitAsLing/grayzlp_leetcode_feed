"""
https://leetcode.com/problems/unique-paths-ii/description/

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

Solution : 2D dp
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        dp[1][1] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i + 1][j + 1] = 0
                else:
                    dp[i + 1][j + 1] += dp[i][j + 1] + dp[i + 1][j]

        return dp[m][n]


# Test code
obs = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]]

sol = Solution()
print sol.uniquePathsWithObstacles(obs)
