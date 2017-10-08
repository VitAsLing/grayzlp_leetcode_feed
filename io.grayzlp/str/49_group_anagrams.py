"""
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        for s in strs:
            sort_s = ''.join(sorted(str(s)))
            if sort_s not in mapping:
                mapping[sort_s] = [s];
            else:
                mapping[sort_s].append(s)
        res = []
        for k, v in mapping.iteritems():
            res.append(v)
        return res


# Test code
print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
