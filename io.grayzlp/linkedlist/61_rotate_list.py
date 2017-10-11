"""
https://leetcode.com/problems/rotate-list/description/

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        count = 1
        tail = head
        while tail.next is not None:
            tail = tail.next
            count += 1
        tail.next = head

        k %= count
        if k != 0:
            for i in range(0, count - k):
                tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

ret = Solution().rotateRight(None, 0)
while ret is not None:
    print ret.val
    ret = ret.next
