"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif len(stack) > 0:
                if c == ')' and stack.pop() == '(':
                    continue
                elif c == '}' and stack.pop() == '{':
                    continue
                elif c == ']' and stack.pop() == '[':
                    continue
                else:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


## Test code
print Solution().isValid("]")

