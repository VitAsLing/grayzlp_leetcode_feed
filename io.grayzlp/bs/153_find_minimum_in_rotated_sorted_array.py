"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[lo] <= nums[hi]:
                return nums[lo]
            mid = (lo + hi) / 2

            if nums[mid] >= nums[lo]:
                lo = mid + 1
            else:
                hi = mid


# Test code
print Solution().findMin([4, 1, 2])
