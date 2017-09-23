"""
https://leetcode.com/problems/reverse-integer/description/

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        if x > 0:
            BASE = 10
        else:
            BASE = -10
        while x != 0:
            rev = rev * 10 + (x % BASE)
            x = (x / BASE) * BASE / 10
            if rev > 2**31 - 1 or rev < -(2**31):
                return 0
        return rev


# Test code
print Solution().reverse(123)
