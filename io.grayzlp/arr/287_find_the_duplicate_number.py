"""
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
 prove that at least one duplicate number must exist. Assume that there is only one duplicate number,
 find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return None
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow


# Test code
print Solution().findDuplicate([1, 2, 3, 4, 3])
print Solution().findDuplicate([1, 3, 3, 4, 3])