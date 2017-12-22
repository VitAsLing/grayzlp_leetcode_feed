"""
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for c in t:
            if c not in dic:
                return False
            dic[c] -= 1
        for k in dic.keys():
            if dic[k] != 0:
                return False
        return True


# Test code
print Solution().isAnagram("asssaa", "aaasss")
print Solution().isAnagram("asssaa", "aaassd")
