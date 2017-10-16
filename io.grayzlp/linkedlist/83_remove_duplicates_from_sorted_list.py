"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        prev = sentinel
        cur = head
        while cur is not None:

            while cur.next is not None and cur.val == cur.next.val:
                cur = cur.next
            prev.next = cur
            prev = cur
            cur = cur.next
        return sentinel.next


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l4 = ListNode(3)
l5 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

res = Solution().deleteDuplicates(l1)
while res:
    print res.val
    res = res.next
