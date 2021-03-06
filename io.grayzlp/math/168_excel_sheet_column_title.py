"""
https://leetcode.com/problems/excel-sheet-column-title/description/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        else:
            return self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))


# Test code
print Solution().convertToTitle(28)
