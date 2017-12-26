"""
https://leetcode.com/problems/remove-invalid-parentheses/description/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.remove(s, ans, 0, 0, ('(', ')'))
        return ans

    def remove(self, s, res, last_i, last_j, par):
        print s
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == par[0]:
                count += 1
            if s[i] == par[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                    self.remove(s[0:j] + s[j + 1:], res, i, j, par)
            return
        rev = s[::-1]
        print rev
        if par[0] == '(':
            self.remove(rev, res, 0, 0, (')', '('))
        else:
            res.append(rev)


# Test code
print Solution().removeInvalidParentheses("(()))")
