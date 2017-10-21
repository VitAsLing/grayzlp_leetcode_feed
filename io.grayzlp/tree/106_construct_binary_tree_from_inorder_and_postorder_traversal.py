"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(len(postorder) - 1, 0, len(inorder) - 1, inorder, postorder)

    def helper(self, post_end, in_start, in_end, inorder, postorder):
        if post_end < 0 or in_start > in_end:
            return None
        root = TreeNode(postorder[post_end])
        root_index_in_inorder = -1
        for i in range(in_start, in_end + 1):
            if inorder[i] == root.val:
                root_index_in_inorder = i
                break
        root.left = self.helper(post_end - in_end + root_index_in_inorder - 1, in_start, root_index_in_inorder - 1,
                           inorder, postorder)
        root.right = self.helper(post_end - 1, root_index_in_inorder + 1, in_end, inorder, postorder)
        return root


# Test code
res = Solution().buildTree([2, 1, 3], [2, 3, 1])
print res.val
print res.left.val
print res.right.val
