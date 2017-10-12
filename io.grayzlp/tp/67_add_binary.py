"""
https://leetcode.com/problems/add-binary/description/

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        plus = 0
        res = ''
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                su = int(a[i]) + int(b[j]) + plus
                i -= 1
                j -= 1
                plus = su / 2
                res = str(su % 2) + res
                continue
            elif i >= 0:
                su = int(a[i]) + plus
                i -= 1
                plus = su / 2
                res = str(su % 2) + res
            elif j >= 0:
                su = int(b[j]) + plus
                j -= 1
                plus = su / 2
                res = str(su % 2) + res
        if plus > 0:
            res = str(plus) + res
        return res


# Test code
print Solution().addBinary("111", "11")
