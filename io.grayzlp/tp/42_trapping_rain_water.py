"""
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_left, max_right = 0, 0
        ret = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    ret += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    ret += max_right - height[right]
                right -= 1
        return ret


# Test code
print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
