"""
https://leetcode.com/problems/convert-bst-to-greater-tree/description/

Given a Binary Search Tree (BST), convert it to a Greater Tree such that
every key of the original BST is changed to the original key plus sum of
all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        sum = self.sumNode(root)
        stack = []
        cur = root
        while cur or len(stack):
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur.val, sum = sum, sum - cur.val
            cur = cur.right
        return root

    def sumNode(self, root):
        if not root:
            return 0
        return root.val + self.sumNode(root.left) + self.sumNode(root.right)


# Test code
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t2.left = t1
t2.right = t3

print Solution().convertBST(t2).val
