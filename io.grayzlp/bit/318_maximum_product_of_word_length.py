"""
https://leetcode.com/problems/maximum-product-of-word-lengths/description/

Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume that each word will contain
 only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        val = [0 for _ in xrange(len(words))]
        for i in xrange(len(words)):
            word = words[i]
            for ch in word:
                val[i] |= 1 << (ord(ch) - ord('a'))
        ret = 0
        for i in xrange(len(words) - 1):
            for j in xrange(i + 1, len(words)):
                if val[i] & val[j] == 0 and len(words[i]) * len(words[j]) > ret:
                    ret = len(words[i]) * len(words[j])
        return ret


# Test code
print(Solution().maxProduct(['a', 'aa', 'cc', 'ddd', 'aaa']))





