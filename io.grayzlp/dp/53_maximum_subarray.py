"""
https://leetcode.com/problems/maximum-subarray/description/
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for x in range(len(nums) + 1)]
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            if dp[i] < 0:
                dp[i + 1] = nums[i]
            else:
                dp[i + 1] = nums[i] + dp[i]

        return max([dp[i] for i in range(1, len(nums) + 1)])


# Test code
sol = Solution()
print sol.maxSubArray([-1])
