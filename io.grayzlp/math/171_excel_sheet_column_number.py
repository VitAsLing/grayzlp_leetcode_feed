"""
https://leetcode.com/problems/excel-sheet-column-number/description/

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        for c in s:
            val = (ord(c) - ord('A')) + 1
            prev = prev * 26 + val
        return prev


# Test code
print Solution().titleToNumber("AA")
