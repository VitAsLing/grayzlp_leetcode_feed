"""
https://leetcode.com/problems/container-with-most-water/description/

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j, max_water = 0, len(height) - 1, 0
        while i < j:
            h = min(height[i], height[j])
            max_water = max(max_water, (j - i) * h)
            print max_water
            while height[i] <= h and i < j:
                i += 1
            while height[j] <= h and i < j:
                j -= 1
        return max_water


# Test code
print Solution().maxArea([1, 3, 2, 5, 25, 24, 5])
