"""
https://leetcode.com/problems/sliding-window-maximum/description/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to
the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
"""


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0 or k <= 0:
            return []
        queue = []
        res = [0] * (len(nums) - k + 1)
        ri = 0
        for i in range(len(nums)):
            while len(queue) and queue[0] < (i - k + 1):
                queue.pop(0)
            while len(queue) and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                res[ri] = nums[queue[0]]
                ri += 1
        return res


# Test code
print Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
