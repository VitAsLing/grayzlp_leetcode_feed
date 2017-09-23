"""
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        min_start, max_length = 0, 1
        i = 0
        while i < len(s):
            if i + max_length / 2 >= len(s):
                return s[min_start:(min_start + max_length)]
            j = i
            k = i
            while k < len(s) - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while k < len(s) - 1 and j > 0 and s[j - 1] == s[k + 1]:
                j -= 1
                k += 1
            if k - j + 1 > max_length:
                min_start = j
                max_length = k - j + 1
        return s[min_start:(min_start + max_length)]


# Test code
print Solution().longestPalindrome("cbbddd")
