"""
https://leetcode.com/problems/divide-two-integers/description/

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ret = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                ret += i
                i <<= 1
                tmp <<= 1
        if not positive:
            return ret * -1
        return min(max(-2147483648, ret), 2147483647)


# Test code
print Solution().divide(1, 1)
