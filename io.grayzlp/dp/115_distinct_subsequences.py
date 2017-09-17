"""
https://leetcode.com/problems/distinct-subsequences/description/

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)
        dp = [[0 for x in range(m + 1)] for y in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = 1
        for i in range(0, n):
            for j in range(0, m):
                if s[j] == t[i]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[n][m]


# Test code
sol = Solution()
print sol.numDistinct("rabbbit", "rabbit")
