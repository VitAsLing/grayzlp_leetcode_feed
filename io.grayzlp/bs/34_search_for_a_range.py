"""
https://leetcode.com/problems/search-for-a-range/description/

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lo, hi = 0, n - 1
        ret_low, ret_hi = -1, -1
        while lo <= hi:
            mid = (lo + hi) / 2
            if mid == 0 or nums[mid] > nums[mid - 1]:
                if nums[mid] == target:
                    ret_low = mid
            if mid == n - 1 or nums[mid] < nums[mid + 1]:
                if nums[mid] == target:
                    ret_hi = mid
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                i = mid
                while i > 0 and nums[i - 1] == target:
                    i -= 1
                ret_low = i
                j = mid
                while j < n - 1 and nums[j + 1] == target:
                    j += 1
                ret_hi = j
                break
            else:
                hi = mid - 1
        return [ret_low, ret_hi]


# Test code
print Solution().searchRange([1], 1)


