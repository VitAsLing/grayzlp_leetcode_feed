"""
https://leetcode.com/problems/3sum-closest/description/

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        best_distance = sys.maxint
        list.sort(nums)
        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                lo, hi, = i + 1, len(nums) - 1
                while lo < hi:
                    cur_distance = target - nums[i] - nums[lo] - nums[hi]
                    if abs(cur_distance) < abs(best_distance):
                        best_distance = cur_distance

                    if cur_distance == 0:
                        return target - cur_distance
                    elif cur_distance < 0:
                        hi -= 1
                    else:
                        lo += 1
        return target - best_distance


# Test code
print Solution().threeSumClosest([0, 1, 2], 3)

