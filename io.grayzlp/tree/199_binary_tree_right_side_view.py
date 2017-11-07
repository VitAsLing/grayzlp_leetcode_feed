"""
https://leetcode.com/problems/binary-tree-right-side-view/description/

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can
see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # DFS
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.rightView(root, res, 0)
        return res

    def rightView(self, node, res, level):
        if not node:
            return
        if level == len(res):
            res.append(node.val)
        self.rightView(node.right, res, level + 1)
        self.rightView(node.left, res, level + 1)

    # Straight Solution like BFS
    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        level = [root]
        while level:
            res.append(level[len(level) - 1].val)
            level = self.levelOrder(level)
        return res

    def levelOrder(self, nodes):
        new_level = []
        for node in nodes:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        return new_level


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n3.right = n4

print Solution().rightSideView(n1)
