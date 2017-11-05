"""
https://leetcode.com/problems/majority-element/description/

Given an array of size n, find the majority element. The majority element is the element that appears more than
floor( n/2 ) times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
from collections import deque


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority = nums[0]
        count = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if count == 0:
                majority = num
                count += 1
            elif majority != num:
                count -= 1
            else:
                count += 1
        return majority


    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = self.sort(nums)
        return sorted_nums[len(sorted_nums) / 2]

    def sort(self, nums):
        if len(nums) <= 1:
            return nums

        def merge(lhs, rhs):
            res, lhs, rhs = deque(), deque(lhs), deque(rhs)

            while lhs and rhs:
                res.append(lhs.popleft() if lhs[0] < rhs[0] else rhs.popleft())
            res.extend(lhs if lhs else rhs)
            return list(res)

        mid = len(nums) / 2
        left = self.sort(nums[0:mid])
        right = self.sort(nums[mid:])
        return merge(left, right)


# Test code
print Solution().majorityElement([3, 3, 3, 6, 7])
