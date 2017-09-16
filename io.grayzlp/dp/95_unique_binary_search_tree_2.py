"""
https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def offset(self, node, offset):
        if node is None:
            return None
        new_node = TreeNode(node.val + offset)
        new_node.left = self.offset(node.left, offset)
        new_node.right = self.offset(node.right, offset)
        return new_node

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n <= 0:
            return []
        dp = [[] for x in range(n + 1)]
        dp[0].append(None)
        for i in range(1, n + 1):
            for j in range(0, i):
                for left_node in dp[j]:
                    for right_node in dp[i - 1 - j]:
                        new_node = TreeNode(j + 1)
                        new_node.left = left_node
                        new_node.right = self.offset(right_node, j + 1)
                        dp[i].append(new_node)

        return dp[n]


# Test code
sol = Solution()
print sol.generateTrees(3)
