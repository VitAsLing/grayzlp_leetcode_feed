"""
https://leetcode.com/problems/linked-list-cycle/description/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        quick = head
        slow = head
        while quick.next and quick.next.next:
            slow = slow.next
            quick = quick.next.next
            if slow == quick:
                return True
        return False


# Test code
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
print Solution().hasCycle(n1)
