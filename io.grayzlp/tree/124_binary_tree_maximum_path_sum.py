"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/


Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""


# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.max_value = -sys.maxint - 1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.max_value

    def dfs(self, node):
        if not node:
            return 0
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        self.max_value = max(self.max_value, left + right + node.val)
        return max(left, right) + node.val


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
print Solution().maxPathSum(n1)
