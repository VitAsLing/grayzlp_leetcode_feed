"""
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
money you can rob tonight without alerting the police.

"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = 0
        prev_max = 0
        prev_prev_max = 0
        for num in nums:
            cur_max = max(prev_max, prev_prev_max + num)
            prev_prev_max = prev_max
            prev_max = cur_max
        return cur_max


# Test code
print Solution().rob([2, 2, 3, 3, 5])
