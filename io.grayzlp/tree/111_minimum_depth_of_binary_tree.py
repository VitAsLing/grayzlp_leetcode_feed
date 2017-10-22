"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)
        if not min_left or not min_right:
            return min_left + min_right + 1
        else:
            return min(min_left, min_right) + 1


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(2)
n5 = TreeNode(3)
n1.left = n2
n1.right = n3
n3.right = n4
n4.right = n5
print Solution().minDepth(n1)
