"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        nth_pre = sentinel
        current = sentinel
        for i in range(n):
            current = current.next
        while current.next is not None:
            current = current.next
            nth_pre = nth_pre.next
        nth_pre.next = nth_pre.next.next
        return sentinel.next


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

node = Solution().removeNthFromEnd(l1, 2)
while node is not None:
    print node.val
    node = node.next
