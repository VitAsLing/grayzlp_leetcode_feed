"""
https://leetcode.com/problems/perfect-squares/description/

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
import sys


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [sys.maxint] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]


# Test code
print Solution().numSquares(12)
print Solution().numSquares(13)
