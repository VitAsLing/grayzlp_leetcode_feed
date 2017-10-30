"""
https://leetcode.com/problems/linked-list-cycle-ii/description/


Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        quick = head
        slow = head
        cycle = False
        while quick.next and quick.next.next:
            quick = quick.next.next
            slow = slow.next
            if quick == slow:
                cycle = True
                break
        if not cycle:
            return None
        first = head
        while first != slow:
            first = first.next
            slow = slow.next
        return first


# Test code
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2
print Solution().detectCycle(n1).val
