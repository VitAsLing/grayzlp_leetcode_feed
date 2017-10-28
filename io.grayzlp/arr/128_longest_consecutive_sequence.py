"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""
import collections


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        map = collections.defaultdict(lambda: 0)
        best = 0
        for n in nums:
            left = map[n - 1]
            right = map[n + 1]
            total = left + right + 1
            map[n] = total
            best = max(best, total)

            map[n - left] = total
            map[n + right] = total
        return best

    # More straight solution
    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best


# Test code
print Solution().longestConsecutive([223, 2, 2321, 1, 3, 4])
