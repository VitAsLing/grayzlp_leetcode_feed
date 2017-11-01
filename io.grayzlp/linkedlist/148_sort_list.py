"""
https://leetcode.com/problems/sort-list/description/

Sort a linked list in O(n log n) time using constant space complexity.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        res = self.merge(l1, l2)
        return res

    # Merge sort
    def merge(self, lhs, rhs):
        sentinel = ListNode(-1)
        cur = sentinel
        while lhs and rhs:
            if lhs.val < rhs.val:
                cur.next = lhs
                lhs = lhs.next
            else:
                cur.next = rhs
                rhs = rhs.next
            cur = cur.next
        while lhs:
            cur.next = lhs
            cur = cur.next
            lhs = lhs.next
        while rhs:
            cur.next = rhs
            cur = cur.next
            rhs = rhs.next
        return sentinel.next


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l4
l4.next = l3
l3.next = l2
node = Solution().sortList(l1)
while node:
    print node.val
    node = node.next
