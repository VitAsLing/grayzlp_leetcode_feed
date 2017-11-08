"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/description/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

"""


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0:
            return 0
        move = 1
        while m != n:
            m >>= 1
            n >>= 1
            move <<= 1
        return m * move


# Test code
print Solution().rangeBitwiseAnd(5, 7)
