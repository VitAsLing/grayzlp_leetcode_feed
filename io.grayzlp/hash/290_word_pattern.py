"""
https://leetcode.com/problems/word-pattern/description/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        word = str.split(' ')
        if len(word) != len(pattern):
            return False
        dic = {}
        dic_reverse = {}
        for i in range(0, len(pattern)):
            p = pattern[i]
            if p in dic and dic[p] != word[i]:
                return False
            if word[i] in dic_reverse and dic_reverse[word[i]] != p:
                return False
            else:
                dic[p] = word[i]
                dic_reverse[word[i]] = p
        return True


# Test code
pattern = "abbc"
str = "dog cat cat dog"
print Solution().wordPattern(pattern, str)
