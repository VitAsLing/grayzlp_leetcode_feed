"""
https://leetcode.com/problems/first-missing-positive/description/


Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.

"""


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            target = nums[i]
            while 0 < target < len(nums) + 1 and target != nums[target - 1]:
                new_target = nums[target - 1]
                nums[target - 1] = target
                target = new_target
        i = 0
        while i < len(nums) and nums[i] == i + 1:
            i += 1
        return i + 1


# Test code
print Solution().firstMissingPositive([2, 1])
