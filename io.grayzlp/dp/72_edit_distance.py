"""
https://leetcode.com/problems/edit-distance/description/

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

It is obvious that operation a anb b is same operation.
2D dp
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0 for x in range(n + 1)] for y in range(m + 1)]
        dp[0][0] = 0
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            dp[i][0] = i
        for i in range(0, m):
            for j in range(0, n):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1

        return dp[m][n]


# Test code
sol = Solution()
print sol.minDistance("swt", "bwtttt")
