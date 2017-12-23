"""
https://leetcode.com/problems/ugly-number-ii/description/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.

"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * n
        res[0] = 1
        t2 = 0
        t3 = 0
        t5 = 0
        for i in range(1, n):
            res[i] = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            if res[i] == res[t2] * 2:
                t2 += 1
            if res[i] == res[t3] * 3:
                t3 += 1
            if res[i] == res[t5] * 5:
                t5 += 1
        return res[-1]


# Test code
print Solution().nthUglyNumber(7)

