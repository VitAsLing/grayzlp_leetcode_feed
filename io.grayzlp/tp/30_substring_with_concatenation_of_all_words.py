"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
from collections import defaultdict


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ret, n, m = [], len(s), len(words)
        if n <= 0 or m <= 0:
            return ret
        dict = defaultdict(lambda: 0)
        for word in words:
            dict[word] += 1

        wl = len(words[0])
        for i in range(0, wl):
            t_dict = defaultdict(lambda: 0)
            left = i
            count = 0
            for j in range(i, n - wl + 1, wl):
                str = s[j:j + wl]
                if dict.get(str) > 0:
                    t_dict[str] += 1
                    if t_dict[str] <= dict[str]:
                        count += 1
                    else:
                        while t_dict[str] > dict[str]:
                            left_side = s[left:left + wl]
                            t_dict[left_side] -= 1
                            if t_dict[left_side] < dict[left_side]:
                                count -= 1
                            left += wl
                    if count == m:
                        ret.append(left)
                        t_dict[s[left:left + wl]] -= 1
                        count -= 1
                        left += wl
                else:
                    t_dict.clear()
                    count = 0
                    left = j + wl
        return ret


# Test code
print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])
