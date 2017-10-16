"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[hi]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                hi -= 1
        return nums[lo] == target


# Test code
print Solution().search([3, 3, 3, 3, 1, 2], 4)
