"""
https://leetcode.com/problems/path-sum-iii/description/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return 0
        return self.pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def pathSumFrom(self, root, sum):
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res = 1
        return res + self.pathSumFrom(root.left, sum - root.val) + self.pathSumFrom(root.right, sum - root.val)

    # my native solution
    def __init__(self):
        self.count = 0

    def pathSumNative(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.dfs([], root, sum)
        return self.count

    def dfs(self, paths, node, target):
        if not node:
            return
        paths += [0]
        for i in xrange(len(paths)):
            paths[i] += node.val
            if paths[i] == target:
                self.count += 1
        self.dfs(paths, node.left, target)
        self.dfs(paths, node.right, target)
        for i in xrange(len(paths)):
            paths[i] -= node.val
        paths.pop()


# Test code
t1 = TreeNode(1)
t2 = TreeNode(1)
t3 = TreeNode(1)
t4 = TreeNode(1)
t5 = TreeNode(1)
t1.left = t2
t1.right = t3
t2.left = t4
t3.right = t5
print Solution().pathSum(t1, 2)
