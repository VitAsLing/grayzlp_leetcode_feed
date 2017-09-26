"""
https://leetcode.com/problems/longest-common-prefix/description/

Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs is None or len(strs) == 0:
            return ""
        pre = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(pre):
                pre = pre[0:-1]

        if len(pre) is None:
            return "".st
        return pre


# Test code
print Solution().longestCommonPrefix(["c", "cc", "ccc"])
