"""
https://leetcode.com/problems/path-sum-ii/description/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ans = []
        self.dfs(ans, [], root, sum)
        return ans

    def dfs(self, res, part, node, sum):
        if not node:
            return
        if not node.left and not node.right and node.val == sum:
            res.append(list(part + [node.val]))
            return
        part.append(node.val)
        self.dfs(res, part, node.left, sum - node.val)
        self.dfs(res, part, node.right, sum - node.val)
        part.pop()


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
print Solution().pathSum(n1, 9)
