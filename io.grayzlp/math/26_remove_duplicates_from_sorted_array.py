"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        id = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[id] = nums[i]
                id += 1
        return id


# Test cod
l = [1, 2, 2, 3, 4, 4, 6]
print Solution().removeDuplicates(l)
print l
