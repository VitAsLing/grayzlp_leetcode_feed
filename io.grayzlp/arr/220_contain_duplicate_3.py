"""
https://leetcode.com/problems/contains-duplicate-iii/description/

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute
difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        dic = {}
        for i in range(len(nums)):
            reposition = nums[i] + (1 << 31)
            bucket = reposition / (t + 1)
            if bucket in dic:
                return True
            if bucket - 1 in dic and reposition - dic[bucket - 1] <= t:
                return True
            if bucket + 1 in dic and dic[bucket + 1] - reposition <= t:
                return True
            if i >= k:
                last_bucket = (nums[i - k] + (1 << 31)) / (t + 1)
                del dic[last_bucket]
            dic[bucket] = reposition
        return False


# Test code
print Solution().containsNearbyAlmostDuplicate([1, 3, 1], 1, 1)
