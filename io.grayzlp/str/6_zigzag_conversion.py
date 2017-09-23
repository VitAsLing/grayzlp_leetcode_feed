"""
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_list = ['' for x in range(numRows)]
        i = 0
        while i < len(s):
            idx = 0
            while idx < numRows and i < len(s):
                str_list[idx] += s[i]
                i += 1
                idx += 1
            idx = numRows - 2
            while idx > 0 and i < len(s):
                str_list[idx] += s[i]
                i += 1
                idx -= 1

        for j in range(1, numRows):
            str_list[0] += str_list[j]
        return str_list[0]


# Test code
print Solution().convert("", 3)



