"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note
that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

"""


class Solution(object):
    # O(nlogn) solution
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0] * len(nums)
        size = 0
        for n in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) >> 1
                if tails[m] < n:
                    i = m + 1
                else:
                    j = m
            tails[i] = n
            if i == size:
                size += 1
        return size


    # my O(n2) solution
    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        best = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        for val in dp:
            best = max(best, val)
        return best


# Test code
print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
