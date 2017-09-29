"""
https://leetcode.com/problems/merge-two-sorted-lists/description/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        current = sentinel
        lhs = l1
        rhs = l2
        while lhs is not None or rhs is not None:
            if lhs is None:
                current.next = rhs
                current = current.next
                rhs = rhs.next
            elif rhs is None:
                current.next = lhs
                current = current.next
                lhs = lhs.next
            else:
                if lhs.val < rhs.val:
                    current.next = lhs
                    current = current.next
                    lhs = lhs.next
                else:
                    current.next = rhs
                    current = current.next
                    rhs = rhs.next
        return sentinel.next


# Test code
l1 = ListNode(3)
l2 = ListNode(10)
l1.next = l2
r1 = ListNode(4)
r2 = ListNode(9)
r1.next = r2

ret = Solution().mergeTwoLists(l1, r1)
while ret is not None:
    print ret.val
    ret = ret.next
