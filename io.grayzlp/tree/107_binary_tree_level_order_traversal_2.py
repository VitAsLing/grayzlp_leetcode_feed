"""
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Iteratively
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        cur = [root]
        while len(cur):
            tmp = []
            count = len(cur)
            for i in range(count):
                node = cur.pop(0)
                tmp.append(node.val)
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            ans.insert(0, tmp)
        return ans

    # Recursively
    def levelOrderBottom2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        self.helper(ans, [root])
        return ans

    def helper(self, res, cur):
        if not len(cur):
            return
        next = []
        level = []
        for node in cur:
            level.append(node.val)
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
        res.insert(0, level)
        self.helper(res, next)


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(2)
n5 = TreeNode(3)
n1.left = n2
n2.left = n3
n1.right = n4
n4.right = n5
print Solution().levelOrderBottom(n1)
