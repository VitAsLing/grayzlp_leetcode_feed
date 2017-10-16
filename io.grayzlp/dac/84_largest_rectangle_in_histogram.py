"""
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of
largest rectangle in the histogram.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        ans = 0
        while i < len(heights):
            if len(stack) == 0 or heights[i] >= heights[stack[len(stack) - 1]]:
                stack.append(i)
                i += 1
            else:
                cur = stack.pop()
                if len(stack) == 0:
                    left_index = 0
                else:
                    left_index = stack[len(stack) - 1] + 1
                ans = max(ans, heights[cur] * (i - left_index))
        while len(stack) > 0:
            cur = stack.pop()
            if len(stack) == 0:
                left_index = 0
            else:
                left_index = stack[len(stack) - 1] + 1
            ans = max(ans, heights[cur] * (i - left_index))
        return ans

    # O(n2) enum all possible rectangle
    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        ans = 0
        for i in range(0, len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                ans = max(ans, min_height * (j - i + 1))
        return ans


# Test code
print Solution().largestRectangleArea([2, 1, 2])
