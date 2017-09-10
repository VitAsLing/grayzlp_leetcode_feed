"""
https://leetcode.com/problems/regular-expression-matching/description/

Solution: 2D dp
"""


class Solution(object):
    def isMatch(self, s, p):
        dp = [[False for x in range(len(p) + 1)] for y in range(len(s) + 1)]
        dp[0][0] = True
        for y in range(1, len(p)):
            if p[y] == '*' and dp[0][y - 1]:
                dp[0][y + 1] = True
        for x in range(0, len(s)):
            for y in range(0, len(p)):
                if p[y] == '.':
                    dp[x + 1][y + 1] = dp[x][y]
                elif s[x] == p[y]:
                    dp[x + 1][y + 1] = dp[x][y]
                elif p[y] == '*':
                    if p[y - 1] != s[x] and p[y - 1] != '.':
                        dp[x + 1][y + 1] = dp[x + 1][y - 1]
                    else:
                        dp[x + 1][y + 1] = dp[x + 1][y] or dp[x][y + 1] or dp[x + 1][y - 1]
        return dp[len(s)][len(p)]


"""
Test code
"""
s = Solution()
print s.isMatch("", ".*")
