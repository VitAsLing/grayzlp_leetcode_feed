"""
https://leetcode.com/problems/symmetric-tree/description/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Iteratively
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        stack = []
        if root.left:
            if root.right:
                stack.append(root.left)
                stack.append(root.right)
            else:
                return False
        elif root.right:
            return False
        while len(stack) > 0:
            if len(stack) % 2 == 1:
                return False
            right = stack.pop()
            left = stack.pop()

            if left.val != right.val:
                return False
            if left.left:
                if right.right:
                    stack.append(left.left)
                    stack.append(right.right)
                else:
                    return False
            elif right.right:
                return False
            if left.right:
                if right.left:
                    stack.append(left.right)
                    stack.append(right.left)
                else:
                    return False
            elif right.left:
                return False
        return True

    # Recursively
    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.isSysmetricHelp(root.left, root.right)

    def isSysmetricHelp(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                self.isSysmetricHelp(left.left, right.right) and
                self.isSysmetricHelp(left.right, right.left))


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
print Solution().isSymmetric(n1)
