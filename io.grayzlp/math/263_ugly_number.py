"""
https://leetcode.com/problems/ugly-number/description/

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14
is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in (2, 3, 5):
            while num % i == 0 and num > 1:
                num /= i
        return num == 1


# Test code
print Solution().isUgly(14)
print Solution().isUgly(6)

