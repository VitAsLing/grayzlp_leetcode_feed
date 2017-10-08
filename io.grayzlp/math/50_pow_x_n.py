"""
https://leetcode.com/problems/powx-n/description/

Implement pow(x, n).

"""


class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            return 1 / x * self.myPow(1 / x, -(n + 1))
        if n == 0:
            return 1
        if n == 2:
            return x * x
        if n % 2 == 0:
            return self.myPow(self.myPow(x, n / 2), 2)
        else:
            return x * self.myPow(self.myPow(x, n / 2), 2)


# Test code
print Solution().myPow(0.00001, 2147483647)

