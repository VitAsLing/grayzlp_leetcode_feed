"""
https://leetcode.com/problems/fraction-to-recurring-decimal/description/

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Credits:
Special thanks to @Shangrila for adding this problem and creating all test cases.
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        num = abs(numerator)
        den = abs(denominator)

        res.append(str(num / den))
        num %= den
        if num != 0:
            res.append('.')
        num_map = {num: len(res)}
        while num != 0:
            num *= 10
            res.append(str(num / den))
            num %= den
            if num in num_map.keys():
                pos = num_map[num]
                res.insert(pos, '(')
                res.append(')')
                break
            else:
                num_map[num] = len(res)
        print res
        return ''.join(res)


# Test code
print Solution().fractionToDecimal(1, 3)
