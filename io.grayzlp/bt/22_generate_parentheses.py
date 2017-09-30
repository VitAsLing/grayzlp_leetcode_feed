"""
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.back_tracking("", 0, 0, n, ret)
        return ret

    def back_tracking(self, part, left, right, n, ret):
        if left == right == n:
            if n == 0:
                return
            ret.append(part)
            return
        if left < n:
            self.back_tracking(part + "(", left + 1, right, n, ret)
        if right < left:
            self.back_tracking(part + ")", left, right + 1, n, ret)


# Test code
print Solution().generateParenthesis(3)
