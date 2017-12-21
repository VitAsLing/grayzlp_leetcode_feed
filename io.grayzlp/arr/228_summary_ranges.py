"""
https://leetcode.com/problems/summary-ranges/description/

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) == 0:
            return res
        start = -1
        prev = -1
        for i in range(len(nums)):
            num = nums[i]
            if i == 0:
                prev = num
                start = num
                continue
            cur = num
            if prev == cur - 1:
                prev = cur
                continue
            else:
                if start == prev:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(prev))
                prev = num
                start = num
        prev = nums[-1]
        if start == prev:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(prev))
        return res


# Test code
print Solution().summaryRanges([1, 2, 4, 7, 8, 10])
