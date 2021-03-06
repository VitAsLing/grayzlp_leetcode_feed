"""
https://leetcode.com/problems/rectangle-area/description/

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        width = max((min(C, G) - max(A, E)), 0)
        height = max((min(D, H) - max(B, F)), 0)

        add = (C - A) * (D - B) + (G - E) * (H - F)
        return add - width * height


# Test code
print Solution().computeArea(1, 1, 3, 3, 2, 2, 4, 4)
