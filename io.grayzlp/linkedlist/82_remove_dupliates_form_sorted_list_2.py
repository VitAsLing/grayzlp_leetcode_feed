"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

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
            if prev.next == cur:
                prev = cur
                cur = cur.next
            else:
                # exists duplicates
                prev.next = cur.next
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

res = Solution().deleteDuplicates(l3)
while res:
    print res.val
    res = res.next

