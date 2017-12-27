"""
https://leetcode.com/problems/diameter-of-binary-tree/description/

Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.best = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth(root)
        return self.best

    def max_depth(self, node):
        if not node:
            return 0

        left = self.max_depth(node.left)
        right = self.max_depth(node.right)

        self.best = max(self.best, left + right)

        return max(left, right) + 1


# Test code
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3

print Solution().diameterOfBinaryTree(t1)
