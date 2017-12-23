"""
https://leetcode.com/problems/single-number-ii/description/

Given an array of integers, every element appears three times except for one, which appears exactly once.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        print ones


# Test code
print Solution().singleNumber([2, 2, 3, 4, 2, 4, 4])
