"""
https://leetcode.com/problems/insertion-sort-list/description/

Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        left = self.insertionSortList(head.next)

        # find correct position
        pre = None
        cur = left
        while cur and cur.val < head.val:
            pre = cur
            cur = cur.next
        if not pre and not cur:
            return head
        if pre and not cur:
            pre.next = head
            head.next = None
            return left
        if not pre and cur:
            head.next = left
            return head
        if pre and cur:
            pre.next = head
            head.next = cur
            return left


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l4
l4.next = l3
l3.next = l2
node = Solution().insertionSortList(l1)
while node:
    print node.val
    node = node.next
