"""
https://leetcode.com/problems/reverse-words-in-a-string/description/

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.

"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: stra
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""
        queue = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue
            j = i + 1
            while j < len(s) and s[j] != ' ':
                j += 1
            if j > len(s):
                break
            queue.insert(0, s[i:j])
            i = j
        return ' '.join(queue)


# Test code
print Solution().reverseWords("")
