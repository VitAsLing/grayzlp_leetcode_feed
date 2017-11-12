"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/


Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
of which the sum >= s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

"""
import sys


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i, j, sum = 0, 0, 0
        mi = sys.maxint
        while j < len(nums):
            sum += nums[j]
            while sum >= s and i <= j:
                print i, j
                mi = min(mi, j - i + 1)
                sum -= nums[i]
                i += 1
            j += 1
        if mi == sys.maxint:
            mi = 0
        return mi


# Test code
print Solution().minSubArrayLen(100, [2, 3, 1, 2, 4, 3])
