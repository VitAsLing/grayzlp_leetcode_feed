"""
https://leetcode.com/problems/power-of-two/description/

Given an integer, write a function to determine if it is a power of two.

"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0:
            return False
        if n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        else:
            return False


# Test code
print Solution().isPowerOfTwo(1)
print Solution().isPowerOfTwo(2)
print Solution().isPowerOfTwo(0)
print Solution().isPowerOfTwo(9)
