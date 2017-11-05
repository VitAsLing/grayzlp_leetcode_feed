"""
https://leetcode.com/problems/factorial-trailing-zeroes/description/

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 5
        res = 0
        while n / i > 0:
            res += n / i
            i *= 5
        return res


# Test code
print Solution().trailingZeroes(100)
