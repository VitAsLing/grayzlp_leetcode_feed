"""
https://leetcode.com/problems/triangle/description/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""
import sys


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m <= 0:
            return 0
        dp = [sys.maxint for x in range(m + 1)]
        dp[1] = triangle[0][0]
        for i in range(1, m):
            row = triangle[i]
            for j in reversed(range(len(row))):
                dp[j + 1] = min(dp[j], dp[j + 1]) + row[j]
        return min(dp)


# Test code
sol = Solution()
tri = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print sol.minimumTotal(tri)
