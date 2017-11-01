"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        queue = []
        valid_op = ['+', '-', '*', '/']
        for token in tokens:
            if token in valid_op:
                rhs = queue.pop()
                lhs = queue.pop()
                queue.append(self.evaluate(token, lhs, rhs))
            else:
                queue.append(token)
        return int(queue.pop())

    def evaluate(self, op, lhs, rhs):
        lhs = int(lhs)
        rhs = int(rhs)
        if op == '+':
            return lhs + rhs
        if op == '-':
            return lhs - rhs
        if op == '*':
            return lhs * rhs
        if op == '/':
            return int(float(lhs) / rhs)
        return None


# Test code
print Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
