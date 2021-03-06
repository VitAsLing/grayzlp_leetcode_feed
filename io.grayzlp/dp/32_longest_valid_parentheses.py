""""
https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

"""
# Analysis
"""
Solution : linear dp
Also can use stack to resolve.
"""


class Solution(object):
    def longestValidParentheses(self, s):
        # store the valid substring length which use this as the stop index
        dp = [0 for x in range(len(s) + 1)]
        for i in range(1, len(s)):
            if s[i] == '(':
                dp[i + 1] = 0
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i + 1] = dp[i - 1] + 2
                elif s[i - 1] == ')':
                    if (i - dp[i] - 1) >= 0 and s[i - dp[i] - 1] == '(':
                        dp[i + 1] = dp[i - dp[i] - 1] + dp[i] + 2
                    else:
                        dp[i + 1] = 0

        return max(dp)


# Test code
sol = Solution()
# print sol.longestValidParentheses("(())()())")
# print sol.longestValidParentheses("")
# print sol.longestValidParentheses("()(())")
print sol.longestValidParentheses("(()))")
