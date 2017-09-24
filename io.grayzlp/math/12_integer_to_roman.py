"""
https://leetcode.com/problems/integer-to-roman/description/

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return m[num / 1000 % 10] + c[num / 100 % 10] + x[num / 10 % 10] + i[num % 10]


# Test code
print Solution().intToRoman(2333)

