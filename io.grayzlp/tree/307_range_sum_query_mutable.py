"""
https://leetcode.com/problems/range-sum-query-mutable/description/

Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

"""


class SegmentTreeNode(object):

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = 0


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.root = self.buildTree(nums, 0, len(nums) - 1)

    def buildTree(self, nums, start, end):
        ret = SegmentTreeNode(start, end)
        if start == end:
            ret.sum = nums[start]
        elif start < end:
            mid = start + (end - start) / 2
            ret.left = self.buildTree(nums, start, mid)
            ret.right = self.buildTree(nums, mid + 1, end)
            ret.sum = ret.left.sum + ret.right.sum
        return ret

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.updateInternal(self.root, i, val)

    def updateInternal(self, node, i, val):
        if node.start == node.end == i:
            node.sum = val
        elif node.start <= i <= node.end:
            mid = node.start + (node.end - node.start) / 2
            if i <= mid:
                self.updateInternal(node.left, i, val)
            elif i >= (mid + 1):
                self.updateInternal(node.right, i, val)
            node.sum = node.left.sum + node.right.sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumRangeInternal(self.root, i, j)

    def sumRangeInternal(self, node, i, j):
        if node.start >= i and node.end <= j:
            return node.sum
        elif node.start > j or node.end < i:
            return 0
        else:
            mid = node.start + (node.end - node.start) / 2
            if j < mid + 1:
                return self.sumRangeInternal(node.left, i, j)
            elif i > mid:
                return self.sumRangeInternal(node.right, i, j)
            else:
                return self.sumRangeInternal(node.left, i, j) + self.sumRangeInternal(node.right, i, j)


# Test code
obj = NumArray([1, 2, 3, 4, 5, 6])
obj.update(0, 0)
print (obj.sumRange(0, 5))
