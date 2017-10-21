"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
Given preorder and inorder traversal of a tree, construct the binary tree.

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, 0, len(inorder) - 1, preorder, inorder)

    def helper(self, pre_start, in_start, in_end, preorder, inorder):
        if pre_start >= len(preorder) or in_start > in_end:
            return None
        root = TreeNode(preorder[pre_start])
        in_index_of_root = -1
        for i in range(in_start, in_end + 1):
            if inorder[i] == root.val:
                in_index_of_root = i
                break
        root.left = self.helper(pre_start + 1, in_start, in_index_of_root - 1, preorder, inorder)
        root.right = self.helper(pre_start + in_index_of_root - in_start + 1, in_index_of_root + 1, in_end, preorder,
                                 inorder)
        return root


# Test code
res = Solution().buildTree([1, 2, 3], [2, 1, 3])
print res.val
print res.left.val
print res.right.val
