"""
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such
that nums[i] = nums[j] and the absolute difference between i and j is at most k.

"""


class Solution(object):

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        collect = set()
        for i in range(len(nums)):
            if i > k:
                collect.remove(nums[i - k - 1])
            if nums[i] in collect:
                return True
            collect.add(nums[i])
        return False

    # tle
    def containsNearbyDuplicate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic.keys():
                if i - dic[nums[i]] <= k:
                    return True
            dic[nums[i]] = i
        return False


# Test code
print Solution().containsNearbyDuplicate([1, 2, 3, 4, 1], 3)
