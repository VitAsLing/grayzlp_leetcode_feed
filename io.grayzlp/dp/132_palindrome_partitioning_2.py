"""
https://leetcode.com/problems/palindrome-partitioning-ii/description/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0
        dp = [x - 1 for x in range(n + 1)]
        for i in range(0, n):
            odd_offset = 0
            while i - odd_offset >= 0 and i + odd_offset < n and s[i + odd_offset] == s[i - odd_offset]:
                dp[i + odd_offset + 1] = min(dp[i + odd_offset + 1], 1 + dp[i - odd_offset])
                odd_offset += 1
            even_offset = 0
            while i - even_offset >= 0 and i + even_offset + 1 < n and s[i + even_offset + 1] == s[i - even_offset]:
                dp[i + even_offset + 2] = min(dp[i + even_offset + 2], 1 + dp[i - even_offset])
                even_offset += 1
        return dp[n]


# Test code
sol = Solution()
print sol.minCut("aabaaaac")
