"""
https://leetcode.com/problems/burst-balloons/description/

Given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by array nums.
 You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right]
 coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <= n <= 500, 0 <= nums[i] <+ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xnums = [1] + [num for num in nums if num] + [1]
        l = len(xnums)
        memory = [[0] * l for _ in range(l)]
        return self.burst(xnums, memory, 0, l - 1)

    def burst(self, nums, memo, left, right):
        if memo[left][right] > 0:
            return memo[left][right]
        for i in range(left + 1, right):
            memo[left][right] = max(memo[left][right], nums[i] * nums[left] * nums[right] +
                                    self.burst(nums, memo, left, i) +
                                    self.burst(nums, memo, i, right))
        return memo[left][right]


# Test code
print Solution().maxCoins([3, 1, 5, 8])
