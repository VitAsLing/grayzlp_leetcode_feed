"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j, rmax = 0, 0, 0
        kvmap = {}
        while i < len(s):
            if s[i] in kvmap.keys():
                j = max(j, kvmap.get(s[i]) + 1)
            kvmap[s[i]] = i
            rmax = max(rmax, i - j + 1)
            i += 1
        return rmax


# Test code
print Solution().lengthOfLongestSubstring("pwwkew")

