"""
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""


# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode(0)
        cur = sentinel
        add = 0
        while l1 is not None or l2 is not None:
            add /= 10
            if l1 is not None:
                add += l1.val
                l1 = l1.next
            if l2 is not None:
                add += l2.val
                l2 = l2.next
            cur.next = ListNode(add % 10)
            cur = cur.next
        if (add / 10) == 1:
            cur.next = ListNode(add / 10)
        return sentinel.next


# Test code
# 473
ll1 = ListNode(3)
ll2 = ListNode(7)
ll3 = ListNode(4)
ll1.next = ll2
ll2.next = ll3
# 37
rl1 = ListNode(3)
rl2 = ListNode(7)
rl1.next = rl2

ret = Solution().addTwoNumbers(ListNode(5), ListNode(5))
while ret is not None:
    print ret.val
    ret = ret.next

