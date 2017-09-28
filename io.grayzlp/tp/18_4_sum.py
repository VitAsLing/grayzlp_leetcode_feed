"""
https://leetcode.com/problems/4sum/description/

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if nums is None or len(nums) < 4:
            return []
        list.sort(nums)
        if nums[0] * 4 > target or nums[-1] * 4 < target:
            return []
        ret = []
        for i in range(0, len(nums) - 3):
            z = nums[i]
            if i > 0 and z == nums[i - 1]:
                continue
            if z + 3 * nums[-1] < target:
                continue
            if z * 4 > target:
                continue
            if z * 4 == target:
                if i + 3 < len(nums) and nums[i + 3] == z:
                    ret.append([z, z, z, z])
                    break
            for three_sum_ret in self.threeSum(nums, target - z, i + 1, len(nums) - 1):
                    ret.append([z] + three_sum_ret)
        return ret

    def threeSum(self, nums, target, lo, hi):
        if lo + 1 >= hi:
            return []
        if 3 * nums[lo] > target or 3 * nums[hi] < target:
            return []
        ret = []
        for i in range(lo, hi - 1):
            z = nums[i]
            if i > lo and z == nums[i - 1]:
                continue
            if z + 2 * nums[hi] < target:
                continue
            if z * 3 > target:
                continue
            if z * 3 == target:
                if i + 1 < hi and nums[i + 2] == z:
                    ret.append([z, z, z])
                    break
            for two_sum_ret in self.twoSum(nums, target - z, i + 1, hi):
                ret.append([z] + two_sum_ret)
        return ret

    def twoSum(self, nums, target, lo, hi):
        if lo >= hi:
            return []
        if 2 * nums[lo] > target or 2 * nums[hi] < target:
            return []
        i, j = lo, hi
        ret = []
        while i < j:
            sum_ = nums[i] + nums[j]
            if sum_ == target:
                ret.append([nums[i], nums[j]])
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif sum_ < target:
                while i < j and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
            elif sum_ > target:
                while i < j and nums[j] == nums[j - 1]:
                    j -= 1
                j -= 1
        return ret


# Test code
print Solution().fourSum([1, 2, 3, 4, 2, 0], 5)
