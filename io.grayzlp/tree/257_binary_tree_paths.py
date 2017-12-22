"""
https://leetcode.com/problems/binary-tree-paths/description/

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        ans = []
        if root.left:
            self.dfs(root.left, str(root.val), ans)
        if root.right:
            self.dfs(root.right, str(root.val), ans)
        return ans

    def dfs(self, node, part, res):
        part = part + "->" + str(node.val)
        if not node.left and not node.right:
            res.append(part)
            return
        if node.left:
            self.dfs(node.left, part, res)
        if node.right:
            self.dfs(node.right, part, res)


# Test code
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t1
t2.right = t3

print Solution().binaryTreePaths(t2)



