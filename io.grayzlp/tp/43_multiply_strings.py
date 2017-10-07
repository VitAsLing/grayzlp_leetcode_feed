"""
https://leetcode.com/problems/multiply-strings/description/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        p = [0] * (m + n)
        for i in reversed(range(0, m)):
            for j in reversed(range(0, n)):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                su = p[p2] + mul
                p[p1] += su / 10
                p[p2] = su % 10

        res = ""
        for num in p:
            if not (len(res) == 0 and num == 0):
                res = res + str(num)
        if len(res) == 0:
            res = '0'
        return res


# Test code
print Solution().multiply("123", "456")
