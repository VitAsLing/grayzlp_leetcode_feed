"""
https://leetcode.com/problems/palindrome-partitioning/description/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        self.dfs(ans, [], s, 0)
        return ans

    def dfs(self, res, part, s, start):
        if start == len(s):
            res.append(list(part))
            return
        else:
            for i in range(start + 1, len(s) + 1):
                if self.is_partition(s, start, i - 1):
                    part.append(s[start:i])
                    self.dfs(res, part, s, i)
                    part.pop()

    def is_partition(self, s, begin, end):
        while begin < end:
            if s[begin] != s[end]:
                return False
            begin += 1
            end -= 1
        return True


# Test code
print Solution().partition("aabbaa")
