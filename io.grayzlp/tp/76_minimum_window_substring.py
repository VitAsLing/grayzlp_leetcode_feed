"""
https://discuss.leetcode.com/category/84/minimum-window-substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

"""
from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        di = defaultdict(lambda: 0)
        for c in t:
            di[c] += 1
        count = len(t)
        begin, end, best, res = 0, 0, len(s) + 1, ''
        while end < len(s):
            if di[s[end]] > 0:
                count -= 1
            di[s[end]] -= 1
            end += 1
            while count == 0:
                if end - begin < best:
                    best = end - begin
                    res = s[begin:end]
                if di[s[begin]] == 0:
                    count += 1
                di[s[begin]] += 1
                begin += 1
        return res


# Test code
print Solution().minWindow("ADOBECODEBANC", "ABC")
