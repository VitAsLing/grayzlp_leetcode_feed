"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/


Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Recursively
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, begin, end):
        if begin == end:
            return TreeNode(nums[begin])
        if begin > end:
            return None
        mid = (begin + end + 1) / 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, begin, mid - 1)
        root.right = self.helper(nums, mid + 1, end)
        return root


# Test code
res = Solution().sortedArrayToBST([1, 2, 3])
print res.val, res.left.val, res.right.val
