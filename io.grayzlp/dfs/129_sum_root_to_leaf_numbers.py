"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, root, prev):
        if not root:
            return 0
        if not root.left and not root.right:
            return prev * 10 + root.val
        return self.helper(root.left, prev * 10 + root.val) + self.helper(root.right, prev * 10 + root.val)

    def sumNumbers2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.dfs(root)
        print res
        total = 0
        for r in res:
            total += int(''.join(r))
        return total

    def dfs(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[str(root.val)]]
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        ans = []

        for x in left + right:
            x.insert(0, str(root.val))
            ans.append(list(x))
            x.pop(0)
        return ans


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print Solution().sumNumbers(n1)
