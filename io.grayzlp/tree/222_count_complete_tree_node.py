"""
https://leetcode.com/problems/count-complete-tree-nodes/description/

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level
are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def height(self, node):
        if not node:
            return 0
        return 1 + self.height(node.left)

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        h = self.height(root)
        if h == 0:
            return 0
        rh = self.height(root.right)
        if rh == h - 1:
            return (1 << (h - 1)) + self.countNodes(root.right)
        else:
            return (1 << (h - 2)) + self.countNodes(root.left)


# Test code
t1 = TreeNode(1)
t2 = TreeNode(1)
t3 = TreeNode(1)
t4 = TreeNode(1)
t1.left = t2
t1.right = t3
t2.left = t4
print Solution().countNodes(t1)
