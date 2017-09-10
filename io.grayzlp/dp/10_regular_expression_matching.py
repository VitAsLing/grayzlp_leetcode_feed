# coding=utf-8
"""
https://leetcode.com/problems/regular-expression-matching/description/

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

# Analysis
"""
Use a 2d bool array to store state whether s[0, i] (s's substring) and p[0, j] can match or not.
When calculate the dp[i + 1][j + 1], three case:
1. if p[j] == s[i] :   dp[i + 1][j + 1] = dp[i][j]
2. if p[j] == '.' : dp[i + 1][j + 1] = dp[i][j]
3. if p[j] == * :
    1) p[j - 1] == s[i] or p[j - 1] == '.' :
        a. dp[i][j + 1]  a* represents multiple a
        b. dp[i + 1][j] a* represents one a
        c. dp[i + 1][j - 1] a* represents empty
        if a or b or c is true dp[i + 1][j + 1] can be true
    2) otherwise 
        dp[i + 1][j - 1] a* can only represent empty to match
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p)):
            if p[j] == '*' and dp[0][j - 1]:
                dp[0][j + 1] = True
        for i in range(0, len(s)):
            for j in range(0, len(p)):
                if p[j] == '.':
                    dp[i + 1][j + 1] = dp[i][j]
                elif s[i] == p[j]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j] == '*':
                    if p[j - 1] != s[i] and p[j - 1] != '.':
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = dp[i + 1][j] or dp[i][j + 1] or dp[i + 1][j - 1]
        return dp[len(s)][len(p)]


# Test code
s = Solution()
print s.isMatch("", ".*")
