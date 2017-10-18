"""
https://leetcode.com/problems/subsets-ii/description/


Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums = sorted(nums)
        self.backtracing(ans, [], 0, nums)
        return ans

    def backtracing(self, res, part, start, nums):
        res.append(list(part))
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i - 1]:
                part.append(nums[i])
                self.backtracing(res, part, i + 1, nums)
                part.pop()


# Test code
print Solution().subsetsWithDup([4,4,4,1,4])
