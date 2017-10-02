"""
https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        count = 0
        while cur is not None and count != k:
            cur = cur.next
            count += 1
        if count == k:
            cur = self.reverseKGroup(cur, k)
            while count != 0:
                count -= 1
                tmp = head.next
                head.next = cur
                cur = head
                head = tmp
            head = cur
        return head


# Test code
l1 = ListNode(0)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
ret = Solution().reverseKGroup(l1, 1)
while ret is not None:
    print ret.val
    ret = ret.next
