"""
https://leetcode.com/problems/range-sum-query-immutable/description/

Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cache = []
        count = 0
        for num in nums:
            count += num
            self.cache.append(count)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.cache[j]
        return self.cache[j] - self.cache[i - 1]


# Test code
obj = NumArray([-2, 3, 2, 1])
print obj.sumRange(0, 2)
print obj.sumRange(1, 3)
