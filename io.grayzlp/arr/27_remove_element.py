"""
https://leetcode.com/problems/remove-element/description/

Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
"""



class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        tail = length - 1
        i = 0
        while i <= tail:
            if nums[i] == val:
                nums[i] = nums[tail]
                tail -= 1
            else:
                i += 1
        return i


# Test code
l = [1, 2, 2, 4, 2, 5, 2]
print Solution().removeElement(l, 2)
print l