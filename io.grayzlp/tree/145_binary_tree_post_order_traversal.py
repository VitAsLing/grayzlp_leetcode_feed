"""
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Iteratively
    def postorderTraversal(self, root):
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
                ans.insert(0, cur.val)
                cur = cur.right
            cur = queue.pop()
            cur = cur.left
        return ans

    # Recursively
    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.helper(ans, root)
        return ans

    def helper(self, res, root):
        if not root:
            return
        self.helper(res, root.left)
        self.helper(res, root.right)
        res.append(root.val)


# Test code
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4
print Solution().postorderTraversal(n1)
