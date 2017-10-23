"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Mode Brilliant
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.help(root, None)

    def help(self, node, pre):
        if not node:
            return pre
        pre = self.help(node.right, pre)
        pre = self.help(node.left, pre)
        node.right = pre
        node.left = None
        return node

    # Iteratively
    def flatten1(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        head = root
        while head:
            if head.left:
                left = head.left
                right = head.right
                head.left = None
                head.right = left
                while left.right:
                    left = left.right
                left.right = right
            head = head.right

    # Recursively
    def flatten2(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left = root.left
        right = root.right
        self.flatten(left)
        self.flatten(right)
        if left:
            root.left = None
            root.right = left
            tail = left
            while tail.right:
                tail = tail.right
            tail.right = right


# Test code
print Solution().flatten(TreeNode(0))

