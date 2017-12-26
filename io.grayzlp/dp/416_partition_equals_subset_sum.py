"""
https://leetcode.com/problems/partition-equal-subset-sum/description/

Given a non-empty array containing only positive integers, find if the array
 can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0
        for n in nums:
            s += n
        if s & 1 == 1:
            return False
        half = s >> 1

        dp = [False] * (half + 1)
        dp[0] = True
        for n in nums:
            for i in range(half, 0, -1):
                if i >= n:
                    dp[i] = dp[i] or dp[i - n]
        return dp[-1]


# Test code
print Solution().canPartition([1, 5, 11, 5, 2])
