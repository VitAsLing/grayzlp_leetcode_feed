"""
https://leetcode.com/problems/majority-element-ii/description/

Given an integer array of size n, find all elements that appear more than |_ n/3 _] times.
The algorithm should run in linear time and in O(1) space.

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return list(set(nums))
        candidate1 = nums[0]
        count1 = 0
        candidate2 = nums[0]
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 += 1
            elif count2 == 0:
                candidate2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        res = []
        if count1 > (len(nums) / 3):
            res.append(candidate1)
        if count2 > (len(nums) / 3) and candidate2 != candidate1:
            res.append(candidate2)
        return res


# Test code
print Solution().majorityElement([1])


