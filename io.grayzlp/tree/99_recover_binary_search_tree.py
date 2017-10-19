"""
https://leetcode.com/problems/recover-binary-search-tree/description/

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""


# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(-sys.maxint - 1)
        first = None
        second = None
        cur = root
        stack = []
        while cur or len(stack) > 0:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not first and (prev and prev.val >= cur.val):
                first = prev
            if first and (prev and prev.val >= cur.val):
                second = cur
            prev = cur
            cur = cur.right
        tmp = first.val
        first.val = second.val
        second.val = tmp


# Test code
n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)
n1.left = n3
# n1.right = n2
Solution().recoverTree(n1)
print n1.left.val
