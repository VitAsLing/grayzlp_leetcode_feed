# coding=utf-8
"""
https://leetcode.com/problems/wildcard-matching/description/

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

2d dp
"""


class Solution(object):
    def isMatch(self, s, p):
        dp = [[False for x in range(len(p) + 1)] for y in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(len(p)):
            if p[j] == '*':
                dp[0][j + 1] = True
            else:
                break
        for i in range(len(s)):
            for j in range(len(p)):
                print dp
                if p[j] == '*':
                    dp[i + 1][j + 1] = dp[i][j + 1] or dp[i + 1][j] or dp[i][j]
                else:
                    dp[i + 1][j + 1] = dp[i][j] and (s[i] == p[j] or p[j] == '?')

        return dp[len(s)][len(p)]


# Test code
sol = Solution()
print sol.isMatch("aab", "z*")
