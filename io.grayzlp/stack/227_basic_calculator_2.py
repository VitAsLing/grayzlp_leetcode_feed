"""
https://leetcode.com/problems/basic-calculator-ii/description/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.

"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        sign = '+'
        num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)

            if not c.isdigit() and c != ' ' or (i == (len(s) - 1)):
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    stack.append(int(float(stack.pop()) / num))
                sign = c
                num = 0
        res = 0
        for i in stack:
            res += i
        return res


# Test code
print Solution().calculate("14-3/2")
