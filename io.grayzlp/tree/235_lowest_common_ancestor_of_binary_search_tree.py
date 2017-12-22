"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: The lowest common ancestor is defined between two nodes v and w
 as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition.


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if (root.val - p.val) * (root.val - q.val) < 1:
            return root
        if p.val < root.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


# Test code
t1 = TreeNode(3)
t2 = TreeNode(2)
t3 = TreeNode(1)
t4 = TreeNode(4)
t1.left = t2
t2.left = t3
t1.right = t4
print Solution().lowestCommonAncestor(t1, t3, t4).val
print Solution().lowestCommonAncestor(t1, t2, t3).val
