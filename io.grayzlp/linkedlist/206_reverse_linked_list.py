"""
https://leetcode.com/problems/reverse-linked-list/description/


Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # Iteratively
    def reverseList(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev

    # Recursively
    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse_help(head, None)

    def reverse_help(self, head, prev):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse_help(next, head)


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
res = Solution().reverseList(l1)
while res:
    print res.val
    res = res.next

