"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return self.helper(head, count)

    def helper(self, head, count):
        if not head or count == 0:
            return None
        if count == 1:
            return TreeNode(head.val)
        half = count / 2
        cur = head
        for i in range(0, half):
            cur = cur.next
        root = TreeNode(cur.val)
        root.left = self.helper(head, half)
        root.right = self.helper(cur.next, count - half - 1)
        return root


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
res = Solution().sortedListToBST(l1)
print res.val, res.left.val, res.right.val
