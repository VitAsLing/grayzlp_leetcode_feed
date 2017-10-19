"""
https://leetcode.com/problems/validate-binary-search-tree/description/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

"""

# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_valid(root, -sys.maxint - 1, sys.maxint)

    def is_valid(self, root, min_val, max_val):
        if not root:
            return True
        if not min_val < root.val < max_val:
            return False
        if self.is_valid(root.left, min_val, root.val) and self.is_valid(root.right, root.val, max_val):
            return True
        return False


# Test code
n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print Solution().isValidBST(n1)
