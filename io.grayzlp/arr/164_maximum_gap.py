"""
https://leetcode.com/problems/maximum-gap/description/

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Credits:
Special thanks to @porker2008 for adding this problem and creating all test cases.

"""
import math

import sys


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find max and min value
        if len(nums) < 2:
            return 0
        mi = nums[0]
        ma = nums[0]
        for num in nums:
            mi = min(mi, num)
            ma = max(ma, num)

        # put in to bucket
        gap = int(math.ceil(float(ma - mi) / (len(nums) - 1)))
        bucket_min = [sys.maxint for k in range(len(nums) - 1)]
        bucket_max = [-sys.maxint - 1 for k in range(len(nums) - 1)]
        for num in nums:
            if num == mi or num == ma:
                continue
            idx = (num - mi) / gap
            print idx
            bucket_min[idx] = min(num, bucket_min[idx])
            bucket_max[idx] = max(num, bucket_max[idx])

        # find max gap
        max_gap = 0
        prev = mi
        for i in range(len(bucket_min)):
            if bucket_min[i] == sys.maxint:
                continue
            max_gap = max(max_gap, bucket_min[i] - prev)
            prev = bucket_max[i]
        max_gap = max(max_gap, ma - prev)
        return max_gap


# Test code
print Solution().maximumGap([1, 10000000])
