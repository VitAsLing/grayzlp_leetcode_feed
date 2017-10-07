"""
https://leetcode.com/problems/jump-game-ii/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        count = 0
        while curr < len(nums) - 1:
            candidate = nums[curr]
            max_scope = 0
            choice = -1
            for i in reversed(range(1, candidate + 1)):
                j = curr + i
                if j >= len(nums) - 1:
                    return count + 1
                if j + nums[j] >= len(nums) - 1:
                    return count + 2
                if max_scope < (j + nums[j]):
                    max_scope = j + nums[j]
                    choice = j
            curr = choice
            count += 1
        return count


# Test code
print Solution().jump([1, 1, 1, 1, 1])
