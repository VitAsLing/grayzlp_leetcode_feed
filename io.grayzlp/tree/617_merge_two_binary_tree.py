"""
https://leetcode.com/problems/merge-two-binary-trees/description/

Given two binary trees and imagine that when you put one of them to
cover the other, some nodes of the two trees are overlapped while the
 others are not.

You need to merge them into a new binary tree. The merge rule is that
if two nodes overlap, then sum node values up as the new value of the
merged node. Otherwise, the NOT null node will be used as the node of
new tree.

Note: The merging process must start from the root nodes of both trees.


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None

        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 if t1 else t2


# Test code
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t1.left = t2
t3.left = t4

t = Solution().mergeTrees(t1, t3)
print t.val
print t.left.val
