"""
https://leetcode.com/problems/roman-to-integer/description/

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ii = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ret = 0
        for i in reversed(range(len(m))):
            if s.startswith(m[i]):
                ret += i * 1000
                s = s[len(m[i]):]
                break
        for i in reversed(range(len(c))):
            if s.startswith(c[i]):
                ret += i * 100
                s = s[len(c[i]):]
                break
        for i in reversed(range(len(x))):
            if s.startswith(x[i]):
                ret += i * 10
                s = s[len(x[i]):]
                break
        for i in reversed(range(len(ii))):
            if s.startswith(ii[i]):
                ret += i * 1
                s = s[len(ii[i]):]
                break
        return ret


# Test code
print Solution().romanToInt('MCX')
