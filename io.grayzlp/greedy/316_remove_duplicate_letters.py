"""
https://leetcode.com/problems/remove-duplicate-letters/discuss/76768/A-short-O(n)-recursive-greedy-solution

Given a string which contains only lowercase letters, remove duplicate letters so that every letter
appear once and only once. You must make sure your result is the smallest in lexicographical order
among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cni = [0 for _ in xrange(26)]
        for c in s:
            cni[ord(c) - ord('a')] += 1
        pos = 0
        for i in xrange(len(s)):
            if ord(s[i]) < ord(s[pos]):
                pos = i
            cni[ord(s[i]) - ord('a')] -= 1
            if cni[ord(s[i]) - ord('a')] == 0:
                break
        if len(s) == 0:
            return ""
        return s[pos] + self.removeDuplicateLetters(s[pos + 1:].replace(s[pos], ""))


# Test code
print(Solution().removeDuplicateLetters("dabcab"))
