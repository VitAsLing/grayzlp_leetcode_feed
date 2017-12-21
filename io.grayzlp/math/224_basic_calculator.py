"""
https://leetcode.com/problems/basic-calculator/description/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        number = 0
        sign = 1
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == "+":
                result += sign * number
                number = 0
                sign = 1
            elif c == "-":
                result += sign * number
                number = 0
                sign = -1
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ")":
                result += sign * number
                number = 0
                result *= stack.pop()
                result += stack.pop()
        if number != 0:
            result += sign * number
        return result


# Test code
print Solution().calculate("1 + 3 - 2 + (6 - 7)")

