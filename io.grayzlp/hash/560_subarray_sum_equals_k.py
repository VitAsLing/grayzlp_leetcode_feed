"""
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers and an integer k, you need to find the total number of
continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prev_dic = {0: 1}
        res = 0
        sum = 0
        for n in nums:
            sum += n
            if sum - k in prev_dic:
                res += prev_dic[sum - k]
            prev_dic[sum] = prev_dic.get(sum, 0) + 1
        return res


# Test code
print Solution().subarraySum([1, 1, 1, 1], 2)
