"""
https://leetcode.com/problems/reorder-list/description/

Given a singly linked list L: L0->L1->...->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next

        pre_mid = p1
        pre_current = p1.next
        while pre_current and pre_current.next:
            current = pre_current.next
            pre_current.next = current.next
            current.next = pre_mid.next
            pre_mid.next = current

        p = head
        right = pre_mid
        while p != right:
            next = right.next
            right.next = next.next
            next.next = p.next
            p.next = next
            p = next.next


# Test code
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

Solution().reorderList(n4)
res = n1
while res:
    print res.val
    res = res.next
