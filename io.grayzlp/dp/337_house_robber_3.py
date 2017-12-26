"""
https://leetcode.com/problems/house-robber-iii/description/

The thief has found himself a new place for his thievery again. There is only one entrance to this area,
called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart
thief realized that "all houses in this place forms a binary tree". It will automatically contact the police
if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.robSub(root))

    def robSub(self, node):
        if not node:
            return 0, 0
        left = self.robSub(node.left)
        right = self.robSub(node.right)

        ans = [0, 0]
        ans[0] = max(left[0], left[1]) + max(right[0], right[1])
        ans[1] = node.val + left[0] + right[0]
        return ans


# Test code
t1 = TreeNode(10)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
print Solution().rob(t1)
