"""
https://leetcode.com/problems/largest-number/description/

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def logic_order(a, b):
            stra = str(a)
            strb = str(b)
            if stra + strb > strb + stra:
                return -1
            else:
                return 1

        nums.sort(logic_order)
        res = ''
        if nums[0] == 0:
            return '0'
        for num in nums:
            res += str(num)
        return res


# Test code
print Solution().largestNumber([3, 30, 34, 5, 9])





