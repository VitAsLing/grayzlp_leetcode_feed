"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        rot = lo
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            real_mid = (mid + rot) % n
            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


# Test code
print Solution().search([4, 5, 6, 7, 1, 2, 3], 1)
