"""
https://leetcode.com/problems/partition-list/description/

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        sentinel_small = ListNode(0)
        sentinel_big = ListNode(0)
        tail_small = sentinel_small
        tail_big = sentinel_big
        while head is not None:
            if head.val < x:
                tail_small.next = head
                tail_small = head
                head = head.next
            else:
                tail_big.next = head
                tail_big = head
                head = head.next
        tail_big.next = None
        tail_small.next = sentinel_big.next
        return sentinel_small.next


# Test code
l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4

res = Solution().partition(None, 3)
while res:
    print res.val
    res = res.next