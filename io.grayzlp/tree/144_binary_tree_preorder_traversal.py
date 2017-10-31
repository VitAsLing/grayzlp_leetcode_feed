"""
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Iteratively
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cur = root
        queue = []
        ans = []
        while cur or len(queue):
            while cur:
                queue.append(cur)
                ans.append(cur.val)
                cur = cur.left
            cur = queue.pop()
            cur = cur.right
        return ans

    # Recursively
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.helper(ans, root)
        return ans

    def helper(self, res, node):
        if not node:
            return
        res.append(node.val)
        self.helper(res, node.left)
        self.helper(res, node.right)


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4
print Solution().preorderTraversal(n1)
