"""
https://leetcode.com/problems/search-insert-position/description/


Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo, hi, ret = 0, n - 1, -1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        else:
            if lo >= n or nums[lo] > target:
                return lo
            else:
                return lo + 1


# Test code
print Solution().searchInsert([1], 2)
