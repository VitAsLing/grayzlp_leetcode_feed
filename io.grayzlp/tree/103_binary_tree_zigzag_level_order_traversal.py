"""
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        self.zigzagLevelOrderHelper(ans, root, 0)
        return ans

    def zigzagLevelOrderHelper(self, res, node, level):
        if not node:
            return
        if len(res) <= level:
            res.append([])
        if not level % 2:
            res[level].append(node.val)
        else:
            res[level].insert(0, node.val)
        self.zigzagLevelOrderHelper(res, node.left, level + 1)
        self.zigzagLevelOrderHelper(res, node.right, level + 1)


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
print Solution().zigzagLevelOrder(n1)
