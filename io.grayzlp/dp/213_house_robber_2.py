"""
https://leetcode.com/problems/house-robber-ii/description/

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not
get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the
neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous
street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.
"""


class Solution(object):
    def rob(self, nums):
        """
        Dp Solution
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        # robber on first day
        prev_prev = 0
        prev = nums[0]

        prev_prev_without_first = 0
        prev_without_first = 0
        for i in range(1, len(nums)):
            cur = max(prev_prev + nums[i], prev)
            prev_prev = prev
            prev = cur

            cur_without_first = max(prev_prev_without_first + nums[i], prev_without_first)
            prev_prev_without_first = prev_without_first
            prev_without_first = cur_without_first
        profit = max(prev_without_first, prev_prev)
        return profit


# Test code
print Solution().rob([1, 2, 5])
