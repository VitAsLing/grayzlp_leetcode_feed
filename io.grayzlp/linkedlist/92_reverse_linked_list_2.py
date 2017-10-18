"""
https://leetcode.com/problems/reverse-linked-list-ii/description/

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        sentinel.next = head
        prev = sentinel
        for i in range(0, m - 1):
            prev = prev.next
        start = prev.next
        then = start.next
        for j in range(0, n - m):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        return sentinel.next


# Test code
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
res = Solution().reverseBetween(l1, 2, 3)
while res:
    print res.val
    res = res.next
