"""
https://leetcode.com/problems/jump-game/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        reach = 0
        while i < len(nums) and i <= reach:
            reach = max(i + nums[i], reach)
            i += 1
        if i == len(nums):
            return True
        return False


# Test code
print Solution().canJump([1, 1, 1, 1])
