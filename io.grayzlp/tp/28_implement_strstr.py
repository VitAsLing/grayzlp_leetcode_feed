"""
https://leetcode.com/problems/implement-strstr/description/

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        if n == 0:
            return 0
        elif m == 0:
            return -1
        i = 0
        while i + n - 1 < m:
            j = 0
            while j < n and haystack[i + j] == needle[j]:
                j += 1
            if j == n:
                return i
            i += 1
        return -1


# Test code:
print Solution().strStr("", "avd")
