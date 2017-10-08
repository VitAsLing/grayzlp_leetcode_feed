"""
https://leetcode.com/problems/permutations-ii/description/

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        used = [False for i in range(len(nums))]
        self.backtracking(sorted(nums), used, res, [])
        return res

    def backtracking(self, nums, used, res, tmp):
        if len(tmp) == len(nums):
            res.append(list(tmp))
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                    continue
                else:
                    tmp.append(nums[i])
                    used[i] = True
                    self.backtracking(nums, used, res, tmp)
                    used[i] = False
                    tmp.pop()


# Test code
print Solution().permuteUnique([2, 2, 1, 1])
