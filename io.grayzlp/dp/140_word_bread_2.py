"""
https://leetcode.com/problems/word-break-ii/description/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""
import time


class Solution(object):
    """
    My solution
    """

    def word_break_helper(self, hs, dp_back, index):
        """
        :type hs: str
        :type dp_back: List[set]
        :type index: cur_index
        :rtype: List[str]
        """
        if index == 0:
            return ['']
        new_list = []
        for m in dp_back[index]:
            for strs in self.word_break_helper(hs, dp_back, m + 1):
                if m == -1:
                    new_list.append(strs + hs[m + 1:index])
                else:
                    new_list.append(strs + ' ' + hs[m + 1:index])
        return new_list

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        dp_set = [set() for x in range(n + 1)]
        dp = [False for x in range(n + 1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(0, i + 1):
                if dp[j] and s[j:i + 1] in wordDict:
                    dp[i + 1] = True
                    dp_set[i + 1].add(j - 1)
        print dp, dp_set
        return self.word_break_helper(s, dp_set, n)

    def wordBreak2(self, s, wordDict):
        """
        Stefan Pochmann 's solution
        https://discuss.leetcode.com/topic/35762/9-lines-python-10-lines-c
        :param s:
        :param wordDict:
        :return:
        """
        memo = {len(s): ['']}

        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i + 1, len(s) + 1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]

        return sentences(0)


# Test code
sol = Solution()
test_s = "catsanddog"
test_dict = ["cat", "cats", "and", "sand", "dog"]
print time.time()
print sol.wordBreak(test_s, test_dict)
print time.time()
