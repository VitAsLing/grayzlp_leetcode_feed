"""
https://leetcode.com/problems/merge-k-sorted-lists/description/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
from Queue import PriorityQueue


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        queue = PriorityQueue()
        for node in lists:
            queue.put((node.val, node))
        cur = dummy
        while queue.qsize() > 0:
            cur.next = queue.get()[1]
            cur = cur.next
            if cur.next is not None:
                queue.put((cur.next.val, cur.next))
        return dummy.next


# Test code
t = [ListNode(1), ListNode(0)]
result = Solution().mergeKLists(t)
while result is not None:
    print result.val
    result = result.next
