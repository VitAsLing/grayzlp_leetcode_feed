"""
https://leetcode.com/problems/subsets/description/

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        self.backtracking(ans, [], 0, nums)
        return ans

    def backtracking(self, sets, part, start, nums):
        sets.append(list(part))
        for i in range(start, len(nums)):
            part.append(nums[i])
            self.backtracking(sets, part, i + 1, nums)
            part.pop()


# Test code
print Solution().subsets([1, 2, 3])
