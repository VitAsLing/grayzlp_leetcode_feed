"""
https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Dfs solution
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        """
        :param root:
        :return: if root is balanced, return height of root, otherwise return -1
        """
        if not root:
            return 0
        left = self.dfsHeight(root.left)
        if left == -1:
            return -1
        right = self.dfsHeight(root.right)
        if right == -1:
            return -1
        if abs(left - right) <= 1:
            return max(left, right) + 1
        return - 1

    # plain solution
    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1


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
print Solution().isBalanced(n1)
