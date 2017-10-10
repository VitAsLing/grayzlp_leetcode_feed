"""
https://leetcode.com/problems/length-of-last-word/description/

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.

"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        for i in reversed(range(len(s))):
            if length == 0:
                if s[i] == ' ':
                    continue
                else:
                    length = 1
            else:
                if s[i] == ' ':
                    return length
                else:
                    length += 1
        return length


# Test code
print Solution().lengthOfLastWord('WWW www a  ')
